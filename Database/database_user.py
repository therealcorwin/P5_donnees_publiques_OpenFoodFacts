# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec

import Config.constants as cons
from Database.database import DataBaseCreator as Base


class DataBaseUser:

    def __init__(self):
        self.db = None

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
    """ Connecting in the API """

    """ Connecting in the database """
    databases = Base()                                                              # Load the database class
    connecting = databases.connect_mysql()                                                    # Load the MySQL connexion

    """ Control the database """
    # get_bases = databases.get_databases()                                                      # Get the database list
    # get_tables = databases.get_tables()                                                           # Get the table list
    # get_products = databases.get_all_products()                                                  # Get the insert list

    # choose = databases.choose_database()

    """ Create table """

    """ Insert data """


if __name__ == "__main__":
    main()
