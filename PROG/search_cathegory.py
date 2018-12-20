#!/usr/bin/env python3
# -*- coding: Utf-8 -*-

import requests as req

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

    def connecting(self):
        api = "https://fr.openfoodfacts.org/cgi/search.pl"  # Address OpenFooFact.org the API FR locating
        config = {"action": "process",  # This config for  for connecting API
                  "tagtype_0": "categories",  # Get the result by category
                  'tag_0': CATEGORY,  # the tag represents the article search
                  "tag_contains_0": "contains",
                  "page_size": 10,  # Number of articles per page
                  "json": 1}  # The API response in JSON

        requests = req.get(api, params=config)  # Uses the configuration for the connection
        response = requests.json()  # Return the response in JSON
        products = response['products']  # Finally result of API
        pprint(products)
        return products  # Return the finally response

    def research(self, response):
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

