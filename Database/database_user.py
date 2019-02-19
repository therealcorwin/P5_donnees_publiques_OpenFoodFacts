# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec
from Config.constants import *


class DataBaseUser:
    """
        This class has the responsibility to control the database of the user
    """

    def __init__(self):
        """ Just share the connection for MySQL """
        self.db = None

    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database(f"mysql+mysqlconnector://{USER}:{PASSWORD}@localhost/"
                               f"{DATABASE}?charset=utf8mb4")
        return self.db

    def get_databases(self):
        """ Control the database """
        databases = self.db.query("SHOW DATABASES;")
        for row in databases:
            print(row['Database'])
        return databases

    def get_tables(self):
        """ Control the tables """
        table = self.db.query("SHOW TABLES;")
        for tables in enumerate(table):
            print(tables)
        return table

    def get_all_products(self):
        """ Control in the tables """
        return self.db.query("""
                                SELECT * FROM demo.Products;
                             """,  fetchall=True).as_dict()

    def get_all_products_per_category(self, category):
        """ Control in the tables """
        cat = self.db.query("""
                                SELECT * FROM Products AS product
                                JOIN products_categories_summary_key AS pc ON pc.product_id = product.barre_code  
                                JOIN Categories_summary AS c ON pc.c_category_id = c.id							
                                WHERE c.c_category = :user;	
                            """, user=category, fetchall=True).as_dict()
        return cat

    def get_products_in_select_category(self, select_product):
        """ Get the products in choice the category """
        prod = self.db.query("""
                                SELECT product.name_product, product.grade, product.barre_code FROM Products AS product
                                WHERE name_product LIKE :user;
                             """, user=select_product, fetchall=True).as_dict()
        return [(i, p['name_product'], p['grade'], p['barre_code']) for i, p in enumerate(prod)]

    def choose_products_from_the_category(self, category, product):
        """ Offers a list of products with a holiest grade """
        prod = self.db.query("""
                             SELECT product.barre_code, product.name_product, product.grade FROM Products AS product
                             JOIN Products_categories_summary_key AS pcsk ON pcsk.product_id = product.barre_code
                             JOIN Categories_summary AS cs ON cs.id = pcsk.c_category_id
                             WHERE product.grade < :grade AND cs.c_category = :category;
                             """, grade=product['grade'], category=category, fetchall=True).as_dict()
        return prod

    def insert_favory(self):
        """ Inserts the selected product (s) into the favorites table in the database """
        self.db.query("""
                        INSERT INTO Favorites(
                        barre_code, name_product, grade, store, web_site)
                        VALUES (:...)
                        ON 
                      """, )


def main():
    """" Initialize the database user """

    databases = DataBaseUser()                                                                 # Load the database class
    connecting = databases.connect_mysql()                                                    # Load the MySQL connexion

    # Control the database

    # get_bases = databases.get_databases()                                                      # Get the database list
    # get_tables = databases.get_tables()                                                           # Get the table list
    # get_products = databases.get_all_products_per_category()                                     # Get the insert list
    # get_products = databases.get_product_in_category()                                           # Get the insert list


if __name__ == "__main__":
    main()
