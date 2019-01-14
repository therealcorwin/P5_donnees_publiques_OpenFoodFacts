# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec

import constants as cons


class DataBaseCreator:

    def __init__(self):
        pass

    def connect_mysql(self):
        """"""
        connect = rec.Database("mysql+mysqlconnector://%s:%s@localhost/%s?charset=utf8mb4"
                               % (cons.USER, cons.PASSWORD, cons.DATABASE))

        return connect

    def show_database(self, connect):
        """"""
        rows = connect.query("SHOW DATABASES")
        for row in rows:
            print(row['Database'])
        return rows

    def show_table(self, connect):
        """"""
        rows = connect.query("SHOW TABLES")
        for row in rows:
            print(row)
        return rows

    def use_database(self, connect):
        """"""
        pass

    def create_table_product(self, connect):
        """"""
        connect.query(""" CREATE TABLE Products_10k_Table (
                                Barre_code TINYINT(13) PRIMARY KEY,
                                Name_product VARCHAR(30),
                                Grade CHAR(1),
                                Web_site VARCHAR(255)) """)
        return connect

    def create_table_categories(self, connect):
        """"""
        connect.query(""" CREATE TABLE Categories (
                                Categories VARCHAR(15))""")
        return connect

    def create_table_stores(self, connect):
        """"""
        connect.query(""" CREATE TABLE Stores (
                                Stores VARCHAR(50)) """)
        return connect

    def create_store_table(self):
        pass

    def create_category_table(self):
        pass

    def create_favorites_table(self):
        pass


def main():
    databases = DataBaseCreator()

    connecting = databases.connect_mysql()
    # product = databases.create_table_product(connecting)
    # categories = databases.create_table_categories(connecting)
    # stores = databases.create_table_stores(connecting)
    show = databases.show_table(connecting)
    # choose = databases.choose_database(connecting)


if __name__ == "__main__":
    main()
#  QUERY_INSERT = """()"""
#  QUERY_ALTER = """()"""
#  QUERY_MODIFY = """()"""
#  QUERY_INSERT = """(INSERT IN TO Product(product_name, generic_name, url, nutrition_grade_fr, store)
#                     VALUES(:product_name, :generic_name, :url, :nutrition_grade_fr, :store))"""
