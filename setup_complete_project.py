#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE CRÉATION COMPLÈTE DU PROJET
Projet BI - Panthéon-Sorbonne Data Analytics
Ce script crée TOUS les fichiers et dossiers nécessaires
"""

import os
import sys
import shutil
from pathlib import Path

def create_directory_structure():
    """Créer tous les dossiers nécessaires"""
    directories = [
        "01_data/raw",
        "01_data/processed",
        "01_data/warehouse",
        "02_database/ddl",
        "02_database/dml",
        "02_database/views",
        "03_etl",
        "04_analysis/queries",
        "05_visualization/powerbi",
        "06_documentation/business",
        "06_documentation/technical",
        "07_tests"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Dossier créé: {directory}")

def create_data_creation_script():
    """Créer le script de génération des données"""
    content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pour créer les fichiers CSV de données"""

import pandas as pd
import os
import random
from datetime import datetime, timedelta

def create_data_files():
    os.makedirs('01_data/raw', exist_ok=True)
    
    # 1. ENSEIGNES
    enseignes_data = {
        'Enseigne': ['Enseigne Alpha', 'Enseigne Beta', 'Enseigne Gamma', 'Enseigne Delta', 'Enseigne Epsilon'],
        'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice'],
        'Adresse': ['123 Rue de Paris', '456 Rue de Lyon', '789 Rue de Marseille', '101 Rue de Toulouse', '202 Rue de Nice']
    }
    df_enseignes = pd.DataFrame(enseignes_data)
    df_enseignes.to_csv('01_data/raw/enseignes.csv', index=False)
    print(f"✅ enseignes.csv créé: {len(df_enseignes)} lignes")
    
    # 2. CATEGORIES
    categories_data = {
        'Reference_Categorie': ['HGKFLAO4', 'X4DVDP1R', 'FCY1Z3AD', 'BHPBGMP8', '2ATURREX', 
                                'VYOSD42Y', 'WB3615LA', '5U2QY0OE', '6CFXB8S3', 'I9IXI9VN'],
        'Categorie': ['Électronique', 'Alimentaire', 'Papeterie', 'Mobilier', 'Vêtements',
                     'Jouets', 'Sport', 'Beauté', 'Santé', 'Automobile'],
        'Description': ['Électronique', 'Alimentaire', 'Papeterie', 'Mobilier', 'Vêtements',
                       'Jouets', 'Sport', 'Beauté', 'Santé', 'Automobile']
    }
    df_categories = pd.DataFrame(categories_data)
    df_categories.to_csv('01_data/raw/categories.csv', index=False)
    print(f"✅ categories.csv créé: {len(df_categories)} lignes")
    
    # 3. PRODUITS
    produits_data = {
        'Reference_Produit': [],
        'Nom': [],
        'Reference_Categorie': [],
        'Prix': []
    }
    
    produits_liste = [
        ('23MAGJD9', 'Téléphone', 'HGKFLAO4', 1030),
        ('FTX48SNW', 'Ordinateur', 'HGKFLAO4', 178),
        ('A4A4AEW6', 'Télévision', 'HGKFLAO4', 269),
        ('X3FNDA2D', 'Tablette', 'HGKFLAO4', 1104),
        ('Q1K0RDPN', 'Casque', 'HGKFLAO4', 1169),
        ('M9OZGE36', 'Café', 'X4DVDP1R', 60),
        ('3JESS2RQ', 'Thé', 'X4DVDP1R', 1920),
        ('U75V4RGE', 'Chocolat', 'X4DVDP1R', 1234),
        ('UTR2K7LI', 'Biscuits', 'X4DVDP1R', 951),
        ('1TO8DT10', 'Céréales', 'X4DVDP1R', 1737),
        ('95KNZG8Q', 'Cahier', 'FCY1Z3AD', 1028),
        ('J64TA6WE', 'Stylo', 'FCY1Z3AD', 44),
        ('YK7FXJAX', 'Crayon', 'FCY1Z3AD', 1900),
        ('7EEXZCTL', 'Gomme', 'FCY1Z3AD', 1792),
        ('HGY2FBWC', 'Règle', 'FCY1Z3AD', 1547),
        ('R4XH25O7', 'Chaise', 'BHPBGMP8', 1704),
        ('XE3D1521', 'Table', 'BHPBGMP8', 202),
        ('3H8TUYIQ', 'Canapé', 'BHPBGMP8', 2000),
        ('TMN8A5BC', 'Lit', 'BHPBGMP8', 922),
        ('QSGOF1NR', 'Armoire', 'BHPBGMP8', 998),
        ('OXM2O3WT', 'T-shirt', '2ATURREX', 982),
        ('BAEHGJPU', 'Jean', '2ATURREX', 349),
        ('SODO5Y83', 'Veste', '2ATURREX', 1432),
        ('FRM9CKO2', 'Sweat', '2ATURREX', 1043),
        ('UUTE2LOB', 'Chaussures', '2ATURREX', 341),
        ('N5LV7W5S', 'Poupée', 'VYOSD42Y', 1757),
        ('7O2LARCO', 'Lego', 'VYOSD42Y', 1587),
        ('RV694FWE', 'Puzzle', 'VYOSD42Y', 1441),
        ('P5GU8M9T', 'Voiture', 'VYOSD42Y', 700),
        ('LY7E0L37', 'Jeu de société', 'VYOSD42Y', 177),
        ('1Q73T12C', 'Ballon', 'WB3615LA', 1471),
        ('VE83H8IM', 'Raquette', 'WB3615LA', 844),
        ('L1FS467F', 'Vélo', 'WB3615LA', 1244),
        ('A5I0K1K3', 'Tapis de yoga', 'WB3615LA', 652),
        ('25JLQLY7', 'Haltère', 'WB3615LA', 111),
        ('W1N5JI2N', 'Shampooing', '5U2QY0OE', 1517),
        ('D3B17ZSN', 'Crème', '5U2QY0OE', 690),
        ('JNMIDJK5', 'Parfum', '5U2QY0OE', 1069),
        ('ULPCQDRS', 'Maquillage', '5U2QY0OE', 350),
        ('ZKBEBE26', 'Brosse', '5U2QY0OE', 1182),
        ('KM1IRIL1', 'Vitamines', '6CFXB8S3', 818),
        ('X4VVEZEA', 'Médicaments', '6CFXB8S3', 1757),
        ('PRSHKGFT', 'Bandages', '6CFXB8S3', 335),
        ('Q8KWKNGV', 'Thermomètre', '6CFXB8S3', 699),
        ('5X4YX1CL', 'Tensiomètre', '6CFXB8S3', 1602),
        ('ZMZV43PY', 'Pneu', 'I9IXI9VN', 1942),
        ('W9S1PNY2', 'Batterie', 'I9IXI9VN', 651),
        ('5G3VLXI9', 'Huile moteur', 'I9IXI9VN', 396),
        ('PFH0KAG5', 'Balais essuie-glace', 'I9IXI9VN', 327),
        ('IUN5F5QH', 'Filtre à air', 'I9IXI9VN', 1926)
    ]
    
    for ref, nom, cat, prix in produits_liste:
        produits_data['Reference_Produit'].append(ref)
        produits_data['Nom'].append(nom)
        produits_data['Reference_Categorie'].append(cat)
        produits_data['Prix'].append(prix)
    
    df_produits = pd.DataFrame(produits_data)
    df_produits.to_csv('01_data/raw/produits.csv', index=False)
    print(f"✅ produits.csv créé: {len(df_produits)} lignes")
    
    # 4. VENTES (200 transactions)
    random.seed(42)
    ventes_data = {
        'IDVente': list(range(1, 201)),
        'Date_vente': [],
        'Reference_Produit': [],
        'Quantite': [],
        'Enseigne': [],
        'Prix_Total': []
    }
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    for i in range(200):
        days_between = (end_date - start_date).days
        random_days = random.randint(0, days_between)
        random_date = start_date + timedelta(days=random_days)
        ventes_data['Date_vente'].append(random_date.strftime('%Y-%m-%d'))
        
        product = random.choice(produits_data['Reference_Produit'])
        ventes_data['Reference_Produit'].append(product)
        
        quantity = random.randint(1, 10)
        ventes_data['Quantite'].append(quantity)
        
        store = random.choice(enseignes_data['Enseigne'])
        ventes_data['Enseigne'].append(store)
        
        product_idx = produits_data['Reference_Produit'].index(product)
        unit_price = produits_data['Prix'][product_idx]
        total_price = unit_price * quantity
        ventes_data['Prix_Total'].append(total_price)
    
    df_ventes = pd.DataFrame(ventes_data)
    df_ventes.to_csv('01_data/raw/ventes.csv', index=False)
    print(f"✅ ventes.csv créé: {len(df_ventes)} lignes")
    
    print("\\n✅ Tous les fichiers de données ont été créés dans 01_data/raw/")
    return df_ventes, df_produits, df_categories, df_enseignes

if __name__ == "__main__":
    create_data_files()
'''
    
    with open('03_etl/00_create_data.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Fichier créé: 03_etl/00_create_data.py")

def create_etl_pipeline():
    """Créer le pipeline ETL principal"""
    content = '''#!/usr/bin/env python3
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
        logger.info("\\nPHASE 2: TRANSFORMATION DES DONNÉES")
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
            'Marseille': 'Provence-Alpes-Côte d\\'Azur',
            'Toulouse': 'Occitanie',
            'Nice': 'Provence-Alpes-Côte d\\'Azur'
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
        logger.info("\\nPHASE 3: CHARGEMENT DANS LE DATA WAREHOUSE")
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
        logger.info(f"\\n✅ Data Warehouse créé: {db_path}")
    
    def run_etl(self):
        logger.info("🚀 DÉMARRAGE DU PIPELINE ETL")
        self.extract()
        dim_temps, dim_produit, dim_enseigne, dim_categorie, fact_ventes = self.transform()
        self.load(dim_temps, dim_produit, dim_enseigne, dim_categorie, fact_ventes)
        logger.info("\\n🎉 PIPELINE ETL TERMINÉ AVEC SUCCÈS!")

if __name__ == "__main__":
    etl = DataWarehouseETL()
    etl.run_etl()
'''
    
    with open('03_etl/02_etl_pipeline.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Fichier créé: 03_etl/02_etl_pipeline.py")

def main():
    print("="*60)
    print("🚀 CRÉATION COMPLÈTE DU PROJET BI SORBONNE")
    print("="*60)
    print()
    
    # 1. Créer la structure
    print("📁 Création de la structure des dossiers...")
    create_directory_structure()
    print()
    
    # 2. Créer les scripts Python
    print("🐍 Création des scripts Python...")
    create_data_creation_script()
    create_etl_pipeline()
    print()
    
    # 3. Exécuter la création des données
    print("📊 Génération des données...")
    os.system("python 03_etl/00_create_data.py")
    print()
    
    # 4. Exécuter l'ETL
    print("🔧 Construction du Data Warehouse...")
    os.system("python 03_etl/02_etl_pipeline.py")
    print()
    
    print("="*60)
    print("✅ PROJET CRÉÉ AVEC SUCCÈS!")
    print("="*60)
    print()
    print("📌 Prochaines étapes:")
    print("  1. Ouvrir Power BI Desktop")
    print("  2. Importer les CSV depuis: 01_data/processed/")
    print("  3. Créer les relations entre les tables")
    print("  4. Développer les visualisations")
    print()
    print("📁 Structure créée:")
    print("  - 01_data/raw/ : Données sources")
    print("  - 01_data/processed/ : Tables pour Power BI")
    print("  - 01_data/warehouse/ : Base de données SQLite")
    print("  - 03_etl/ : Scripts ETL")
    print()

if __name__ == "__main__":
    main()
