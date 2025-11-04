#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyse Exploratoire des Données (EDA)
Projet BI - Panthéon-Sorbonne Data Analytics
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configuration
plt.style.use('seaborn-v0_8-darkgrid')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

class DataExplorer:
    """Classe pour l'analyse exploratoire des données"""
    
    def __init__(self, data_path='01_data/raw/'):
        self.data_path = data_path
        self.dataframes = {}
        self.load_data()
        
    def load_data(self):
        """Charger tous les fichiers CSV"""
        print("=" * 80)
        print("CHARGEMENT DES DONNÉES")
        print("=" * 80)
        
        files = {
            'ventes': 'ventes.csv',
            'produits': 'produits.csv',
            'categories': 'categories.csv',
            'enseignes': 'enseignes.csv'
        }
        
        for name, file in files.items():
            try:
                df = pd.read_csv(f"{self.data_path}{file}")
                self.dataframes[name] = df
                print(f"✅ {name}: {len(df)} lignes, {len(df.columns)} colonnes")
            except Exception as e:
                print(f"❌ Erreur lors du chargement de {file}: {e}")
                
    def basic_info(self):
        """Informations basiques sur chaque dataset"""
        print("\n" + "=" * 80)
        print("INFORMATIONS GÉNÉRALES")
        print("=" * 80)
        
        for name, df in self.dataframes.items():
            print(f"\n📊 DATASET: {name.upper()}")
            print("-" * 40)
            print(f"Dimensions: {df.shape}")
            print(f"Colonnes: {list(df.columns)}")
            print(f"Types de données:")
            print(df.dtypes)
            print(f"\nValeurs manquantes:")
            print(df.isnull().sum())
            print(f"\nPremières lignes:")
            print(df.head(3))
            
    def data_quality_check(self):
        """Vérification de la qualité des données"""
        print("\n" + "=" * 80)
        print("CONTRÔLE QUALITÉ DES DONNÉES")
        print("=" * 80)
        
        issues = []
        
        # Vérifier les ventes
        if 'ventes' in self.dataframes:
            ventes = self.dataframes['ventes']
            
            # Doublons
            duplicates = ventes.duplicated().sum()
            if duplicates > 0:
                issues.append(f"⚠️ {duplicates} doublons dans les ventes")
            
            # Dates invalides
            try:
                ventes['Date_vente'] = pd.to_datetime(ventes['Date_vente'])
                date_range = f"{ventes['Date_vente'].min()} à {ventes['Date_vente'].max()}"
                print(f"📅 Période des ventes: {date_range}")
            except:
                issues.append("⚠️ Problème avec les dates de vente")
            
            # Prix négatifs
            if 'Prix Total' in ventes.columns:
                negative_prices = (ventes['Prix Total'] < 0).sum()
                if negative_prices > 0:
                    issues.append(f"⚠️ {negative_prices} prix négatifs")
                    
        # Vérifier l'intégrité référentielle
        if 'ventes' in self.dataframes and 'produits' in self.dataframes:
            ventes = self.dataframes['ventes']
            produits = self.dataframes['produits']
            
            # Produits orphelins
            ventes_products = set(ventes['Reference Produit'].unique())
            available_products = set(produits['Reference_Produit'].unique())
            orphans = ventes_products - available_products
            
            if orphans:
                issues.append(f"⚠️ {len(orphans)} références produits introuvables")
                
        if issues:
            print("\n🔴 Problèmes détectés:")
            for issue in issues:
                print(f"  {issue}")
        else:
            print("\n✅ Aucun problème majeur détecté!")
            
    def statistical_summary(self):
        """Résumé statistique des données numériques"""
        print("\n" + "=" * 80)
        print("RÉSUMÉ STATISTIQUE")
        print("=" * 80)
        
        if 'ventes' in self.dataframes:
            ventes = self.dataframes['ventes']
            
            print("\n📈 Statistiques des Ventes:")
            print("-" * 40)
            
            # Convertir la date
            ventes['Date_vente'] = pd.to_datetime(ventes['Date_vente'])
            
            # Statistiques générales
            total_revenue = ventes['Prix Total'].sum()
            avg_transaction = ventes['Prix Total'].mean()
            total_quantity = ventes['Quantite'].sum()
            avg_quantity = ventes['Quantite'].mean()
            
            print(f"💰 Chiffre d'affaires total: {total_revenue:,.2f} €")
            print(f"📊 Nombre de transactions: {len(ventes)}")
            print(f"💵 Panier moyen: {avg_transaction:.2f} €")
            print(f"📦 Quantité totale vendue: {total_quantity:,.0f}")
            print(f"📦 Quantité moyenne par transaction: {avg_quantity:.2f}")
            
            # Top 5 enseignes
            print("\n🏪 Top 5 Enseignes par CA:")
            top_stores = ventes.groupby('Enseigne')['Prix Total'].sum().sort_values(ascending=False).head()
            for store, revenue in top_stores.items():
                print(f"  {store}: {revenue:,.2f} €")
            
            # Analyse temporelle
            print("\n📅 Analyse Temporelle:")
            ventes['Year'] = ventes['Date_vente'].dt.year
            ventes['Month'] = ventes['Date_vente'].dt.month
            yearly_sales = ventes.groupby('Year')['Prix Total'].sum()
            for year, revenue in yearly_sales.items():
                print(f"  {year}: {revenue:,.2f} €")
                
    def generate_insights(self):
        """Générer des insights automatiques"""
        print("\n" + "=" * 80)
        print("INSIGHTS CLÉS")
        print("=" * 80)
        
        insights = []
        
        if 'ventes' in self.dataframes:
            ventes = self.dataframes['ventes']
            ventes['Date_vente'] = pd.to_datetime(ventes['Date_vente'])
            
            # Meilleur mois
            ventes['YearMonth'] = ventes['Date_vente'].dt.to_period('M')
            best_month = ventes.groupby('YearMonth')['Prix Total'].sum().idxmax()
            best_month_revenue = ventes.groupby('YearMonth')['Prix Total'].sum().max()
            insights.append(f"📈 Meilleur mois: {best_month} ({best_month_revenue:,.2f} €)")
            
            # Produit star
            if 'produits' in self.dataframes:
                ventes_with_products = ventes.merge(
                    self.dataframes['produits'], 
                    left_on='Reference Produit', 
                    right_on='Reference_Produit',
                    how='left'
                )
                if 'Nom' in ventes_with_products.columns:
                    top_product = ventes_with_products.groupby('Nom')['Prix Total'].sum().idxmax()
                    top_product_revenue = ventes_with_products.groupby('Nom')['Prix Total'].sum().max()
                    insights.append(f"⭐ Produit star: {top_product} ({top_product_revenue:,.2f} €)")
            
            # Concentration des ventes
            top20_products = ventes.groupby('Reference Produit')['Prix Total'].sum().nlargest(20).sum()
            total_revenue = ventes['Prix Total'].sum()
            concentration = (top20_products / total_revenue) * 100
            insights.append(f"🎯 Les 20 meilleurs produits = {concentration:.1f}% du CA")
            
            # Saisonnalité
            ventes['Quarter'] = ventes['Date_vente'].dt.quarter
            q4_sales = ventes[ventes['Quarter'] == 4]['Prix Total'].sum()
            q4_percent = (q4_sales / total_revenue) * 100
            insights.append(f"🎄 Q4 représente {q4_percent:.1f}% des ventes annuelles")
            
        print("\n💡 Insights découverts:")
        for i, insight in enumerate(insights, 1):
            print(f"{i}. {insight}")
            
    def export_summary(self):
        """Exporter un résumé de l'analyse"""
        summary = {
            'date_analyse': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'datasets': {}
        }
        
        for name, df in self.dataframes.items():
            summary['datasets'][name] = {
                'rows': len(df),
                'columns': len(df.columns),
                'missing_values': df.isnull().sum().sum(),
                'duplicates': df.duplicated().sum()
            }
            
        # Sauvegarder le résumé
        import json
        with open('01_data/processed/eda_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
            
        print("\n✅ Résumé exporté vers: 01_data/processed/eda_summary.json")
        
    def run_complete_analysis(self):
        """Exécuter l'analyse complète"""
        print("\n" + "🔍 ANALYSE EXPLORATOIRE DES DONNÉES " + "🔍")
        print("Projet BI - Panthéon-Sorbonne")
        print("=" * 80)
        
        self.basic_info()
        self.data_quality_check()
        self.statistical_summary()
        self.generate_insights()
        
        print("\n" + "=" * 80)
        print("ANALYSE TERMINÉE AVEC SUCCÈS ✅")
        print("=" * 80)


def main():
    """Fonction principale"""
    # Note: Ajuster le chemin selon votre structure
    explorer = DataExplorer(data_path='/mnt/project/')
    explorer.run_complete_analysis()
    
    # Pour exporter le résumé (créer d'abord les dossiers)
    # explorer.export_summary()


if __name__ == "__main__":
    main()
