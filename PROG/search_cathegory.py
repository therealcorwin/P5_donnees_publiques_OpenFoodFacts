#!/usr/bin/env python3
# -*- coding: Utf-8 -*-

import requests
import records

from pprint import pprint


# CONSTANTS #

# print(json.dumps(products, sort_keys=True, indent=1))

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

class Api_call:

    def __init__(self):
        pass

    def research(self):
            api = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=" + ITEM + "&search_simple=1"
            config = {"action": "process", "page_size": 1000, "json": 1}

            req = requests.get(api, params=config)
            response = req.json()

            pos = 0
            try:
                while pos < 50:
                    product = {
                        response['products'][pos]['categories'],
                        # response['products'][pos]['product_name'],
                        # response['products'][pos]['generic_name_fr'],
                        response['products'][pos]['nutrition_grade_fr'],
                        # response['products'][pos]['stores'],
                        response['products'][pos]['url']}
                    preform = sorted(product)
                    pos += 1
                    pprint(preform)

            except KeyError:
                print("KeyError", "POSITION ACTUEL :", pos)

                # gett = response.get(preform)
                # print(gett)

            except IndexError:
                print("IndexError", "POSITION ACTUEL :", pos)

def main():
    call = Api_call()
    api = call.research()


if __name__ == "__main__":
    main()

