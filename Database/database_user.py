# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec

from Config.constants import *


class DataBaseUser:
    """
    # Recherche Products -> sub_category
    # SELECT product.name_product FROM Products AS product
    # JOIN _product_category AS pc ON pc.product_id = product.barre_code
    # JOIN Categories AS c ON pc.category_id = c.id
    # WHERE c.category = 'conserves';
    """

    def __init__(self):
        """  """
        self.db = None

    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database(f"mysql+mysqlconnector://{USER}:{PASSWORD}@localhost/"
                               f"{NEW_DATABASE}?charset=utf8mb4")
        return self.db

    def get_databases(self):
        """ Control the database """
        databases = self.db.query("SHOW DATABASES;")
        for row in databases:
            print(row['Database'])
        return True

    def create_database(self, choose):
        creating = self.db("""
                            CREATE DATABASE :choose;
                           """, choose=choose)
        return True

    def use_database(self, use):
        using = self.db.query("USE :use;", use=use)
        return True

    def drop_database(self, drop):
        droping = self.db.query("DROP DATABASES :drop;", drop=drop)
        return True

    def get_tables(self):
        """ Control the tables """
        tables = self.db.query("SHOW TABLES;")
        for table in tables:
            print(table)
        return True

    def get_all_products(self):
        """ Control in the tables """
        return self.db.query("""
                                SELECT * FROM demo.Products;
                             """,  fetchall=True).as_dict()

    def get_all_products_per_category(self, user):
        """ Control in the tables """
        # user = "plats surgelés"
        cat = self.db.query(""" 
                                SELECT product.name_product FROM Products AS product      
                                JOIN products_categories_summary_key AS pc ON pc.product_id = product.barre_code  
                                JOIN Categories_summary AS c ON pc.c_category_id = c.id							
                                WHERE c.c_category = :user;	
                            """, user=user, fetchall=True).as_dict()
        for get_cat in enumerate(cat):
            print(get_cat)

    def get_product_in_category(self, user):
        print("In data user class")
        # user = "cons"
        prod = self.db.query("""
                                SELECT product.name_product FROM Products AS product  
                                WHERE name_product LIKE ':user;	
                             """, user=user,  fetchall=True).as_dict()
        for get_prod in enumerate(prod):
            print(get_prod)


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
    get_products = databases.get_all_products_per_category()                                     # Get the insert list
    # get_products = databases.get_product_in_category()                                     # Get the insert list


if __name__ == "__main__":
    main()
