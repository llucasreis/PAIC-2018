from math import *

import collaborative_recommendation as cr
import content_based_recommendation as cbr

cr_users = {}
cbr_users = {}


if __name__ == "__main__":

	cr_users['Lucas'] = {'João Amoêdo': 3, 'Ciro Gomes': 3, 'Fernando Haddad': 1}

	cbr_users['Lucas'] = {'saude': 3, 'seguranca': 5, 'educacao': 3, 'economia': 3, 'cultura': 2, 'tecnologia': 5,
	'meio ambiente': 2}

	cr_recommendation = cr.recommend(cr_users['Lucas'])

	print(cr_recommendation)
	print('----------------------------------')

	final_recommendation = cbr.recommend(cr_recommendation, cbr_users['Lucas'])

	print(final_recommendation)