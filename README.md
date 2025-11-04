# PROJET POWER BI - SDA7 2025
## Panthéon-Sorbonne Data Analytics

### 📊 Description du Projet
Développement d'un système décisionnel complet pour l'analyse des données de vente d'une chaîne de distribution avec 5 enseignes (Alpha, Beta, Gamma, Delta, Epsilon).

### 🎯 Objectifs
- Création d'un Data Warehouse optimisé
- Implémentation d'un modèle en étoile/flocon
- Développement de tableaux de bord interactifs Power BI
- Analyse des performances commerciales multi-enseignes

### 🛠 Technologies Utilisées
- **Base de données** : PostgreSQL / SQL Server
- **ETL** : Python (pandas, SQLAlchemy)
- **Visualisation** : Power BI
- **Cloud** : Azure Data Factory

### 📁 Structure des Données
- `ventes.csv` : 500 transactions
- `produits.csv` : 100 produits
- `categories.csv` : 10 catégories
- `enseignes.csv` : 5 points de vente

### 👨‍🎓 Équipe
Jiwon Yi

### 📧 Contact
Cours supervisé par : Ibrahim Tahirou
```

### **.gitignore 추천:**
```
# Données
*.csv
*.xlsx
data/raw/*

# Power BI
*.pbix.bak
*.pbit

# Python
__pycache__/
*.pyc
venv/
.env

# Logs
*.log
logs/

# Credentials
config/credentials.json
.env.local
