#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import requests
import records

from pprint import pprint


# CONSTANTS #


DB_CONNECT = records.Database("""mysql+mysqlconnector://OPFF:OCP5@localhost/Category_Product?charset=utf8mb4""")

ITEM = 'Chocolat'                                             # print(json.dumps(products, sort_keys=True, indent=1))

PRODUCT = []
GRADES = ["a", "b", "c", "d", "e"]
CATEGORY = ["Viandes",
			"Boissons",
			"Poissons",
			"Charcuterie",
			"Riz",
			"Fromage",
			"Desserts",
			"Produits_laitiers",
			"Gâteaux",
			"Biscuit",
			"Chocolat",
			"Pâtes",
			"Epicerie"]


def research():

	for category in CATEGORY:
		for grade in GRADES:
			url = "https://fr.openfoodfacts.org/cgi/search.pl"
			config = {
				"action": "process",
				"tagtype_0": "categories",
				"tag_contains_0": "contains",
				"tag_0": category,
				"tagtype_1": "nutrition_grade_fr",
				"tag_contains_1": "contains",
				"tag_1": grade,
				"sort_by": "product_name",
				"page_size": 1,
				"json": 1
			}
			req = requests.get(url, params=config)
			response = req.json()
			PRODUCT.extend(response["products"])


			pprint(PRODUCT)

research()

#     products = (
#         response['products'][1]['product_name'],
#         response['products'][1]['generic_name_fr'],
#         response['products'][1]['url'],
#         response['products'][1]['nutrition_grade_fr'],  # + Picture
#         response['products'][1]['stores'])


#  QUERY_INSERT = """()"""
#  QUERY_ALTER = """()"""
#  QUERY_MODIFY = """()"""
#  QUERY_INSERT = """(INSERT IN TO Product(product_name, generic_name, url, nutrition_grade_fr, store)
#                     VALUES(:product_name, :generic_name, :url, :nutrition_grade_fr, :store))"""

