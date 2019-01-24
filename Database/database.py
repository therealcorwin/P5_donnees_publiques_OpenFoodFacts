# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec

import Config.constants as cons
from Api.search_category import ApiCollectingData


class DataBaseCreator:

    def __init__(self):
        self.db = None

    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database(f"mysql+mysqlconnector://{cons.USER}:{cons.PASSWORD}@localhost/"
                               f"{cons.DATABASE}?charset=utf8mb4")
        return self.db

    def create_table_product(self):
        """ Create table """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Products (
                        barre_code BIGINT PRIMARY KEY,
                        name_product VARCHAR(150),
                        grade CHAR(1),
                        web_site VARCHAR(255));
                       """)

    def create_table_category(self):
        """"""
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Categories (
                        id BIGINT PRIMARY KEY AUTO_INCREMENT,
                        category VARCHAR(125),
                        sub_category VARCHAR(125)); 
                      """)

    def create_table_store(self):
        """"""
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Stores (
                        id BIGINT PRIMARY KEY AUTO_INCREMENT,
                        store VARCHAR(150) UNIQUE);
                    """)

    def create_table_subkey(self):
        """ Creating the index """
        self.db.query("""                                                           
                        CREATE TABLE IF NOT EXISTS _Product_store (
                        product_id INT REFERENCES Products(barre_code) ON DELETE CASCADE,
                        store_id INT REFERENCES Stores(id) ON DELETE CASCADE,
                        PRIMARY KEY (product_id, store_id));
                     """)                                                             # Index = id_products + id_ stores

        self.db.query("""
                        CREATE TABLE IF NOT EXISTS _Product_category ( 
                        product_id INT REFERENCES Products(barre_code) ON DELETE CASCADE,
                        category_id INT REFERENCES Category(id) ON DELETE CASCADE,
                        PRIMARY KEY (product_id, category_id));
                      """)                                                           # Index = id_products + id_category

        self.db.query("""
                        CREATE TABLE IF NOT EXISTS _Product_sub_category ( 
                        product_id INT REFERENCES Products(barre_code) ON DELETE CASCADE,
                        sub_category_id INT REFERENCES Category(id) ON DELETE CASCADE,
                        PRIMARY KEY (product_id, sub_category_id));
                      """)                                                       # Index = id_products + id_sub_category

    def create_favorites_table(self):
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Products (
                        barre_code BIGINT PRIMARY KEY,
                        name_product VARCHAR(150),
                        grade CHAR(1),
                        web_site VARCHAR(255));
                       """)

    def insert_product(self, id, name, grade, url, *args):
        """ Insert the product data in the table"""
        self.db.query("""                        
                        INSERT INTO Products (barre_code, name_product, grade, web_site) 
                        VALUES 
                        (:id, :name, :grade, :url) 
                        ON DUPLICATE KEY UPDATE barre_code = :id;
                      """,
                      id=id, name=name, grade=grade, url=url)

    def insert_category(self, id, name, grade, url, categories, sub_category, stores, *args):
        """ Insert the category list data in the table"""
        for category in categories:
                self.db.query("""
                            INSERT INTO Categories(category, sub_category) 
                            VALUES 
                            (:category, :sub_category)
                            ON DUPLICATE KEY UPDATE category=:category;                          
                              """,
                              category=category, sub_category=sub_category)

    def insert_stores(self, id, name, grade, url, categories, sub_category, stores, *args):
        """ Insert the store list data in the table"""
        for store in stores:
            self.db.query("""
                            INSERT INTO Stores(store)
                            VALUES (:store)
                            ON DUPLICATE KEY UPDATE store=:store;
                          """,
                          store=store)

    def insert_table_subkey(self, product_id, store_id):
        """ Creating the index """
        self.db.query("""                                                           
                        INSERT IN TO _Product_store(product_id, store_id),
                        VALUES (:product_id, :store_id);
                     """,
                      product_id=product_id, store_id=store_id)  # VALUES = :Products.id?, :Stores.store?

    #         self.db.query("""
    #                         INSERT IN TO _Product_category (
    #                         product_id INT REFERENCES Products(barre_code) ON DELETE CASCADE,
    #                         category_id INT REFERENCES Category(id) ON DELETE CASCADE,
    #                         PRIMARY KEY (product_id, category_id));
    #                       """)
    #
    #         self.db.query("""
    #                         INSERT IN TO _Product_sub_category (
    #                         product_id INT REFERENCES Products(barre_code) ON DELETE CASCADE,
    #                         sub_category_id INT REFERENCES Category(id) ON DELETE CASCADE,
    #                         PRIMARY KEY (product_id, sub_category_id));
    #                       """)

    def insert_favory(self):
        pass

    def create_tables(self):
        """ Execute the creating table """
        self.create_table_subkey()
        self.create_table_product()
        self.create_table_category()
        self.create_table_store()
        # self.create_favorites_table()
        return None

    def insert_rows(self, products):
        """ Completion the data row per row """
        for product in products:
            self.insert_table_subkey()
            self.insert_product(*product)
            self.insert_category(*product)
            self.insert_stores(*product)
        return None

def main():
    """ Connecting in the API """
    downloader = ApiCollectingData()                                                                # Load the API class
    connect = downloader.bring_out()                                                            # Load the API connexion
    final_products = downloader.format_final_response(connect)                                  # Harvest OPFF's request

    """ Connecting in the database """
    databases = DataBaseCreator()                                                              # Load the database class
    connecting = databases.connect_mysql()                                                    # Load the MySQL connexion

    """ Control the database """
    # get_bases = databases.get_databases()                                                      # Get the database list
    # get_tables = databases.get_tables()                                                           # Get the table list
    # get_products = databases.get_all_products()                                                  # Get the insert list

    # choose = databases.choose_database()

    """ Create table """
    create_table = databases.create_tables()                                             # Creating the necessary tables

    """ Insert data """
    insert_data = databases.insert_rows(final_products)


if __name__ == "__main__":
    main()

