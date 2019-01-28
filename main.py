# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import Config.constants as cons


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
def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))

def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ?'
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break
"{} a dit : {}".format("PERMET DE REMPLIR", "LES PERENTHESES")
"{character} a dit : {quote}".format(character="Babar", quote="...bla bla")

    """

    def __init__(self):
        pass

    def step_1(self):
        list = print(cons.CATEGORIES)
        print("Bienvenue dans le programme de substitution 'Petit Beurre'", '\n',
              "Choisir une categories parmit la liste entre 0 et 12, puis appuyer sur ENTREE")
        user = input().isdigit()




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

