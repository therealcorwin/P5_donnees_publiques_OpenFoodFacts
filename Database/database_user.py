# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Database.database import DataBaseCreator


class DataBaseUser:

    def __init__(self):
        self.database = DataBaseCreator()  # Load the database class
        self.db = self.database.connect_mysql()

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
    """ Init the class """
    user = DataBaseUser()

    """ Control the database """
    get_bases = user.get_databases()                                                      # Get the database list
    get_tables = user.get_tables()                                                           # Get the table list
    get_products = user.get_all_products()                                                  # Get the insert list

    # choose = user.choose_database()


if __name__ == "__main__":
    main()
