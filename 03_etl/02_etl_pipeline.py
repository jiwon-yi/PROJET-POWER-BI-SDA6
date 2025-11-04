#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ETL Pipeline - Construction du Data Warehouse"""

import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataWarehouseETL:
    def __init__(self, source_path='01_data/raw/', target_path='01_data/warehouse/'):
        self.source_path = source_path
        self.target_path = target_path
        self.dataframes = {}
        os.makedirs(target_path, exist_ok=True)
        
    def extract(self):
        logger.info("="*60)
        logger.info("PHASE 1: EXTRACTION DES DONNÉES")
        logger.info("="*60)
        
        files = {
            'ventes': 'ventes.csv',
            'produits': 'produits.csv',
            'categories': 'categories.csv',
            'enseignes': 'enseignes.csv'
        }
        
        for name, file in files.items():
            df = pd.read_csv(f"{self.source_path}{file}")
            self.dataframes[name] = df
            logger.info(f"✅ {name}: {len(df)} lignes extraites")
    
    def transform(self):
        logger.info("\nPHASE 2: TRANSFORMATION DES DONNÉES")
        logger.info("="*60)
        
        # DIM_TEMPS
        logger.info("📅 Création de DIM_TEMPS...")
        ventes = self.dataframes['ventes']
        ventes['Date_vente'] = pd.to_datetime(ventes['Date_vente'])
        
        dates = pd.date_range(
            start=ventes['Date_vente'].min(),
            end=ventes['Date_vente'].max(),
            freq='D'
        )
        
        dim_temps = pd.DataFrame({
            'id_temps': range(1, len(dates) + 1),
            'date_complete': dates,
            'annee': dates.year,
            'mois': dates.month,
            'jour': dates.day,
            'trimestre': dates.quarter,
            'semaine': dates.isocalendar().week,
            'jour_semaine': dates.dayofweek + 1,
            'nom_jour': dates.strftime('%A'),
            'nom_mois': dates.strftime('%B'),
            'est_weekend': (dates.dayofweek >= 5).astype(int)
        })
        logger.info(f"  ✅ {len(dim_temps)} dates créées")
        
        # DIM_PRODUIT
        logger.info("📦 Création de DIM_PRODUIT...")
        produits = self.dataframes['produits']
        categories = self.dataframes['categories']
        
        dim_produit = produits.merge(categories, on='Reference_Categorie', how='left')
        dim_produit['id_produit'] = range(1, len(dim_produit) + 1)
        
        dim_produit['gamme_prix'] = pd.cut(
            dim_produit['Prix'],
            bins=[0, 100, 500, 1000, float('inf')],
            labels=['Économique', 'Standard', 'Premium', 'Luxe']
        )
        logger.info(f"  ✅ {len(dim_produit)} produits transformés")
        
        # DIM_ENSEIGNE
        logger.info("🏪 Création de DIM_ENSEIGNE...")
        enseignes = self.dataframes['enseignes']
        dim_enseigne = enseignes.copy()
        dim_enseigne['id_enseigne'] = range(1, len(dim_enseigne) + 1)
        dim_enseigne['region'] = dim_enseigne['Ville'].map({
            'Paris': 'Île-de-France',
            'Lyon': 'Auvergne-Rhône-Alpes',
            'Marseille': 'Provence-Alpes-Côte d\'Azur',
            'Toulouse': 'Occitanie',
            'Nice': 'Provence-Alpes-Côte d\'Azur'
        })
        logger.info(f"  ✅ {len(dim_enseigne)} enseignes transformées")
        
        # DIM_CATEGORIE
        logger.info("🏷️ Création de DIM_CATEGORIE...")
        dim_categorie = categories.copy()
        dim_categorie['id_categorie'] = range(1, len(dim_categorie) + 1)
        dim_categorie['super_categorie'] = dim_categorie['Categorie'].map({
            'Électronique': 'High-Tech',
            'Alimentaire': 'Consommation',
            'Papeterie': 'Bureau',
            'Mobilier': 'Maison',
            'Vêtements': 'Mode',
            'Jouets': 'Loisirs',
            'Sport': 'Loisirs',
            'Beauté': 'Bien-être',
            'Santé': 'Bien-être',
            'Automobile': 'Transport'
        })
        logger.info(f"  ✅ {len(dim_categorie)} catégories transformées")
        
        # FACT_VENTES
        logger.info("💼 Création de FACT_VENTES...")
        ventes = self.dataframes['ventes'].copy()
        ventes['Date_vente'] = pd.to_datetime(ventes['Date_vente'])
        
        date_to_id = dict(zip(dim_temps['date_complete'], dim_temps['id_temps']))
        ventes['id_temps'] = ventes['Date_vente'].map(date_to_id)
        
        prod_to_id = dict(zip(dim_produit['Reference_Produit'], dim_produit['id_produit']))
        ventes['id_produit'] = ventes['Reference_Produit'].map(prod_to_id)
        
        ens_to_id = dict(zip(dim_enseigne['Enseigne'], dim_enseigne['id_enseigne']))
        ventes['id_enseigne'] = ventes['Enseigne'].map(ens_to_id)
        
        fact_ventes = pd.DataFrame({
            'id_vente': ventes['IDVente'],
            'id_temps': ventes['id_temps'],
            'id_produit': ventes['id_produit'],
            'id_enseigne': ventes['id_enseigne'],
            'quantite': ventes['Quantite'],
            'prix_unitaire': ventes['Prix_Total'] / ventes['Quantite'],
            'prix_total': ventes['Prix_Total'],
            'cout_estime': ventes['Prix_Total'] * 0.7,
            'marge_brute': ventes['Prix_Total'] * 0.3
        })
        logger.info(f"  ✅ {len(fact_ventes)} transactions transformées")
        
        return dim_temps, dim_produit, dim_enseigne, dim_categorie, fact_ventes
    
    def load(self, dim_temps, dim_produit, dim_enseigne, dim_categorie, fact_ventes):
        logger.info("\nPHASE 3: CHARGEMENT DANS LE DATA WAREHOUSE")
        logger.info("="*60)
        
        # SQLite
        db_path = f"{self.target_path}datawarehouse.db"
        conn = sqlite3.connect(db_path)
        
        dim_temps.to_sql('dim_temps', conn, if_exists='replace', index=False)
        logger.info(f"✅ DIM_TEMPS chargée")
        
        dim_produit.to_sql('dim_produit', conn, if_exists='replace', index=False)
        logger.info(f"✅ DIM_PRODUIT chargée")
        
        dim_enseigne.to_sql('dim_enseigne', conn, if_exists='replace', index=False)
        logger.info(f"✅ DIM_ENSEIGNE chargée")
        
        dim_categorie.to_sql('dim_categorie', conn, if_exists='replace', index=False)
        logger.info(f"✅ DIM_CATEGORIE chargée")
        
        fact_ventes.to_sql('fact_ventes', conn, if_exists='replace', index=False)
        logger.info(f"✅ FACT_VENTES chargée")
        
        conn.close()
        
        # Export CSV pour Power BI
        csv_path = '01_data/processed/'
        os.makedirs(csv_path, exist_ok=True)
        
        dim_temps.to_csv(f'{csv_path}dim_temps.csv', index=False)
        dim_produit.to_csv(f'{csv_path}dim_produit.csv', index=False)
        dim_enseigne.to_csv(f'{csv_path}dim_enseigne.csv', index=False)
        dim_categorie.to_csv(f'{csv_path}dim_categorie.csv', index=False)
        fact_ventes.to_csv(f'{csv_path}fact_ventes.csv', index=False)
        
        logger.info(f"✅ Tables exportées dans {csv_path}")
        logger.info(f"\n✅ Data Warehouse créé: {db_path}")
    
    def run_etl(self):
        logger.info("🚀 DÉMARRAGE DU PIPELINE ETL")
        self.extract()
        dim_temps, dim_produit, dim_enseigne, dim_categorie, fact_ventes = self.transform()
        self.load(dim_temps, dim_produit, dim_enseigne, dim_categorie, fact_ventes)
        logger.info("\n🎉 PIPELINE ETL TERMINÉ AVEC SUCCÈS!")

if __name__ == "__main__":
    etl = DataWarehouseETL()
    etl.run_etl()
