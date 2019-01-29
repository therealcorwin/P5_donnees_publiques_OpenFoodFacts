# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

# C:\Users\Admin\GoogleDrive\DATA_OPEN_PROG\OPENCLASSROOMS\MyProjectOC\PROJET_05\MySQL\bin
# DROP TABLE `demo`.`_product_category`, `demo`.`_product_store`, `demo`.`_product_sub_category`, `demo`.`categories`, `demo`.`products`, `demo`.`stores`;


from Database.database_user import DataBaseUser
from Api.search_category import ApiCollectingData


class DataBaseCreator:
    """
    """

    def __init__(self, db):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.db = db

    def create_table_product(self):
        """ Create table """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS products (
                        barre_code BIGINT PRIMARY KEY,
                        name_product VARCHAR(150),
                        grade CHAR(1),
                        web_site VARCHAR(255));
                       """)

    def create_table_store(self):
        """  """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS stores (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        store VARCHAR(150) UNIQUE);
                      """)

    def create_table_category(self):
        """  """
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS categories (
                        id BIGINT PRIMARY KEY AUTO_INCREMENT,
                        category VARCHAR(125),
                        sub_category VARCHAR(125)); 
                      """)

    def product_category(self):
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS _product_category ( 
                        product_id BIGINT REFERENCES products(barre_code) ON DELETE CASCADE,
                        category_id INT UNSIGNED REFERENCES categories(id) ON DELETE CASCADE,
                        PRIMARY KEY (product_id, category_id))
                       """)

    def product_store(self):
        self.db.query("""                                                           
                        CREATE TABLE IF NOT EXISTS _product_store (
                        product_id BIGINT REFERENCES Products(barre_code) ON DELETE CASCADE,
                        store_id INT REFERENCES stores(id) ON DELETE CASCADE,
                        PRIMARY KEY (product_id, store_id))
                      """)
        
    def product_sub_category(self):
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS _product_sub_category (
                        product_id BIGINT REFERENCES products(barre_code) ON DELETE CASCADE,
                        sub_category_id INT UNSIGNED REFERENCES categories(id) ON DELETE CASCADE,
                        PRIMARY KEY (product_id, sub_category_id))
                      """)

    def create_favorites_table(self):
        self.db.query("""
                        CREATE TABLE IF NOT EXISTS products (
                        barre_code BIGINT PRIMARY KEY,
                        name_product VARCHAR(150),
                        grade CHAR(1),
                        web_site VARCHAR(255));
                       """)

    def insert_product(self, id, name, grade, url, categories, sub_category, stores, *args):
        """ Insert the product data in the table"""
        self.db.query("""                        
                        INSERT INTO products (barre_code, name_product, grade, web_site) 
                        VALUES 
                        (:id, :name, :grade, :url) 
                        ON DUPLICATE KEY UPDATE barre_code = :id;
                      """, id=id, name=name, grade=grade, url=url)

    def insert_stores(self, id, name, grade, url, categories, sub_category, stores, *args):
        """ Insert the store list data in the table"""
        for store in stores:
            self.db.query("""
                            INSERT INTO stores(store)
                            VALUES (:store)
                            ON DUPLICATE KEY UPDATE store=:store;
                          """, store=store)

    def insert_category(self, id, name, grade, url, categories, sub_category, stores, *args):
        """ Insert the category list data in the table"""
        for category in categories:
            self.db.query("""
                            INSERT INTO categories(category, sub_category) 
                            VALUES 
                            (:category, :sub_category)
                            ON DUPLICATE KEY UPDATE category=:category;                          
                          """, category=category, sub_category=sub_category)

    def insert_product_store(self, id, name, grade, url, categories, sub_category, stores, *args):
        for store in stores:
            self.db.query("""
                             INSERT INTO _Product_store (product_id, store_id)
                             VALUES (

                             (SELECT barre_code FROM products WHERE name_product=:barre_code),
                             (SELECT id FROM stores WHERE store = :store_id  ));
                           """, barre_code=id, store_id=store)

    def insert_product_category(self, id, name, grade, url, categories, sub_category, stores, *args):
        for category in categories:
            self.db.query("""
                                INSERT INTO _Product_category (product_id, category_id)
                                VALUES (

                                (SELECT barre_code FROM products WHERE name_product=:barre_code),
                                (SELECT id FROM categories WHERE category = :category  ));
                              """, barre_code=id, category=category)

    def insert_product_sub_category(self, id, name, grade, url, categories, sub_category, stores, *args):
        for s_category in sub_category:
            self.db.query("""
                             INSERT INTO _Product_sub_category (product_id, sub_category_id)
                             VALUES (

                             (SELECT barre_code FROM products WHERE name_product=:barre_code),
                             (SELECT id FROM categories WHERE sub_category_id=:sub_category));
                           """, barre_code=id, sub_category=s_category)

    def insert_favory(self):
        pass

    def create_tables(self):
        """ Execute the creating table """
        self.create_table_product()
        self.create_table_store()
        self.create_table_category()

        self.product_store()
        self.product_category()
        self.product_sub_category()
        # self.create_favorites_table()

    def insert_rows(self, products):
        """ Completion the data row per row """
        for product in products:
            self.insert_product(*product)
            self.insert_stores(*product)

            self.insert_category(*product)
            self.insert_product_store(*product)

            # self.insert_product_category(*product)
            # self.insert_product_sub_category(*product)



def main():
    # Init the class
    db = DataBaseUser()
    connect = db.connect_mysql()
    creating = DataBaseCreator(connect)

    # Connecting in the API
    downloader = ApiCollectingData()                                                                # Load the API class
    connect = downloader.bring_out()                                                            # Load the API connexion
    final_products = downloader.format_final_response(connect)                                    # Harvest OPFF request

    # Create table
    create_table = creating.create_tables()                                              # Creating the necessary tables

    # Insert data
    insert_data = creating.insert_rows(final_products)


if __name__ == "__main__":
    main()

# C:\Users\Admin\GoogleDrive\DATA_OPEN_PROG\OPENCLASSROOMS\MyProjectOC\PROJET_05\MySQL\bin
