# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec

from Config import constants as conf
from Database.database_user import DataBaseUser


class Main:
    """
        This class has the responsibility of directing the user
    """

    def __init__(self):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.db = self.connect_mysql()
        self.database = DataBaseUser(self.db)

    def home_menu(self):
        """ This function allows to direct the user """
        print('\n', conf.DECO, '\n',
              "***  Bonjour et bienvenue au ° Substitute Factory ° ***",
              '\n', conf.DECO, '\n')
        print("Tapez:", '\n',
              " |-'1': Quel aliment souhaitez-vous remplacer ?" '\n',
              " |-'2': Retrouver mes aliments substitués" '\n',
              " |-'Q': Pour quitter", '\n')
        user = input()
        key_list = ["1", "2", "Q"]
        if user not in key_list:
            print('\n', conf.SPACE_ADJUST,  conf.INDEX_ERROR, '\n')
            self.home_menu()
        else:
            if user == '1':
                self.choice_category()
            elif user == '2':
                self.product_store()

            if user == 'Q':
                self.exit()

    def choice_category(self):
        """ Choice Category """
        category = \
            self.value_error(self.choice_category_action)
        print('\n', conf.SPACE_ADJUST,
              "|*** vous avez choisis ***| : ",
              category.capitalize(), '\n')
        self.choice_product(category)

    def choice_category_action(self):
        """
        This function is linked with
        choice_category to control the user input
        """
        for i, get in enumerate(conf.CATEGORIES):
            print("*", i+1, get)
        user = input('\n' 
                     " |*** Pour choisir une catégorie, "
                     "tapez le chiffre associé et appuyer sur ENTREE ***| "
                     '\n')
        return conf.CATEGORIES[int(user)-1]

    def choice_product(self, category):
        """ Choice product """
        product = \
            self.value_error(self.choice_product_action, category)
        print('\n', conf.SPACE_ADJUST,
              "|*** Vous avez choisis ***| : ",
              product['name_product'].capitalize(), '\n')
        self.choice_substitute(category, product)

    def choice_product_action(self, category):
        """
        This function is linked with
        choice_product to control the user input
        """
        products = \
            self.database.get_all_products_per_category(str(category))
        for i, select in enumerate(products):
            print(f"* ({i+1}, {select['name_product']})")
        user = input('\n' 
                     " |*** Pour choisir un produit, "
                     "tapez le chiffre associé et appuyer sur ENTREE ***| "
                     '\n')
        return products[int(user) - 1]

    def choice_substitute(self, category, product):
        """ Choice the substitute """
        substitute = \
            self.value_error(self.choice_substitute_action, category, product)
        self.choose_favorite_final(category, product, substitute)

    def choice_substitute_action(self, category, product):
        """
        This function is linked with
        choice_substitute to control the user input
        """
        substitutes = \
            self.database.choose_products_from_the_category(category, product)
        print("     "
              "| Code barre |,    | Nom Produits |,    "
              "| NutriScore |", '\n')
        for i, select in enumerate(substitutes):
            print(f"* ({i+1}, {select['barcode']}, "
                  f"{select['name_product']}, {select['grade']})")
        user = input('\n' " | Vous pouvez choisir un produits" '\n'
                     " |-tapez le chiffre associé et appuyer sur ENTREE" '\n'
                     " |-'Q' pour quitter" '\n'
                     " |-'H' retour au Menu" '\n')
        if user.isdigit():
            substitute = substitutes[int(user)-1]
            print('\n', conf.SPACE_ADJUST,
                  "|*** Vous avez choisis ***|",
                  substitute['name_product']+",",
                  "de grade : ", substitute['grade'], '\n'*2,
                  "|*** Souhaitez-vous sauvegarder ce produit ? ***|", '\n')
            self.choose_favorite_final(category, product, substitute)
        else:
            key_list = ["C", "H", "Q"]
            if user not in key_list:
                self.choice_substitute_action(category, product)
            elif user == 'C':
                self.choice_substitute_action(category, product)
            elif user == 'H':
                self.home_menu()
            if user == 'Q':
                self.exit()
        return substitutes[int(user)]

    def choose_favorite_final(self, category, product, substitute):
        """ Choose de products final substitute and save in the data base """
        user = input(" | tapez:" '\n' 
                     " |-'O': pour oui" '\n'
                     " |-'N': pour non" '\n' 
                     " |-'C': pour choisir un nouveau produit" '\n' 
                     " |-'H': retour au Menu" '\n'
                     " |-'Q': pour quitter, valider avec ENTREE" '\n')
        if user.isdigit():
            print('\n', conf.SPACE_ADJUST,  conf.INDEX_ERROR, '\n')
            self.choose_favorite_final(category, product, substitute)
        else:
            key_list = ["O", "N", "C", "H", "Q"]
            if user not in key_list:
                print('\n', conf.SPACE_ADJUST, conf.VALUE_ERROR, '\n')
                self.choose_favorite_final(category, product, substitute)
            elif user == 'O':
                id_product = product['barcode']
                id_substitute = substitute['barcode']
                self.database.add_into_favorites(id_product, id_substitute)
                print(conf.SPACE_ADJUST,
                      " |*** Ajout du produit ***| ",
                      '\n'*2, conf.SPACE_ADJUST,
                      "|-Nom:", substitute['name_product'],
                      '\n', conf.SPACE_ADJUST,
                      "|-Code barre:", id_substitute,
                      '\n', conf.SPACE_ADJUST,
                      "|-Grade:", substitute['grade'],
                      '\n', conf.SPACE_ADJUST,
                      "|-Site internet:", substitute['web_site'],
                      '\n'*2, conf.SPACE_ADJUST,
                      "|*** Successful ***|", '\n'*2,
                      "|-Contenu du casier favoris: ",
                      '\n'*2,  '\n'*2)
                self.choice_substitute(category, product)
            elif user == 'N':
                print("|Contenu du casier favoris: ",
                      '\n'*2,  '\n'*2)
                self.choice_substitute(category, product)
            elif user == 'C':
                self.choice_substitute(category, product)
            elif user == 'H':
                # self.favorites.pop(key)
                self.home_menu()
            elif user == 'Q':
                self.exit()

    def product_store(self):
        products = self.database.get_favorite_table()
        if len(products) > 0:
            for i, select in enumerate(products):
                print(f"* ({i+1}, {select['name_product']}, {select['stores']})")
            # input("H" : Pour retourner au menu)
            # self.home_menu()
        else:
            print("Il n'y as aucun produits")
            self.home_menu()

    def value_error(self, function, *args):
        """ This function will control the user's input """
        try:
            return function(*args)
        except ValueError:
            print('\n', conf.SPACE_ADJUST, conf.VALUE_ERROR, '\n')
            return self.value_error(function, *args)
        except IndexError:
            print('\n', conf.SPACE_ADJUST,  conf.INDEX_ERROR, '\n')
            return self.value_error(function, *args)

    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database(
                  f"mysql+mysqlconnector://{conf.USER}:{conf.PASSWORD}@localhost/"
                  f"{conf.DATABASE}?charset=utf8mb4")
        return self.db

    def exit(self):
        print('\n', conf.DECO, '\n', conf.SPACE_ADJUST,
              "*** ° Au revoir et à bientot ° ***",
              '\n', conf.DECO, '\n')
        quit()


def main():
    """ Initialize the main class """

    init = Main()
    init.home_menu()


if __name__ == "__main__":
    main()
