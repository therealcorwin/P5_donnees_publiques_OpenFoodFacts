# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import records as rec
from Database.database import *


class DataBaseUser:

    def __init__(self):
        self.db = None

    """TEMP"""
    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database(f"mysql+mysqlconnector://{cons.USER}:{cons.PASSWORD}@localhost/"
                               f"{cons.DATABASE}?charset=utf8mb4")
        return self.db
    """TEMP"""

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
    user = DataBaseUser()
    connecting = user.connect_mysql()                                                    # Load the MySQL connexion


    """ Control the database """
    get_bases = user.get_databases()                                                      # Get the database list
    # get_tables = user.get_tables()                                                           # Get the table list
    # get_products = user.get_all_products()                                                  # Get the insert list

    # choose = user.choose_database()

    # choose = connecting.choose_database()


if __name__ == "__main__":
    main()
