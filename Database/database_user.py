# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


class DataBaseUser:
    """
        This class has the responsibility to control the database of the user
    """

    def __init__(self, db):
        """ Just share the connection for MySQL """
        self.db = db

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
                                SELECT * FROM PurBeurre.Products;
                             """,  fetchall=True).as_dict()

    def get_all_products_per_category(self, category):
        """ Control in the tables """
        print("I.ALL PRODUCT PER CATEGORY")
        cat = self.db.query("""
                                SELECT c.c_category, product.barcode, product.name_product, 
                                product.grade, product.web_site FROM Products AS product
                                JOIN products_categories_summary_key AS pc ON pc.product_id = product.barcode  
                                JOIN Categories_summary AS c ON pc.c_category_id = c.id    
                                WHERE c.c_category = :user
                                AND product.grade IN ('b', 'c', 'd', 'e')
                                GROUP BY product.barcode;
                            """,  user=category, fetchall=True).as_dict()
        return cat

    def choose_products_from_the_category(self, category, product):
        """ Offers a list of products with a holiest grade """
        print("III.PRODUCT IN CATEGORY")

        prod = self.db.query("""
                                SELECT c_category, product.barcode, product.name_product, 
                                product.grade, product.web_site FROM Products AS product
                                
                                jOIN Products_categories_summary_key AS pcsk ON pcsk.product_id = product.barcode
                                JOIN Categories_summary AS cs ON cs.id = pcsk.c_category_id
                                 
                                WHERE product.grade < :grade AND cs.c_category = :category
                                GROUP BY product.barcode
                                ;
                                
                             """, grade=product['grade'], category=category, fetchall=True).as_dict()
        return prod


    def insert_favory(self):
        """ Inserts the selected product (s) into the favorites table in the database """
        self.db.query("""
                        INSERT INTO Favorites(
                        barcode, name_product, grade, store, web_site)
                        VALUES (:...)
                        ON 
                      """,)


    #     def get_products_in_select_category(self, select_product):
    #         print("II.PRODUCT IN CATEGORY")
    #         """ Get the products in choice the category """
    #         prod = self.db.query("""
    #                                 SELECT product.name_product, product.grade, product.barcode FROM Products AS product
    #                                 WHERE name_product LIKE :user;
    #                              """, user=select_product, fetchall=True).as_dict()
    #         return [(i, p['name_product'], p['grade'], p['barcode']) for i, p in enumerate(prod)]
