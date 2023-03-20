# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec

import constants as cons
import search_cathegory as search


class DataBaseCreator:

    def __init__(self):
        pass

    def connect_mysql(self):
        """ Connecting in the database """
        return rec.Database(
            f"mysql+mysqlconnector://{cons.USER}:{cons.PASSWORD}@localhost/{cons.DATABASE}?charset=utf8mb4"
        )

    def show_database(self, connect):
        """ Control the datanase """
        databases = connect.query("SHOW DATABASES")
        for row in databases:
            print(row['Database'])
        return databases

    def show_table(self, connect):
        """"""
        tables = connect.query("SHOW TABLES")
        for table in tables:
            print(table)
        return tables

    def use_database(self, connect):
        """"""
        pass

    def create_table_product(self, connect):
        """ Create table """
        connect.query("""CREATE TABLE Products_10k_Table (
                                Barre_code TINYINT(13) PRIMARY KEY,
                                Name_product VARCHAR(30),
                                Grade CHAR(1),
                                Web_site VARCHAR(255))""")
        return connect

    def create_table_categories(self, connect):
        """"""
        connect.query("""CREATE TABLE Categories (
                                Categories VARCHAR(15))""")
        return connect

    def create_table_stores(self, connect):
        """"""
        connect.query("""CREATE TABLE Stores (
                                Stores VARCHAR(50))""")
        return connect

    def create_favorites_table(self):
        pass

    def create_table(self, connecting):
        """ Execute the creating table """
        product = self.create_table_product(connecting)
        categories = self.create_table_categories(connecting)
        stores = self.create_table_stores(connecting)
        return product, categories, stores

    def insert_product(self, connect):
        response_api = search.convert_type_final()
        insert_product = """INSERT INTO Products_10k_Table (
                            Barre_code,
                            Name_product,
                            Grade,
                            name,
                            Web_site) 
                            VALUES (%s, %s, %s, %s, %s)"""
        connect.query(insert_product, response_api)
        return insert_product

    def insert_categories(self):
        insert_categories = """INSERT INTO Categories (
                               Categories)
                               VALUES (%s)"""

    def insert_stores(self):
        insert_Stores = """INSERT INTO Stores (
                          Stores) 
                          VALUES (%s)"""


def main():
    """ Connecting in the database """
    databases = DataBaseCreator()
    connecting = databases.connect_mysql()

    """ Control the database """
    # show = databases.show_table(connecting)
    # choose = databases.choose_database(connecting)

    """ Create table """
    # categories = databases.create_table(connecting)

    """ Insert data """
    insert_p = databases.insert_product(connecting)


if __name__ == "__main__":
    main()
