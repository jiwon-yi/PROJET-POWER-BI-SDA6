-- =====================================
-- DATA WAREHOUSE SCHEMA
-- Projet BI Sorbonne
-- =====================================

-- Table de faits
CREATE TABLE fact_ventes (
    id_vente INTEGER PRIMARY KEY,
    id_temps INTEGER,
    id_produit INTEGER,
    id_enseigne INTEGER,
    quantite INTEGER,
    prix_total DECIMAL(10,2),
    marge_brute DECIMAL(10,2),
    FOREIGN KEY (id_temps) REFERENCES dim_temps(id_temps),
    FOREIGN KEY (id_produit) REFERENCES dim_produit(id_produit),
    FOREIGN KEY (id_enseigne) REFERENCES dim_enseigne(id_enseigne)
);

-- Dimension Temps
CREATE TABLE dim_temps (
    id_temps INTEGER PRIMARY KEY,
    date_complete DATE,
    annee INTEGER,
    mois INTEGER,
    jour INTEGER,
    trimestre INTEGER,
    nom_jour VARCHAR(20),
    nom_mois VARCHAR(20)
);

-- Dimension Produit  
CREATE TABLE dim_produit (
    id_produit INTEGER PRIMARY KEY,
    reference_produit VARCHAR(50),
    nom VARCHAR(100),
    categorie VARCHAR(50),
    prix DECIMAL(10,2),
    gamme_prix VARCHAR(20)
);

-- Dimension Enseigne
CREATE TABLE dim_enseigne (
    id_enseigne INTEGER PRIMARY KEY,
    enseigne VARCHAR(100),
    ville VARCHAR(100),
    adresse VARCHAR(255),
    region VARCHAR(50)
);
