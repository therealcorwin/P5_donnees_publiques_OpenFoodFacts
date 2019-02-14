# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Config.constants import *
from Database.database_user import DataBaseUser


class Main:

    def __init__(self):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.favorites = []
        self.database = DataBaseUser()
        self.db = self.database.connect_mysql()

    def home_menu(self):
        print('\n', DECO, '\n', "***  Bonjour et bienvenue au °Substitute Factory° ***", '\n', DECO, '\n')
        print("tapez:", '\n',
              "*'R': pour effectuer une Recherche" '\n',
              "*'F': pour consulter les Favoris" '\n',
              '\n', DECO, '\n', SPACE_ADJUST, "*** °DATABASE CONTROL° ***", '\n', DECO, '\n',
              "*'G' pour Consulter les bases de donnèes disponnible", '\n',
              "*'C' pour Choisir une base de donnèes existante", '\n',
              "*'D' pour Dupprimer une base de donnèes existante", '\n',
              "*'N' pour crèer une Nouvelle base de donnèes", '\n',
              "*'Q' pour Quiter", '\n')
        user = input()
        key_list = ["R", "F", "G", "C", "D", "N", "Q"]
        if user not in key_list:
            print('\n', "IndexError - |*** /!\ Tapez le chiffre associé à votre choix dans la liste /!\ ***|", '\n')
            self.home_menu()
        else:
            if user == 'R':
                self.choice_category()
            elif user == 'F':
                    # self.database.get_favorites(user)
                self.home_menu()
            elif user == 'G':
                    # self.database.get_databases()
                self.home_menu()
            elif user == 'C':
                    # self.database.use_database(user)
                self.home_menu()
            elif user == 'D':
                    # self.database.drop_database(user)
                self.home_menu()
            elif user == 'N':
                    # self.database.create_database(user)
                self.home_menu()
                for base in enumerate(SEASON_DATABASES):
                    print(base)
            if user == 'Q':
                quit()

    def choice_category(self):
        """ Choice Category """
        select_category = self.value_error(self.choice_category_action)
        print('\n', "|*** vous avez choisis ***| : ", select_category.capitalize(), '\n')
        self.choice_product(select_category)

    def choice_category_action(self):
        """  """
        for i, get in enumerate(CATEGORIES):
            print("*", i+1, get)
        user = input('\n' " |*** Pour choisir une categorie, tapez le chiffre associé et appuyer sur ENTREE ***| " '\n')
        return CATEGORIES[int(user) - 1]

    def choice_product(self, select_category):
        """  """
        select_product = self.value_error(self.choice_product_action, select_category)
        print('\n', "|*** vous avez choisis ***| : ", select_product['name_product'].capitalize(), '\n')
        self.choice_substitute(select_category, select_product)

    def choice_product_action(self, select_category):
        """  """
        print("choice_product_action")
        products = self.database.get_all_products_per_category(str(select_category))
        for i, select in enumerate(products):
            print(f"* ({i+1}, {select['name_product']})")
        user = input('\n' " |*** Pour choisir un produit, tapez le chiffre associé et appuyer sur ENTREE ***| " '\n')
        if '0' in user:
            raise IndexError()
        return products[int(user) - 1]


    def choice_substitute(self, select_category, select_product):
        """  """
        select_substitute = self.value_error(self.choice_substitute_action, select_category, select_product)
        self.choose_favorite_final(select_category, select_product, select_substitute)

    def choice_substitute_action(self, select_category, select_product):
        substitutes = self.database.get_healthier_product_in_category(select_category, select_product)
        for i, select in enumerate(substitutes):
            print(f"* ({i + 1}, {select['barre_code']}, {select['name_product']}, {select['grade']})")
        user = input('\n' " Vous pouvez choisir un produits " '\n'
                     " tapez le chiffre associé et appuyer sur ENTREE " '\n'
                     " 'Q' pour Quitter " '\n'
                     " 'H' retour au Menu " '\n')
        if user.isdigit():
            select_substitute = substitutes[int(user)]
            print('\n', "Vous avez choisis: ", select_substitute, '\n', "Souhaitez-vous sauvegarder ce produit?", '\n')
            self.choose_favorite_final(select_category, select_product, select_substitute)
        else:
            key_list = ["C", "H", "Q"]
            if user not in key_list:
                self.choice_substitute_action(select_category, select_product)
            elif user == 'C':
                self.choice_substitute_action(select_category, select_product)
            elif user == 'H':
                self.home_menu()
            elif user == 'Q':
                quit()


    def choose_favorite_final(self, select_category, select_product, select_substitute):
        """  """
        user = input('\n' " tapez: " '\n' 
                     " 'O': pour Oui " '\n'
                     " 'N': pour Non " '\n' 
                     " 'C': pour Choisir un nouveau produit " '\n' 
                     " 'H': retour au Menu " '\n'
                     " 'Q': pour Quitter, valider avec ENTREE " '\n')
        if user.isdigit():
            print('\n', "IndexError - Veuillez faire un choix parmi la liste", '\n')
            self.choose_favorite_final(select_category, select_product, select_substitute)
        else:
            key_list = ["O", "N", "C", "H", "Q"]
            if user not in key_list:
                print('\n', "ValueError - |*** /!\ Tapez le chiffre associé à votre choix dans la liste /!\ ***|", '\n')
                self.choose_favorite_final(select_category, select_product, select_substitute)
            elif user == 'O':
                self.favorites.extend(select_substitute)
                print('\n', "Ajout du produits:", select_substitute, "successful", '\n')
                self.choice_substitute_action(select_category, select_product)
            elif user == 'N':
                self.choice_substitute_action(select_category, select_product)
            elif user == 'C':
                self.choice_substitute_action(select_category, select_product)
            elif user == 'H':
                self.home_menu()
            elif user == 'Q':
                quit()

    def value_error(self, select_function, *args):
        """ Control the ValueError """
        try:
            return select_function(*args)
        except ValueError:
            print('\n', "ValueError - |*** /!\ Tapez le chiffre associé à votre choix dans la liste /!\ ***|", '\n')
            return self.value_error(select_function, *args)
        except IndexError:
            print('\n', "IndexError - |*** /!\ Tapez le chiffre associé à votre choix dans la liste /!\ ***|", '\n')
            return self.value_error(select_function, *args)

def main():
    """  """
    init = Main()
    ini = init.home_menu()
    # step1 = init.choice_substitute()
    # init.choice_product_action()


if __name__ == "__main__":
    main()
