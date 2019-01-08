# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec

# DB_CONNECT = records.Database("""mysql+mysqlconnector://OPFF:OCP5@localhost/?charset=utf8mb4""")

# -tc-utiliser des verbes d'action pour les méthodes, comme create_category_table, create_store_table,
# -tc- create_product_store_table(), create_database(), drop_database(), etc.


class DataBaseCreator:

    def __init__(self):
        pass

    def create_database(self):
        pass

    def drop_database(self):
        pass

    def create_table_product(self):
        pass

    def create_store_table(self):
        pass

    def create_category_table(self):
        pass

    def create_product_store_table(self):
        pass

    def fav_like(self):
        pass


#  QUERY_INSERT = """()"""
#  QUERY_ALTER = """()"""
#  QUERY_MODIFY = """()"""
#  QUERY_INSERT = """(INSERT IN TO Product(product_name, generic_name, url, nutrition_grade_fr, store)
#                     VALUES(:product_name, :generic_name, :url, :nutrition_grade_fr, :store))"""
