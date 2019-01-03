# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import requests as req

from pprint import pprint

# CONSTANTS #

CATEGORY = ["Viandes",
            "Boissons",
            "Diététique",
            "Produits_laitiers",
            "Produits_de_la_mer",
            "Biscuiterie"
            ]


class ApiCall:
    """ CALL THE API OPEN FOOD FACT """

    def __init__(self):
        """  """
        pass

    def connecting(self):  # -> Pourquoi PyCharm me suggère d'utiliser la méthode static?
        """ USE THE CONFIGURATION FOR THE CONNECTING """

        global api, config

        for category in CATEGORY:

            """ Ma boucle qui collect mes produits de chaque categories ne fonctionne plus, 
            pourtant avant la création de ma classe celle-ci marchait trés bien^^ """

            api = "https://fr.openfoodfacts.org/cgi/search.pl"             # Address OpenFooFact.org the API FR locating
            config = {"action": "process",                                         # This config for  for connecting API
                      "tagtype_0": "categories",                                            # Get the result by category
                      'tag_0': category,                                         # the tag represents the article search
                      "tag_contains_0": "contains",
                      "page_size": 50,                                                     # Number of articles per page
                      "json": 1}                                                              # The API response in JSON

        return api, config

    def api_response(self):  # -> Pourquoi PyCharm me suggère d'utiliser la méthode static?
        """ USE THE RESPONSE THE API """

        global products

        requests = req.get(api, params=config)                               # Uses the configuration for the connection
        response = requests.json()                                                         # Return the response in JSON
        products = response['products']                                                          # Finally result of API

        return products                                                                    # Return the finally response

    def final_product(self):  # -> Pourquoi PyCharm me suggère d'utiliser la méthode static?
        """ FORMATTED THE RESPONSE JUST HARVEST THE CATEGORY'S SELECTED """

        pos = 0
        print(len(products))

        product_final = []

        for product in products:
            """ J'ai supprimé le dictionnaire pour mes champs, et a opter 
            pour le nomage de mes champ afin de pouvoir les manipuler """

            try:
                categories = product['categories']
                name = product['product_name_fr']
                grade = product['nutrition_grade_fr']
                website = product['url']
                store = product['stores']
                keys = (categories, name, grade, website, store)
                # A tuple that organizes and respect the order of the fields

                pos += 1

                refactor = sorted(keys)
                product_final.append(refactor)
                pprint(product_final)

            except KeyError:
                print("KeyError", "POSITION ACTUEL :", pos)
                continue     # Tester si le 'continue' termine le travail
            except IndexError:
                print("IndexError", "POSITION ACTUEL :", pos)

        print(pos)

        return product_final


def main():
    """ A cette heure ma classe marche bien, sauf la boucle
    d'entrè, puis mes champs vide qui arrete le receuil des donnèes """

    """Mes variables 'global' me servent juste à fonctionnner ma classe, elle seront remplacer et organiser
     par le constructeur """

    call = ApiCall()
    connect = call.connecting()
    formated = call.api_response()
    final = call.final_product()


if __name__ == "__main__":
    main()
