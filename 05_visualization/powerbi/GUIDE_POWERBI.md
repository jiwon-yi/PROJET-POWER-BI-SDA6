# 📊 Guide Power BI - Projet Sorbonne

## 1. Import des Données
- Ouvrir Power BI Desktop
- Obtenir des données → Texte/CSV
- Naviguer vers: 01_data/processed/
- Importer les 5 tables CSV

## 2. Modèle de Données
Relations à créer:
- fact_ventes → dim_temps (id_temps)
- fact_ventes → dim_produit (id_produit)
- fact_ventes → dim_enseigne (id_enseigne)

## 3. Mesures DAX
\\\DAX
CA Total = SUM(fact_ventes[prix_total])
Nb Ventes = COUNTROWS(fact_ventes)
Panier Moyen = DIVIDE([CA Total], [Nb Ventes])
Taux Marge = DIVIDE(SUM(fact_ventes[marge_brute]), [CA Total])
\\\

## 4. Visualisations
- KPI Cards (CA, Nb ventes, Panier moyen)
- Graphique temporel (évolution mensuelle)
- Carte géographique (performance par ville)
- Top 10 produits (graphique en barres)
