# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import tkinter as gui


class TkinterWidgets:

    def __init__(self):
        self.main_app = gui.Tk()                                                                       # Init the screen

    def tkinter_label(self):
        """ Label """
        welcome_label = gui.Label(self.main_app, text="Hello World")
        print(welcome_label.cget('text'))
        welcome_label.config(text='Bienvenue dans les premiers test.')                       # mis a jour de l'affichage

        """ Fonctionnement de mise à jour """
        welcome_label.pack()            # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message
        self.main_app.mainloop()                                                                        # Rafrichir loop
        return None

    def tkinter_message(self):
        """ Message avec '\n' """
        welcome_message = gui.Message(self.main_app, text="Hello World (message '\n')")
        # print(welcome_message.cget('text'))

        """ Fonctionnement de mise à jour """
        welcome_message.pack()        # Affichage en fonction du prefixe variable ici welcome_message ou welcome_message
        self.main_app.mainloop()                                                                        # Rafrichir loop
        return None

    def tkinter_entry(self):
        """ Demande de saisie (input()) """
        imput_selection = gui.Entry(self.main_app)         # show='*' password mode # exportselection=0 bloque selection

        """ Fonctionnement de mise à jour """
        imput_selection.pack()        # Affichage en fonction du prefixe variable ici imput_selection ou welcome_message
        self.main_app.mainloop()                                                                        # Rafrichir loop
        return None

    def tkinter_button(self):
        """ Button """
        button_selection = gui.Button(self.main_app, text='ok')

        """ Button + appel fonction """
        def hello():
            print('hello')
        button_selection_func = gui.Button(self.main_app, text='ok', command=hello)
        # button_selection.pack()       # Affichage en fonction du prefixe variable ici welcome_label ou welcome_message

        """ Fonctionnement de mise à jour """
        # Affichage en fonction du prefixe variable ici button_selection ou button_selection_func
        button_selection.pack()
        button_selection_func.pack()
        self.main_app.mainloop()                                                                        # Rafrichir loop
        return None


Tkinter_init = TkinterWidgets()
# Label = Tkinter_init.tkinter_label()
# Message = Tkinter_init.tkinter_message()
# Entry = Tkinter_init.tkinter_entry()
# Button = Tkinter_init.tkinter_button()


