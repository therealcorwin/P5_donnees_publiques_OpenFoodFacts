###### Utilisez les données publiques de l'OpenFoodFacts

#### Start-up *Pur Beurre*

# Installation [Python 3.7]
https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe

### Téléchargement:

# Télécharger le fichier: 
https://github.com/Lyss74/P5_donnees_publiques_OpenFoodFacts/archive/master.zip

# Ou cloner le repository:
https://github.com/Lyss74/P5_donnees_publiques_OpenFoodFacts.git

## Installation:
Rendez-vous dans le répertoire du projet avec l'invité de commande

# exemple de positionnement: 
    "C:UsersAdminDesktopP5_donnees_publiques_OpenFoodFacts"

# Installè pipenv: 
    pip install pipenv

une fois fait, après quelques minutes:

# tapez: 
    pipenv install requests 
  [L'un des packages necessaires au fonctionnement]

## Lancez un serveur SQL afin dutiliser la base de donnèes.

# La connexion à la base se fera sous ces identifiant: 
    DATABASE = ' PurBeurre'
    USER = 'OPFF' 
    PASSWORD = 'OCP5' 

## Exécuter le fichier main.py:

Rendez-vous dans le répertoire du projet avec l'invité de commande

# exemple de positionnement: 
    "C:UsersAdminDesktopP5_donnees_publiques_OpenFoodFacts"

# Ensuite, taper 
    pipenv run python main.py

#### fonctionnalités:

## ...## ...

# # # # # # # # # # #

# Vous respecterez les bonnes pratiques de la PEP 8, PEP 20 et développerez dans un environnement virtuel

# Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions.