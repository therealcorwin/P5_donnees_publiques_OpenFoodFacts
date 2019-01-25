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


# # -*- PipEnv -*-
# # -*- coding: Utf-8 -*-
#
#
# import records as rec
# from Database.database import *
#
#
# class DataBaseUser:
#
#     def __init__(self):
#         self.db = None
#
#     """TEMP"""
#     def connect_mysql(self):
#         """ Connecting in the database """
#         self.db = rec.Database(f"mysql+mysqlconnector://{cons.USER}:{cons.PASSWORD}@localhost/"
#                                f"{cons.DATABASE}?charset=utf8mb4")
#         return self.db
#     """TEMP"""
#
#     def get_databases(self):
#         """ Control the database """
#         databases = self.db.query("SHOW DATABASES;")
#
#         for row in databases:
#             print(row['Database'])
#         return databases
#
#     def get_tables(self):
#         """"""
#         tables = self.db.query("SHOW TABLES;")
#         for table in tables:
#             print(table)
#         return tables
#
#     def get_all_products(self):
#         return self.db.query("""
#                                 SELECT * FROM demo.Products;
#                              """,
#                              fetchall=True).as_dict()
#
#     def use_database(self):
#         """"""
#         pass
#
#
# def main():
#
#     """ Connecting in the database """
#     user = DataBaseUser()
#     connecting = user.connect_mysql()                                                    # Load the MySQL connexion
#
#
#     """ Control the database """
#     # get_bases = user.get_databases()                                                      # Get the database list
#     # get_tables = user.get_tables()                                                           # Get the table list
#     # get_products = user.get_all_products()                                                  # Get the insert list
#
#     # choose = user.choose_database()
#
#     # choose = connecting.choose_database()
#
#
# if __name__ == "__main__":
#     main()