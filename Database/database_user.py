# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec
from Config.constants import *


class DataBaseUser:

    def __init__(self):
        """  """
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

    def create_database(self, choose):
        self.db("""
                    CREATE DATABASE :choose;
                """, choose=choose)
        return True

    def use_database(self, use):
        using = self.db.query("USE :use;", use=use)

    def drop_database(self, drop):
        """ Drop the database """
        self.db.query("DROP DATABASES :drop;", drop=drop)
        return True

    def get_tables(self):
        """ Control the tables """
        table = self.db.query("SHOW TABLES;")

        for tables in enumerate(table):
            print(tables)
        return True

    def get_all_products(self):
        """ Control in the tables """
        return self.db.query("""
                                SELECT * FROM demo.Products;
                             """,  fetchall=True).as_dict()

    def get_all_products_per_category(self, select_1):
        """ Control in the tables """
        print("FUNCTION 1  / DatabaseUser()")
        cat = self.db.query(""" 
                                SELECT product.name_product, product.grade, product.barre_code FROM Products AS product      
                                JOIN products_categories_summary_key AS pc ON pc.product_id = product.barre_code  
                                JOIN Categories_summary AS c ON pc.c_category_id = c.id							
                                WHERE c.c_category = :user;	
                            """, user=select_1, fetchall=True).as_dict()

        products = [p['name_product'] for p in cat]
        for i, product in enumerate(products):
            CACHE.append(product)

    def get_product_in_category(self, select_2):
        print("FUNCTION 2  / DatabaseUser()")

        prod = self.db.query("""
                              SELECT product.name_product, product.grade FROM Products AS product
                              WHERE name_product LIKE :user;
                             """, user=select_2,  fetchall=True).as_dict()

        for get_prod in enumerate(prod):
            print(get_prod)

#                                  WHERE ta_colonne REGEXP 'Tomates|pelées|entières|au|jus'

#                                  SELECT product.name_product, product.grade FROM Products AS product
#                                  WHERE name_product REGEXP :user;

#                                  SELECT product.name_product, product.grade FROM Products AS product
#                                  WHERE name_product LIKE :user;
#                                  WHERE ta_colonne REGEXP 'Tomates|pelées|entières|au|jus'

#                                  SELECT product.name_product, product.grade FROM Products AS product
#                                  WHERE name_product REGEXP :user;

#                                  SELECT product.name_product, product.grade FROM Products AS product
#                                  WHERE name_product LIKE :user;

# OR et AND
# ( || et && )
#         prod = [p['name_product'] for p in cat]
#         grade = [g['grade'] for g in cat]
#         id = [c['barre_code'] for c in cat]
#         products = (prod, grade, id)
#         for product in products:
#             CACHE.append(product)

def main():
    # Init the class, and Connecting in the database
    databases = DataBaseUser()                                                                 # Load the database class
    connecting = databases.connect_mysql()                                                    # Load the MySQL connexion

    # Control the database
    # c_data = databases.create_database(SEASON_DATABASES['Winter'])
    # use = databases.use_database(SEASON_DATABASES['Winter'])
    # drop = databases.drop_database(SEASON_DATABASES['Winter'])

    # get_bases = databases.get_databases()                                                      # Get the database list
    # get_tables = databases.get_tables()                                                           # Get the table list
    # get_products = databases.get_all_products_per_category()                                     # Get the insert list
    # get_products = databases.get_product_in_category()                                           # Get the insert list


if __name__ == "__main__":
    main()
