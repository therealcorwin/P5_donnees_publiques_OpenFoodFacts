#!/usr/bin/env python3
# -*- coding: Utf-8 -*-

import requests
import records

from pprint import pprint


# CONSTANTS #

# DB_CONNECT = records.Database("""mysql+mysqlconnector://OPFF:OCP5@localhost/Category_Product?charset=utf8mb4""")

# CATEGORY = 'Chocolat'                                             # print(json.dumps(products, sort_keys=True, indent=1))

# "https://fr.openfoodfacts.org/cgi/search.pl ?search_terms="OBJECT"&search_simple=1"

GRADES = ["a", "b", "c", "d", "e"]
CATEGORY = ["Viandes",
            # "Boissons",
            # "Poissons",
            # "Charcuterie",
            # "Fromage",
            # "Produits_laitiers",
            # "Chocolat",
            # "Pâtes",
            "Epicerie"]
ITEM = "Viandes"
PRODUCT = {}


def research():
        api = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=" + ITEM + "&search_simple=1"
        config = {"action": "process", "page_size": 150, "json": 1}

        req = requests.get(api, params=config)
        response = req.json()

        pos = 0
        while pos < 10:
            product = (
                response['products'][pos]['categories'],
                response['products'][pos]['product_name'],
                response['products'][pos]['generic_name_fr'],
                response['products'][pos]['url'],
                response['products'][pos]['nutrition_grade_fr'],
                response['products'][pos]['stores'])

            preform = sorted(product)
            pos += 1

            pprint(preform)


def formating():
    for form in PRODUCT:
        pass


def main():
    research()


if __name__ == "__main__":
    main()

