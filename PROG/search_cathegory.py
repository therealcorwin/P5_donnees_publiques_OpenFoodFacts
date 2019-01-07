# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import requests as req

from pprint import pprint

# CONSTANTS #

CATEGORIES = ["Charcuterie",          # 6 879 line total
              "Boissons",             # 9 808 line total
              "Céréales",             # 8 027 line total
              "Plats_préparé",        # 10 013 line total
              "Plats_surgelé",        # 9 180 line total
              "Biscuit",              # 11 385 line total
              "Viennoiseries"]        # 8 074 line total


class ApiCollecting:
    """ Call the Api Open Food Fact """

    def __init__(self):
        """ The constructor is not useful here """
        pass

    @classmethod
    def bring_out(cls):
        """ Use the configuration for the connecting interface """
        all_products = []
        api = "https://fr.openfoodfacts.org/cgi/search.pl"  # Address OpenFooFact.org the API FR locating
        for categories in CATEGORIES:
            config = {"action": "process",  # This config for  for connecting API
                      "tagtype_0": "categories",  # Get the result by category
                      'tag_0': categories,  # the tag represents the article search
                      "tag_contains_0": "contains",
                      "page_size": 10,  # Number of articles per page
                      "json": 1}  # The API response in JSON

            response = req.get(api, params=config)  # Uses the configuration for the connection
            results = response.json()  # Return the response in JSON
            products = results['products']  # Finally result of API
            all_products.extend(products)

        # pprint(all_products)

        return all_products

    def format_final_response(self, all_products):
        """ Formatted the response just harvest the categories selected """
        pos = 0
        print(len(all_products))
        product_final = []

        for product in all_products:
            try:
                categories = product['categories']
                name = product['product_name_fr']
                grade = product['nutrition_grade_fr']
                website = product['url']
                store = product['stores']
                keys = (name, website)

                formatting = sorted(keys)
                product_final.append(formatting)
                pos += 1

            except KeyError:
                print("KeyError", "POSITION ACTUEL :", pos)

        pprint(product_final)
        print(pos)

        return product_final


def main():
    call = ApiCollecting()
    connect = call.bring_out()
    final = call.format_final_response(connect)


if __name__ == "__main__":
    main()
