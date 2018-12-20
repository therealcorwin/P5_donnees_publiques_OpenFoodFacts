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
        print(len(response['products']))
        formated_product = []
        for product in response['products']:
            try:
                product_cat = {
                    # product['categories'],
                    # product['product_name'],
                    # product['generic_name_fr'],
                    # product['nutrition_grade_fr'],
                    # product['stores'],
                    product['url']}
                preform = sorted(product_cat)
                pos += 1
                formated_product.append(preform)
                pprint(preform)

            except KeyError:
                print("KeyError", "POSITION ACTUEL :", pos)
            except IndexError:
                print("IndexError", "POSITION ACTUEL :", pos)
        print(pos)


def main():
    call = Api_call()
    api = call.research()


if __name__ == "__main__":
    main()

