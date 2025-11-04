#!/usr/bin/env python3
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
    
    print("\n✅ Tous les fichiers de données ont été créés dans 01_data/raw/")
    return df_ventes, df_produits, df_categories, df_enseignes

if __name__ == "__main__":
    create_data_files()
