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
        self.favorite = []


    def value_error(self, select_function, *args):
        """ Control the ValueError """
        try:
            return select_function(*args)
        except ValueError:
            print(" |*** /!\ Tapez le chiffre associé à votre choix dans la liste /!\ ***|")
            return self.value_error(select_function, *args)
        except IndexError:
            print(" |*** /!\ Tapez le chiffre associé à votre choix dans la liste /!\ ***|")
            return self.value_error(select_function, *args)

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
        print("FUNCTION 1 / main()")
        select_1 = self.value_error(self.step_1_action)
        print(" |*** vous avez choisis ***| :  ", select_1.capitalize())
        sleep(0.5)
        self.step_2(select_1)

    def step_1_action(self):
        for get in enumerate(CATEGORIES):
            print("*", get)
        user = input(" |*** Pour choisir une categorie, tapez le chiffre associé et appuyer sur ENTREE ***| ")
        return CATEGORIES[int(user)]

    def step_2_(self):
        pass

    def step_2_action(self):
        pass

    def step_2(self, select_1):
        """ Product choice """
        CACHE = self.database.get_all_products_per_category(str(select_1))
        print("FUNCTION 2 / main()")
        try:
            for select in CACHE:
                print("*", select)
            user = input(" |*** Pour choisir un produit, tapez le chiffre associé et appuyer sur ENTREE ***| ")
            select_2 = CACHE[int(user)]
            print(" |*** vous avez choisis ***| :  ", select_2[1].capitalize())
            sleep(0.5)
        except ValueError:
            print(" |*** /!\ Tapez le chiffre associé à un produit dans la liste /!\ ***|")
            sleep(0.5)
            self.step_2(select_1)
        except IndexError:
            print(" |*** /!\  Vous devez choisir un produit dans la liste /!\ ***|")
            sleep(0.5)
            self.step_2(select_1)
        else:
            self.step_3(select_2[1])

    def step_3(self, select_2):
        """ Substitute research"""
        print("FUNCTION 3  / main()")
        compare = self.database.get_product_in_category(str(select_2))
        for select in compare:
            print(select)
        menu = True
        user = input(" |*** Vous pouvez choisir un produits" '\n' 
                     "tapez le chiffre associé et appuyer sur ENTREE ***|")
        select_3 = compare[int(user)]
        print(" |*** vous avez choisis ***| :  ", select_3, '\n',
              "Souhaitez-vous sauvegarder ce produit?", '\n',)
        user = input("tapez 'O' ou 'N', valider avec ENTREE")
        if user == 'O':
            self.favorite.append(select_3)
            print("Ajout du produits:", select_3, "successful")
            self.step_3(select_2)
        if user == 'N':
            self.step_3(select_2)

        if user == 'G':
            print("Voici votre liste de favoris:", '\n', self.favorite)
        if user == 'M':
            self.home_menu()
        if user == 'Q':
            quit()


def main():

    init = Main()
    ini = init.home_menu()
    # step1 = init.step_3()
    # init.step_2_action()


if __name__ == "__main__":
    main()

