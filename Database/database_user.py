# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec


from Database.database import DataBaseCreator


class DataBaseUser:

    def __init__(self):
        self.db = DataBaseCreator()

    def connect_mysql(self):
        pass

    def get_databases(self):
        """ Control the database """
        databases = self.db.query("SHOW DATABASES;")

        for row in databases:
            print(row['Database'])
        return databases

    def get_tables(self):
        """"""
        tables = self.db.query("SHOW TABLES;")
        for table in tables:
            print(table)
        return tables

    def get_all_products(self):
        return self.db.query("""
                                SELECT * FROM demo.Products;
                             """,
                             fetchall=True).as_dict()

    def use_database(self):
        """"""
        pass


def main():
    """ Connecting in the database """
    databases = DataBaseCreator()                                                              # Load the database class
    connecting = databases.connect_mysql()                                                    # Load the MySQL connexion

    """ Database class user """
    user = DataBaseUser()
    g_databases = user.get_databases()
    g_tables = user.get_tables()
    g_products = user.get_all_products()

    """ Control the database """
    get_bases = connecting.g_databases()
    # get_tables = connecting.get_tables()                                                          # Get the table list
    # get_products = connecting.get_all_products()                                                 # Get the insert list

    # choose = connecting.choose_database()


if __name__ == "__main__":
    main()
