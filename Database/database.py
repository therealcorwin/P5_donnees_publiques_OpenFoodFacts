# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec

import Config.constants as cons
from Api.search_cathegory import ApiCollectingData


class DataBaseCreator:

    def __init__(self):
        self.db = None

    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database(f"mysql+mysqlconnector://{cons.USER}:{cons.PASSWORD}@localhost/"
                               f"{cons.DATABASE}?charset=utf8mb4")
        return self.db

    def get_databases(self):
        """ Control the database """
        databases = self.db.query("SHOW DATABASES;")

        for row in databases:
            print(row['Database'])
        return databases

    def get_tables(self):
        """"""
        tables = self.db.query("SHOW TABLES;")
        for table in tables:
            print(table)
        return tables

    def get_all_products(self):
        return self.db.query(
            """
                SELECT * FROM Products;
            """,
            fetchall=True
            ).as_dict()

    def use_database(self):
        """"""
        pass

    def create_table_product(self):
        """ Create table """
        self.db.query("""
                        CREATE TABLE Products (
                        Barre_code BIGINT PRIMARY KEY,
                        Name_product VARCHAR(255),
                        Grade CHAR(1),
                        Web_site VARCHAR(255))
                       """)

    def create_table_category(self):
        """"""
        self.db.query("""
                        CREATE TABLE Categories (
                        Categories VARCHAR(15));
                      """)

    def create_table_store(self):
        """"""
        self.db.query("""
                        CREATE TABLE Stores (
                        Stores VARCHAR(50));
                      """)

    def create_favorites_table(self):
        pass

    def create_tables(self):
        """ Execute the creating table """
        self.create_table_product()
        # self.create_table_category()
        # self.create_table_store()
        # self.create_favorites_table()
        return None

    def insert_product(self, id, name, grade, url, *args):
        self.db.query("""                        
                        INSERT INTO Products (
                        Barre_code,
                        Name_product,
                        Grade,
                        Web_site) 
                        VALUES 
                        (:id, :name, :grade, :url) 
                        ON DUPLICATE KEY UPDATE Barre_code = :id
                       """,
                      id=id, name=name, grade=grade, url=url)

    def insert_categories(self, categories):
        self.db.query("""
                        INSERT INTO Categories ( 
                        categories) 
                        VALUES 
                        (:categories);
                      """,
                      categories=categories)

    def insert_stores(self, stores):
        self.db.query(
            """
                INSERT INTO Stores ( 
                stores) 
                VALUES 
                :stores);
            """,
            stores=stores)

    def insert_rows_product(self, products):
        for product in products:
            self.insert_product(*product)


def main():
    """ Connecting in the database """
    # downloader = ApiCollectingData()                                                          # Load the API class
    # connect = downloader.bring_out()                                                          # Load the API connexion
    # final_products = tuple(downloader.format_final_response(connect))                         # Harvest OPFF's request

    # databases = DataBaseCreator()                                                          # Load the database class
    # connecting = databases.connect_mysql()                                                 # Load the MySQL connexion

    """ Control the database """
    # get_bases = databases.get_databases()                                                   # Get the database list
    # get_tables = databases.get_tables()                                                          # Get the table list
    # get_products = databases.get_all_products()   /***** # Get the insert list *****\
    # choose = databases.choose_database()

    """ Create table """
    # create_table = databases.create_tables()                                    # Creating Create the necessary tables

    """ Insert data """
    # databases.insert_rows_product(final_products)
    # insert_p = databases.insert_product()
    # insert_c = databases.insert_categories()
    # insert_s = databases.insert_stores


if __name__ == "__main__":
    main()
