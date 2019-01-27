# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec

import Config.constants as cons


class DataBaseUser:
    """

    """

    def __init__(self):
        """  """
        self.db = None

    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database(f"mysql+mysqlconnector://{cons.USER}:{cons.PASSWORD}@localhost/"
                               f"{cons.DATABASE}?charset=utf8mb4")
        return self.db

# si la "liste" retournée est vide, il n'a pas de base. Il suffit de tester
# Pour la liste des tables, tu peux utiliser la methode get_table_names()

    def get_databases(self):
        """ Control the database """
        databases = self.db.query("SHOW DATABASES;")
        for row in databases:
            print(row['Database'])
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

    def use_database(self):
        """  """
        self.db.query("""
                          USE f"{%s};
                      """,)
        pass


def main():
    """ Init the class, and Connecting in the database """
    databases = DataBaseUser()                                                                 # Load the database class
    connecting = databases.connect_mysql()                                                    # Load the MySQL connexion

    """ Choose the existing databases """

    """ Control the database """
    get_bases = databases.get_databases()                                                        # Get the database list
    get_tables = databases.get_tables()                                                             # Get the table list
    get_products = databases.get_all_products()                                                    # Get the insert list


if __name__ == "__main__":
    main()
