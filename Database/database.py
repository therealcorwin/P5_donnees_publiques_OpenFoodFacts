# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec

from Config import constants as cons
from Api import search_cathegory as search


class DataBaseCreator:

    def __init__(self):
        pass

    def connect_mysql(self):
        """ Connecting in the database """
        connect = rec.Database("mysql+mysqlconnector://%s:%s@localhost/%s?charset=utf8mb4"
                               % (cons.USER, cons.PASSWORD, cons.DATABASE))
        return connect

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

    def insert_product(self, connect, ):
        response_api = search()
        insert_product = """
                        INSERT INTO Products_10k_Table (
                        col1,
                        col2,
                        col3,
                        col4,
                        col5) 
                        VALUES 
                        (:barre_code, :name, :grade, :Name, :website)
                         """
        connect.query(insert_product, response_api)
        return insert_product

    def insert_categories(self):
        response_api = search()
        insert_categories = """
                            INSERT INTO Categories ( 
                            col1,) 
                            VALUES 
                            (:format_categories)
                            """
        pass

    def insert_stores(self):
        response_api = search()
        insert_stores = """
                        INSERT INTO Stores (
                        col1) 
                        VALUES 
                        (:stores)
                        """
        pass


def main():
    """ Connecting in the database """
    databases = DataBaseCreator()
    connecting = databases.connect_mysql()

    """ Control the database """
    # show_base = databases.show_database(connecting)
    # show_table = databases.show_table(connecting)
    # choose = databases.choose_database(connecting)

    """ Create table """
    # categories = databases.create_table(connecting)

    """ Insert data """
    # insert_p = databases.insert_product(connecting)


if __name__ == "__main__":
    main()
