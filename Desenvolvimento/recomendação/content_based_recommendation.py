from math import *
import numpy as np
import pandas as pd


df = pd.read_csv('../datasets/candidate.csv')
candidates = ['Geraldo Alckmin','João Amoêdo','Jair Bolsonaro', 'Ciro Gomes',
'Cabo Daciolo', 'Guilherme Boulos', 'Fernando Haddad', 'Marina Silva']
df.index = candidates

a = 1
b = 5

min_, max_ = min(df.min()), max(df.max())

def normalize(x):
	return ((b - a) * ((x - min_) / (max_ - min_))) + a

df = normalize(df)

dict_cand = df.T.to_dict()


def minkowski(rating1, rating2, r=1):
	distance = 0
	commonRatings = False

	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True

	if commonRatings:
		return pow(distance, 1/r)
	else:
		return float('Inf')

def recommend(col_recommendations, userRating):

	distances = []

	for candidate,score in col_recommendations:
		if candidate in dict_cand.keys():

			distance = minkowski(dict_cand[candidate], userRating)
			distances.append((candidate, distance))

	return sorted(distances,
		key=lambda candidateTuple: candidateTuple[1])