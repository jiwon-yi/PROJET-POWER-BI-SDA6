# 📊 PROJET POWER BI - SDA6 2025
## Business Intelligence - Panthéon-Sorbonne Data Analytics

### 🎯 Description
Système décisionnel complet pour l'analyse des ventes d'une chaîne de distribution (5 enseignes, 200 transactions)

### 📁 Structure du Projet
```
PROJET-POWER-BI-SDA6/
├── 01_data/
│   ├── raw/              # Données sources (4 CSV)
│   ├── processed/        # Tables transformées (5 CSV)
│   └── warehouse/        # Base SQLite
├── 02_database/          # Scripts SQL
│   ├── ddl/              # Création des tables
│   └── dml/              # Manipulation données
├── 03_etl/               # Pipeline ETL Python
├── 04_analysis/          # Analyses exploratoires
├── 05_visualization/     # Power BI
├── 06_documentation/     # Documentation
└── 07_tests/             # Tests
```

### 🚀 Quick Start

#### 1. Cloner le repo
```bash
git clone https://github.com/jiwon-yi/PROJET-POWER-BI-SDA6.git
cd PROJET-POWER-BI-SDA6
```

#### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

#### 3. Générer le Data Warehouse
```bash
python setup_complete_project.py
```

### 📊 Métriques Clés
| Métrique | Valeur |
|----------|--------|
| Transactions | 200 |
| Produits | 50 |
| Enseignes | 5 |
| Catégories | 10 |
| Période | 2023-2024 |

### 🏢 Enseignes
- **Paris** - Enseigne Alpha
- **Lyon** - Enseigne Beta  
- **Marseille** - Enseigne Gamma
- **Toulouse** - Enseigne Delta
- **Nice** - Enseigne Epsilon

### 📈 Modèle de Données
**Star Schema (Schéma en étoile)**

#### Table de Faits
- `fact_ventes` - 200 transactions avec métriques

#### Dimensions
- `dim_temps` - Hiérarchie temporelle
- `dim_produit` - Catalogue produits
- `dim_enseigne` - Points de vente
- `dim_categorie` - Classification produits

### 🛠 Stack Technique
| Composant | Technologie |
|-----------|-------------|
| ETL | Python (pandas, SQLAlchemy) |
| Base de données | SQLite |
| Modélisation | Star Schema |
| Visualisation | Power BI |
| Version Control | Git/GitHub |

### 📝 Fichiers Principaux
- `setup_complete_project.py` - Script principal
- `03_etl/00_create_data.py` - Génération des données
- `03_etl/02_etl_pipeline.py` - Pipeline ETL
- `04_analysis/01_data_exploration.py` - Analyse exploratoire

### 📊 Power BI - Guide Rapide
1. Importer les CSV depuis `01_data/processed/`
2. Créer les relations entre les tables
3. Implémenter les mesures DAX
4. Créer les visualisations

### 🎓 Contexte Académique
- **Université** : Paris 1 Panthéon-Sorbonne
- **Formation** : Data Analytics
- **Module** : POWER BI
- **Année** : 2024-2025

### 📧 Contact
**GitHub** : [jiwon-yi](https://github.com/jiwon-yi)

---
© 2024 Projet BI SDA6 - Panthéon-Sorbonne
