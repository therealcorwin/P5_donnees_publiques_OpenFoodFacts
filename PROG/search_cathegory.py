# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import constants as cons

from pprint import pprint

import csv
import requests as req


class ApiCollectingData:
    """ Call the Api Open Food Fact """

    def __init__(self):
        """ The constructor is not useful here """
        pass

    def bring_out(self):
        """ Use the configuration for the connecting interface """

        all_products = []
        api = "https://fr.openfoodfacts.org/cgi/search.pl"                 # Address OpenFooFact.org the API FR locating
        for category in cons.CATEGORIES:
            config = {"action": "process",                                         # This config for  for connecting API
                      "tagtype_0": "categories",                                            # Get the result by category
                      'tag_0': category,                                         # the tag represents the article search
                      "tag_contains_0": "contains",
                      "page_size": 500,                                                     # Number of articles per page
                      "json": 1}                                                              # The API response in JSON

            response = req.get(api, params=config)                           # Uses the configuration for the connection
            results = response.json()                                                      # Return the response in JSON
            products_section = results['products']                                               # Finally result of API

            for product in products_section:
                product['main_category'] = category

            all_products.extend(products_section)

        # pprint(all_products)

        return all_products

    def validate_the_data(self, keys, products_section):
        """ Validate the complete fields """

        for key in keys:
            if key not in products_section or not products_section[key]:
                return False
        return True

    def format_final_response(self, all_products):
        """ Formatted the response just harvest the categories selected """

        product_final = []
        keys = ['id', 'categories', 'product_name_fr', 'nutrition_grade_fr', 'stores', 'url']

        print(len(all_products))

        for product in all_products:
            if self.validate_the_data(keys, product):

                barre_code = product['id']
                categories = product['categories']
                format_categories = product['main_category']
                name = product['product_name_fr']
                grade = product['nutrition_grade_fr']
                store = product['stores']
                website = product['url']

                key = (barre_code, format_categories.upper(), name, grade, store, website)

                formatting = key
                product_final.append(formatting)

        pprint(product_final)
        print(len(product_final))

        return product_final

    def save_data(self, product_final, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            for e in product_final:
                writer.writerow(e)

        return filename


def main():

    name = ApiCollectingData()
    connect = name.bring_out()
    final = name.format_final_response(connect)
    # save_in_file = call.save_data(final , 'output_data_save.csv')


if __name__ == "__main__":
    main()
