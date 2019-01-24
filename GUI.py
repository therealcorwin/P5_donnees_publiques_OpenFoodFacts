# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import tkinter as gui


class GraphicUserInterface:

    def windgets(self):
        main_app = gui.Tk()                                                                            # Init the screen

        """ Label """
        welcome_label = gui.Label(main_app, text="Bienvenue au programme de substitution")
        # print(welcome_label.cget('text'))
        welcome_label.config(text='Bienvenue dans les premiers test.')                       # mis a jour de l'affichage
        # welcome_label.pack()          # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message

        """ Message avec '\n' """
        welcome_message = gui.Message(main_app, text="Bienvenue au programme de substitution (message '\n')")
        # print(welcome_message.cget('text'))
        # welcome_message.pack()        # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message

        """ Demande de saisie (input()) """
        imput_selection = gui.Entry(main_app)              # show='*' password mode # exportselection=0 bloque selection
        # imput_selection.pack()        # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message

        """ Button """
        button_selection = gui.Button(main_app, text='ok')
        # button_selection.pack()       # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message

        """ Button + appel fonction """
        def hello():
            print('hello')
        button_selection_func = gui.Button(main_app, text='ok', command=hello)
        # button_selection.pack()       # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message

        """ Fonctionnement de mise à jour """
        button_selection_func.pack()    # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message
        main_app.mainloop()                                                                             # Rafrichir loop
        return True

    def message_test(self):
        main_app = gui.Tk()                                                                            # Init the screen
        welcome_label = gui.Label(main_app, text="Bienvenue au programme de substitution")
        welcome_label.pack()


        """"""
        main_app.mainloop()                                                                             # Rafrichir loop
        return True


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


tkinter_test = GraphicUserInterface()
message = tkinter_test.message_test()


