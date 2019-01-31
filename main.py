# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec

from Config.constants import *
from Database.database_user import DataBaseUser


class Main:
    """
            - SCENARIO -

    - Affiche les databases disponnible
    - Selectionne la database
    - Affiche des tables disponnible
    - Selectionne une table
    - Affiche le contenu de la table selectionner

    - Affichage des résultats: requêtes, insertions,

    - Selection de la table Categories
    - Selection d'un produits dans la categories séléctionner
    - Comparer le produits séléctionner parmis la table Products grade '<'
    - Mettre les nouveaux substitue dans la table des favoris Substitute

    - * Pouvoir * savegarder la table des favoris
    - * Pouvoir * mettre à jour les requêtes
    - * Pouvoir * ré-insérer dans la table favoris les favoris sauvegarder [code barre/produit via requête barre_code]
    - * Pouvoir *
    """

    def __init__(self):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.database = DataBaseUser()
        self.db = self.database.connect_mysql()

    def step_1(self):  # > user
        """Category choice"""
        deco = "***----------------------------------------------------------***"
        print(deco, '\n', "***Bienvenue dans le programme de substitution 'Petit Beurre'***", '\n', deco)
        try:
            for get in enumerate(CATEGORIES):
                print("*", get)
            user = input("Pour choisir une categorie, tapez le chiffre associé et appuyer sur ENTREE")
            user = CATEGORIES[int(user)]
            print("vous avez choisis ", user.upper())
        except ValueError:
            print("Tapez le chiffre associé à une categorie dans la liste!")
            self.step_1()
        except IndexError:
            print("Vous devez choisir une categorie dans la liste!")
            self.step_1()
        else:
            self.database.get_all_products_per_category(str(user))

    def step_2(self):
        pass

    def step_3(self):
        pass

    def step_4(self):
        pass

    def step_5(self):
        pass


def main():
    init = Main()
    step1 = init.step_1()


if __name__ == "__main__":
    main()

