# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


class DataBaseUser:
    """
        This class has the responsibility to control the database of the user
    """

    def __init__(self, db):
        """ Just share the connection for MySQL """
        self.db = db

    def get_favorite_table(self):
        """ Control in the tables """
        favorites = self.db.query("""
                                SELECT * FROM PurBeurre.Favorites;
                             """,  fetchall=True).as_dict()
        if favorites is None:
            print("Aucun produit trouvè")
        return favorites

# SELECT * FROM Products AS product
    # JOIN products_categories_summary_key AS pc ON pc.product_id = product.barcode
    # JOIN Categories_summary AS c ON pc.c_category_id = c.id
    #
    # NATURAL JOIN Favorites;

    # # c_category, favorites.product_id, substitute_id, name_product, grade, web_site

    def get_all_products_per_category(self, category):
        """ Control in the tables """
        cat = self.db.query("""
                                SELECT c_category, product.barcode, product.name_product, 
                                product.grade, product.web_site FROM Products AS product
                                JOIN products_categories_summary_key AS pc ON pc.product_id = product.barcode  
                                JOIN Categories_summary AS c ON pc.c_category_id = c.id    
                                WHERE c.c_category = :user
                                AND product.grade IN ('b', 'c', 'd', 'e')
                                GROUP BY product.barcode;
                            """, user=category, fetchall=True).as_dict()
        return cat

    def choose_products_from_the_category(self, category, product):
        """ Offers a list of products with a holiest grade """
        prod = self.db.query("""
                                SELECT c_category, product.barcode, product.name_product, 
                                product.grade, product.web_site FROM Products AS product
                                jOIN Products_categories_summary_key AS pcsk ON pcsk.product_id = product.barcode
                                JOIN Categories_summary AS cs ON cs.id = pcsk.c_category_id
                                WHERE product.grade < :grade AND cs.c_category = :category
                                GROUP BY product.barcode;
                             """, grade=product['grade'], category=category, fetchall=True).as_dict()
        return prod

    def add_into_favorites(self, product, substitute):
        """Inserts the selected product and substitute into the Favorites table in the database."""
        product_favorite = self.db.query("""
                                            INSERT INTO Favorites 
                                            (id_product, id_substitute) 
                                            VALUES
                                            (:id_product, :id_substitute);
                                         """, id_product=product, id_substitute=substitute)
        return product_favorite
