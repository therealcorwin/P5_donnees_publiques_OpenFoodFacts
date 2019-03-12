# Utilisez les données publiques de l'OpenFoodFacts

#### Start-up *Pur Beurre*

## Type de base de donnèes:
-MySQL 8.0

## Environnement virtuel:
-PipEnv

## Modèle physique de données: 
https://www.draw.io/#G1LCIp-60WcjpTEOj6mQDMlY9s1ntMLTEo

## Tableau Trello:
https://trello.com/b/SxIbE5ym/project5-openfoodfact

## Langue d'écriture, variables, commentaires, fonctions: 
-Anglais

## Installation [Python 3.7]
https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe

##### Téléchargement:

## Télécharger le fichier: 
https://github.com/Lyss74/P5_donnees_publiques_OpenFoodFacts/archive/master.zip

## Ou cloner le repository:
https://github.com/Lyss74/P5_donnees_publiques_OpenFoodFacts.git

## Packages nécessaire
    - records 
    - requests 
    - mysql-connector-python                

#### Installation:
Rendez-vous dans le répertoire du projet avec l'invité de commande

## Exemple de positionnement: 
    "C:Users\Admin\Desktop\P5_donnees_publiques_OpenFoodFacts"

## Installez pipenv: 
    pip install pipenv

une fois fait, après quelques minutes:

## Tapez: 
    pipenv install 
    [Cette commande installera tous les packages, en suivant le fichier Pipfile]

### Lancez un serveur SQL afin dutiliser la base de donnèes.

## La connexion à la base se fera sous ces identifiants: 
    DATABASE = 'PurBeurre'
    USER = 'OPFF' 
    PASSWORD = 'OCP5' 

### Exécuter le fichier main.py:

Rendez-vous dans le répertoire du projet avec l'invité de commande

## Exemple de positionnement: 
    "C:Users\Admin\Desktop\P5_donnees_publiques_OpenFoodFacts"

## Tapez: 
    pipenv run python main.py


# Fonctionnalités:

#### 1 - Quel aliment souhaitez-vous remplacer ? 

## Six categories proposer:
    -Le choix pour les catégories sont définies de façon à pouvoir proposer un grand nombre de produits référencé, 
     mais aussi de pouvoir recueillir un maximum de produits, plutôt qu'utiliser les catégories renseignèes par tous et pour tous.

## Sélectionnez l'aliment:
    -Après avoir choisi une catégorie, le programme saura vous proposer tous ces produits. 
    -Parmit la liste de produit proposer, le programme saura vous proposer une liste contenant des 
     produits de substitut, tous les grades supérieurs au grade "D" sera automatiquement rejetè. 
    -La derniére étapes qui proposent une liste de produit de substitut, vous proposeras également de 
     sauvegarder un ou plusieurs produits par rapport un produit substituè.

#### 2 - Retrouver mes aliments substitués.

##  Sauvegarde des produits:
    -Après avoir fait le choix de produit de substitut, il est possible de les sauvegarder dans 
     une base de données et de pouvoir les consulter à chaque moment.
