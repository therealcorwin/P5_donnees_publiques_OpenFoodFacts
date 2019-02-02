# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


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
    - * Pouvoir * """

    def __init__(self):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.database = DataBaseUser()
        self.db = self.database.connect_mysql()

    def home_menu(self):
        print('\n', DECO, '\n', "***  Bonjour et bienvenue au °Substitute Factory° ***", '\n', DECO)
        print("Apppyer sur :", '\n', "'G' pour consulter les bases de donnèes disponnible", '\n',
              "'C' pour choisir une bases de donnèes existantes", '\n',
              "'D' pour supprimer une bases de donnèes", '\n',
              "'N' pour crèer une nouvelle bases de donnèes", '\n',
              "'Q' pour quiter ", '\n',)
        user = input("")
        if user == 'G':
            self.database.get_databases()
            self.home_menu()
        if user == 'C':
            self.database.get_databases()
            self.database.use_database(user)
            self.home_menu()
        if user == 'D':
            self.database.drop_database(user)
            self.home_menu()
        if user == 'N':
            for base in enumerate(SEASON_DATABASES):
                print(base)
            self.database.create_database(user)
            self.home_menu()
        if user == 'Q':
            quit()

    def choose_database(self):  # get and choose
        pass

    def create_database(self):  # get, choose, create
        pass

    def drop_database(self):  # get, drop
        pass

    def step_1(self):  # > user
        """Category choice"""
        print('\n', DECO, '\n', "*Bienvenue au programme de substitution 'Petit Beurre'*", '\n', DECO)
        try:
            for get in enumerate(CATEGORIES):
                print("*", get)
            user = input("Pour choisir une categorie, tapez le chiffre associé et appuyer sur ENTREE")
            user = CATEGORIES[int(user)]
            print("vous avez choisis ", user.capitalize())
        except ValueError:
            print("Tapez le chiffre associé à une categorie dans la liste!")
            self.step_1()
        except IndexError:
            print("Vous devez choisir une categorie dans la liste!")
            self.step_1()
        else:
            self.step_2()
            self.database.get_all_products_per_category(str(user))

    def step_2(self ):  # > user
        """Product choice"""
        deco = "***----------------------------------------------------------***"
        print('\n', DECO, '\n', " *** Vous pouvez choisir un produit dans la liste *** ", '\n', DECO)
        # -> locate the list choose of 'product in categories'

        # self.database.get_product_in_category()
        #         try:
        #
        #             user = input("Pour choisir un produit, tapez le chiffre associé et appuyer sur ENTREE")
        #             user = self.database.get_product_in_category(user)
        #             print("vous avez choisis ", str(user))
        #
        #         except ValueError:
        #             print("Tapez le chiffre associé à un produit dans la liste!")
        #             self.step_2()
        #         except IndexError:
        #             print("Vous devez choisir un produit dans la liste!")
        #             self.step_2()
        #         else:            pass  # self.database.get_product_in_category(str(user))

    def save_favorite_substitute_product(self):  # save in database favorites table and save barre_code in csv file
        pass

    def update_database(self):  # drop existing table, lunch update api request,
        pass                    # load and request the barre_code in csv file


def main():
    init = Main()
    step1 = init.step_1()
    # init.home_menu()


if __name__ == "__main__":
    main()

