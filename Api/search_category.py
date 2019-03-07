# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import requests as req
from pprint import pprint

from Config import constants as conf


class ApiCollectingData:
    """
        This class has the responsibility of collecting a certain number
        of products, in selected categories, thus to give a valid
        structure for the insertion in the database
    """

    def __init__(self):
        """ The constructor is not used here """
        pass

    def connect_and_harvest(self):
        """ Use the configuration for the connecting interface """
        all_products = []
        # Address OpenFooFact.org the API FR locating
        api = "https://fr.openfoodfacts.org/cgi/search.pl"
        for category in conf.CATEGORIES:
            # This config for  for connecting API
            config = {"action": "process",
                      # Get the result by category
                      "tagtype_0": "categories",
                      # the tag represents the article search
                      'tag_0': category,
                      "tag_contains_0": "contains",
                      # Number of articles per page
                      # Min content 20, Max content 1000
                      "page_size": 20,
                      # The API response in JSON
                      "json": 1}
            # Uses the configuration for the connection
            response = req.get(api, params=config)
            # Return the response in JSON
            results = response.json()
            # Finally result of API
            products_section = results['products']
            for product in products_section:
                product['main_category'] = category
            all_products.extend(products_section)
        ###############################
        """ PRINT RESULTS FUNCTION """
        ###############################
        # Pprint the first result the API response
        # pprint(all_products)
        ###############################
        return all_products

    def format_final_response(self, all_products):
        """ Formatted the response just harvest the categories selected """
        product_final = []
        keys = ['id', 'product_name_fr', 'nutrition_grade_fr',
                'url', 'categories', 'main_category', 'stores']
        print(len(all_products))
        for product in all_products:
            if self.validate_the_data(keys, product):
                barcode = product['id']
                name = product['product_name_fr']
                grade = product['nutrition_grade_fr']
                website = product['url']
                categories = product['categories'].upper().split(',')
                sub_category = product['main_category'].upper()
                stores = product['stores'].upper().split(',')
                # Respect of the order of the criteria insert in a tuple
                # and simple format in database insert
                key = (barcode, name, grade, website,
                       categories, sub_category, stores)
                formatting = key
                product_final.append(formatting)
                ###############################
                """ PRINT RESULTS FUNCTION """
                ###############################
                # Print type results the stores and category count
                # print('produit: ', name.upper(), '\n'*2,
                      # 'disponnible dans', [len(stores)],
                      # 'magasin(s): = ', stores,
                      # 'présent dans', [sub_category], [len(categories)],
                      # 'categorie(s): = ', categories, '\n',
                      # f"Nous avons récupéré {len(product_final)} produits")
                # Print type results final form
                pprint(product_final)
                ###############################
        return product_final

    def validate_the_data(self, keys, products_section):
        """ Validate the complete fields """
        for key in keys:
            if key not in products_section or not products_section[key]:
                return False
        return True


def main():
    """ Initialize the data collect """

    # Download the response
    downloader = ApiCollectingData()
    connect = downloader.connect_and_harvest()
    downloader.format_final_response(connect)


if __name__ == "__main__":
    main()
