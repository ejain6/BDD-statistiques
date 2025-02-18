# Création d'une BDD et étude statistique

Dans le cadre de ma 1ère année de BUT informatique, nous <i>(en binôme)</i> avons réalisé un projet en lien avec les base de données et les statistiques. Ce projet se cécoupait en deux parties distinctes, que sont les suivantes : 

## Partie base de données
- Création d'un diagramme UML afin de modéliser la BDD
- [Création de la BDD](create_college2_db.sql) en suivant le diagramme et les retours des professeurs à son propos
- [Peulplement de la BDD](populate_college2_db.sql) <i>(une version corrigée, pas exactement celle créée précédemment)</i> par un import de données à mettre en relations venant de plusieurs fichiers CSV (comme [celui ci](fr-en-etablissements.csv))

## Partie etude statistique
- Recherche d'une problématique, qui fut la suivante : Est-il possible de prédire le nombre de filles qui passent le DNB par collège en fonction d’autres statistiques concernant le collège ?
- Import des et traitement données [en python](code.py) à partir d'un [fichier csv](colleges2_stats.csv)
- Création de diagrammes pour étudier les différentes variables statistiques
- Création d'une matrice de covariance et application de la régréssion linéaire multiple afin d'étudier la correlation des vatiables
- Rédaction d'un compte rendu pour synthétiser l'étude
