# 📊 PROJET POWER BI - SDA6 2025
## Business Intelligence - Panthéon-Sorbonne Data Analytics

### 🎯 Description
Système décisionnel complet pour l'analyse des ventes d'une chaîne de distribution (5 enseignes, 200 transactions)

### 📁 Structure du Projet
\\\
PROJET-POWER-BI-SDA6/
├── 01_data/
│   ├── raw/              # Données sources (4 CSV)
│   ├── processed/        # Tables transformées (5 CSV)
│   └── warehouse/        # Base SQLite
├── 02_database/          # Scripts SQL
│   ├── ddl/             # Création des tables
│   └── dml/             # Manipulation données
├── 03_etl/              # Pipeline ETL Python
├── 04_analysis/         # Analyses exploratoires
├── 05_visualization/    # Power BI
├── 06_documentation/    # Documentation
└── 07_tests/           # Tests
\\\

### 🚀 Quick Start
\\\ash
# 1. Cloner le repo
git clone https://github.com/jiwon-yi/PROJET-POWER-BI-SDA6.git

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Générer le Data Warehouse
python setup_complete_project.py
\\\

### 📊 Métriques Clés
- **200 transactions** analysées
- **50 produits** en catalogue
- **5 enseignes** (Paris, Lyon, Marseille, Toulouse, Nice)
- **Modèle en étoile** optimisé

### 🛠 Stack Technique
- ETL: Python (pandas, SQLAlchemy)
- Database: SQLite
- Visualization: Power BI
- Modeling: Star Schema

### 📧 Contact
**Université**: Paris 1 Panthéon-Sorbonne  
**Formation**: Data Analytics  
**GitHub**: [jiwon-yi](https://github.com/jiwon-yi)

---
© 2024 Projet BI SDA6
