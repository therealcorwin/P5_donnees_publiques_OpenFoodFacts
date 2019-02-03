# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

# C:\Users\Admin\GoogleDrive\DATA_OPEN_PROG\OPENCLASSROOMS\MyProjectOC\PROJET_05\MySQL\bin

from Config.constants import *
from Database.database_user import DataBaseUser
from Api.search_category import ApiCollectingData


class DataBaseCreator:
    """
    """

    def __init__(self):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.database = DataBaseUser()
        self.db = self.database.connect_mysql()

    def create_table_product(self):
        """ Create table """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Products (
                        barre_code BIGINT UNIQUE PRIMARY KEY,
                        name_product VARCHAR(150),
                        grade CHAR(1),
                        web_site VARCHAR(255));
                       """)
        return True

    def create_table_category(self):
        """  """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Categories (
                        id BIGINT PRIMARY KEY AUTO_INCREMENT,
                        category VARCHAR(125) UNIQUE);
                      """)

        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Categories_summary (
                        id BIGINT PRIMARY KEY AUTO_INCREMENT,
                        c_category VARCHAR(125) UNIQUE); 
                      """)
        return True

    def create_table_store(self):
        """  """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Stores (
                        id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                        store VARCHAR(150) UNIQUE);
                      """)
        return True

    def create_table_subkey(self):
        """ Creating the index """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Products_categories_key ( 
                        id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
                        product_id BIGINT REFERENCES Products(barre_code),
                        category_id MEDIUMINT REFERENCES Category(id));
                       """)

        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Products_categories_summary_key (
                        id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
                        product_id BIGINT REFERENCES Products(barre_code),
                        c_category_id MEDIUMINT REFERENCES Categories_summary(id));
                      """)

        self.db.query("""                                                           
                        CREATE TABLE IF NOT EXISTS Products_stores (
                        id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
                        product_id BIGINT REFERENCES Products(barre_code),
                        store_id MEDIUMINT REFERENCES Stores(id));               
                      """)
        return True

    def create_favorites_table(self):
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS Products (
                        barre_code BIGINT PRIMARY KEY,
                        name_product VARCHAR(150),
                        grade CHAR(1),
                        web_site VARCHAR(255));
                       """)
        return True

    def insert_product(self, id, name, grade, url, *args):
        """ Insert the product data in the table"""
        self.db.query("""                        
                        INSERT INTO Products (barre_code, name_product, grade, web_site) 
                        VALUES 
                        (:id, :name, :grade, :url) 
                        ON DUPLICATE KEY UPDATE barre_code=:id;
                      """, id=id, name=name, grade=grade, url=url)
        return True

    def insert_category(self, id, name, grade, url, categories, sub_category, stores, *args):
        """ Insert the category list data in the table"""
        for category in categories:
            self.db.query("""
                            INSERT INTO Categories(category) 
                            VALUES 
                            (:category)
                            ON DUPLICATE KEY UPDATE category=:category;                          
                          """, category=category)

            self.db.query("""
                            INSERT INTO Categories_summary(c_category) 
                            VALUES 
                            (:c_category)
                            ON DUPLICATE KEY UPDATE c_category=:c_category;                          
                          """, c_category=sub_category)

            self.db.query("""
                            INSERT INTO Products_categories_key (product_id, category_id)
                            VALUES (:barre_code,
                            (SELECT id FROM Categories WHERE category=:category_id));
                          """, barre_code=id, category_id=category)

            self.db.query("""
                            INSERT INTO Products_categories_summary_key (product_id, c_category_id)
                            VALUES (:barre_code,
                            (SELECT id FROM Categories_summary WHERE c_category=:category_id));
                          """, barre_code=id, category_id=sub_category)
            return True

    def insert_stores(self, id, name, grade, url, categories, sub_category, stores, *args):
        """ Insert the store list data in the table"""
        for store in stores:
            self.db.query("""
                            INSERT INTO Stores(store)
                            VALUES (:store)
                            ON DUPLICATE KEY UPDATE store=:store;
                          """, store=store)

            self.db.query("""
                            INSERT INTO Products_stores (product_id, store_id)
                            VALUES (:barre_code,
                            (SELECT id FROM Stores WHERE store=:store_id));
                          """, barre_code=id, store_id=store)
        return True

    def insert_favory(self):
        pass

    def create_tables(self):
        """ Execute the creating table """
        self.create_table_product()
        self.create_table_category()
        self.create_table_store()
        self.create_table_subkey()
        print('\n', DECO, '\n', "    **** Creating table success ****    ")
        # self.create_favorites_table()
        return True

    def insert_rows(self, products):
        """ Completion the data row per row """
        for product in products:
            self.insert_product(*product)
            self.insert_category(*product)
            self.insert_stores(*product)
        print('\n', DECO, '\n', "    **** Insert data, success *****     ", '\n', DECO, '\n', )
        return True


def main():
    """ Init the class """
    creating = DataBaseCreator()

    """ Connecting in the API """
    downloader = ApiCollectingData()                                                                # Load the API class
    connect = downloader.bring_out()                                                            # Load the API connexion
    final_products = downloader.format_final_response(connect)                                  # Harvest OPFF's request

    """ Create table """
    create_table = creating.create_tables()                                              # Creating the necessary tables

    """ Insert data """
    insert_data = creating.insert_rows(final_products)


if __name__ == "__main__":
    main()
