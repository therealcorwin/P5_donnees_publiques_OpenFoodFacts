# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from time import sleep

from Config.constants import *
from Database.database_user import DataBaseUser


class Main:

    def __init__(self):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.database = DataBaseUser()
        self.db = self.database.connect_mysql()

    def home_menu(self):
        print('\n', DECO, '\n', "***  Bonjour et bienvenue au °Substitute Factory° ***", '\n', DECO)
        print("Apppyer sur :", '\n', "'R' pour effectuer une recherche", '\n',
              # "'G' pour consulter les bases de donnèes disponnible", '\n',
              # "'C' pour choisir une base de donnèes existante", '\n',
              # "'D' pour supprimer une base de donnèes existante", '\n',
              # "'N' pour crèer une nouvelle base de donnèes", '\n',
              "'Q' pour quiter ", '\n')
        user = input("")
        if user == 'R':
            self.step_1()
        #         if user == 'G':
        #             self.database.get_databases()
        #             user = input("")
        #             self.home_menu()
        #         if user == 'C':
        #             self.choose_database()
        #         if user == 'D':
        #             user = input("")
        #             self.home_menu()
        #         if user == 'N':
        #             user = input("")
        #             for base in enumerate(SEASON_DATABASES):
        #                 print(base)
        #             self.home_menu()
        if user == 'Q':
            quit()

    def step_1(self):
        """ Choice Category """
        try:
            for get in enumerate(CATEGORIES):
                print("*", get)
            user = input(" |*** Pour choisir une categorie, tapez le chiffre associé et appuyer sur ENTREE ***| ")
            select_1 = CATEGORIES[int(user)]
            print(" |*** vous avez choisis ***| :  ", select_1.capitalize())
            sleep(1.5)
        except ValueError:
            print(" |*** /!\ Tapez le chiffre associé à une categorie dans la liste /!\ ***|")
            self.step_1()
        except IndexError:
            print(" |*** /!\  Vous devez choisir une categorie dans la liste /!\ ***|")
            self.step_1()
        else:
            self.step_2(select_1)

    def step_2(self, select_1):
        """Product choice"""
        self.database.get_all_products_per_category(str(select_1))
        try:
            print("MAIN() - STEP_2/SELECT_2")
            for select in enumerate(CACHE):
                print("*", select)
            user = input(" |*** Pour choisir un produit, tapez le chiffre associé et appuyer sur ENTREE ***| ")
            select_2 = CACHE[int(user)]
            print(" |*** vous avez choisis ***| :  ", select_2.capitalize())
            sleep(1.5)
        except ValueError:
            print(" |*** /!\ Tapez le chiffre associé à un produit dans la liste /!\ ***|")
            sleep(1)
            self.step_2(select_1=None)
        except IndexError:
            print(" |*** /!\  Vous devez choisir un produit dans la liste /!\ ***|")
            sleep(1)
            self.step_2(select_1=None)
        else:
            self.step_3(select_2)

    def step_3(self, select_2):
        self.database.get_product_in_category(str(select_2))
        pass

def main():
    init = Main()
    ini = init.home_menu()
    # step1 = init.step_1()


if __name__ == "__main__":
    main()

