# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from Config.constants import *
from Database.database_user import *


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
        self.base_user = DataBaseUser()

    def step_1(self):  # > user
        """Category choice"""
        deco = " ***----------------------------------------------------------***"
        print(deco, '\n', "***Bienvenue dans le programme de substitution 'Petit Beurre'***", '\n', deco)
        try:
            for get in enumerate(CATEGORIES):
                print("*", get)
            user = input("Pour choisir une catego5rie, tapez le chiffre associé et appuyer sur ENTREE")
            print("vous avez choisis ", CATEGORIES[int(user)])
        except:
            print("Vous devez choisir une categorie dans la liste!")
            self.step_1()
        else:
            self.base_user.get_all_category()

    def step_2(self):
        pass

    def step_3(self):
        pass

    def step_4(self):
        pass

    def step_5(self):
        pass


def main():
    data_user = DataBaseUser()
    connect = data_user.connect_mysql()
    init = Main()
    step1 = init.step_1()


if __name__ == "__main__":
    main()

