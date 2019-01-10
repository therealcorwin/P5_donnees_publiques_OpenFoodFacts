# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec

from constants import *


class Main:

    def __init__(self):
        pass

    def step_1(self, connect):
        DB_CONNECT = rec.Database("""mysql+mysqlconnector://USER:PASSWORD@localhost/?charset=utf8mb4""")
        pass

    def step_2(self, create):
        DB_CREATE = rec.Database("""mysql+mysqlconnector://USER:PASSWORD@localhost/?charset=utf8mb4""")
        pass


def main():
    pass


if __name__ == "__main__":
    main()

