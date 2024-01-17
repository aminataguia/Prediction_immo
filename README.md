Real Estate Price Prediction Project
Overview
Ce projet a pour objectif de prédire le prix au mètre carré des biens immobiliers en Île-de-France en utilisant différentes techniques de modélisation prédictive. Le projet est divisé en deux phases principales : la #phase1, qui se concentre sur la ville de Paris en 2022 avec deux variables explicatives (latitude et longitude), et la #phase2, qui élargit la portée à toute l'Île-de-France en 2022 en explorant davantage de variables explicatives.

## Que contient se Git 
README.md le fichier que vous lisez actuellement 
Analyse model.ipynb le fichier contenant l'integralité des exports python demandé 

### Le rendu 

#Phase1

Objectif
Prédire le prix au mètre carré des biens immobiliers à Paris en 2022 en utilisant la latitude et la longitude comme variables explicatives.

Étapes
Filtrage des données : Sélection des données uniquement pour Paris en 2022.
Création de nouvelles fonctionnalités : Ajout de la fonctionnalité 'prix_m2'.
Entraînement du modèle : Utilisation de différents modèles (Linear Regression, Decision Tree Regressor, RandomForest Regressor) avec GridSearchCV pour sélectionner le meilleur modèle.
Résultats
Le modèle RandomForest Regressor a été identifié comme le meilleur, avec des paramètres optimaux tels que 'max_depth', 'min_samples_leaf', et 'n_estimators'.
Les résultats sont évalués en utilisant la Mean Squared Error (RMSE) sur l'ensemble de test.

#Phase2

Objectif
Étendre la prédiction du prix au mètre carré à toute l'Île-de-France en 2022, en explorant davantage de variables explicatives.

Étapes
Filtrage des données : Utilisation de l'ensemble de données pour toute l'Île-de-France en 2022.
Exploration de nouvelles variables : Inclusion de variables supplémentaires dans le modèle.
Entraînement du modèle : Utilisation de GridSearchCV avec différents modèles pour sélectionner le meilleur modèle.
Résultats
Le modèle RandomForest Regressor a également été identifié comme le meilleur pour cette phase.
L'ensemble de test est utilisé pour évaluer les performances du modèle.
API FastAPI
Mise en œuvre de deux API distinctes pour les modèles de phase 1 et phase 2 respectivement. Les modèles sont exposés via des points de terminaison distincts.

Fichiers et Modèles
model_phase1.pkl : Modèle de phase 1 sauvegardé avec pickle.
model_phase2.pkl : Modèle de phase 2 sauvegardé avec pickle.

## Instructions d'utilisation
Installer les dépendances avec pip install -r requirements.txt.
Exécuter l'API FastAPI avec uvicorn api:app --reload.
Utiliser les points de terminaison respectifs pour prédire les prix au mètre carré pour les deux phases.
importer sur le meme chemin tableau.csv 






