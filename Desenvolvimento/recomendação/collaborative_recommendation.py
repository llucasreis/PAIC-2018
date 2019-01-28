from math import *
import numpy as np
import pandas as pd
from collections import Counter

df = pd.read_csv('../datasets/dados-pesquisa/avaliacao.csv')
df.drop(['Timestamp'],axis=1,inplace=True)

df = df.astype(float)
df.index = range(1,len(df)+1)

voters = ['eleitor' + str(i) for i in range(1,len(df)+1)]

new_df = df.mask(np.random.random(df.shape) < .4)

new_df.index = voters


def minkowski(rating1, rating2, r=1):
	distance = 0
	commonRatings = False

	for candidate in rating1.keys():

		if not isnan(rating1[candidate]) and not isnan(rating2[candidate]):

			distance += pow(abs(rating1[candidate] - rating2[candidate]), r)
			commonRatings = True

	return pow(distance, 1/r) if commonRatings else float('Inf')

def neighbor(votername):
	distances = []

	for voter in voters:
		if voter != votername:

			distance = minkowski(new_df.loc[voter], new_df.loc[votername])
			distances.append((distance, voter))

	return sorted(distances,
		key=lambda voterTuple: voterTuple[0])


def listOfRecommendations(votername):

	k_nearest = neighbor(votername)[:7]
	nearest_neighbors = [voter[1] for voter in k_nearest]

	voter_ratings = new_df.loc[votername]

	candidate_counter, score_counter = [], {}

	for voter in nearest_neighbors:
		neighbor_ratings = new_df.loc[voter]

		for candidate in neighbor_ratings.keys():
			if isnan(voter_ratings[candidate]) and not isnan(neighbor_ratings[candidate]):

				candidate_counter.append(candidate)

				if score_counter.get(candidate) is None:
					score_counter[candidate] = neighbor_ratings[candidate]
				else:
					score_counter[candidate] += neighbor_ratings[candidate]

	candidate_counter = Counter(candidate_counter)
	recomendations = []

	for candidate in candidate_counter:
		recomendations.append((candidate, score_counter[candidate] / candidate_counter[candidate]))

	return sorted(recomendations,
			key=lambda candidateTuple: candidateTuple[1],
			reverse=True)

def recommend(userRating):
	for candidate in list(new_df.columns):
		if candidate not in userRating:
			userRating[candidate] = float('NaN')

	new_df.loc['eleitor' + str(len(df)+1)] = userRating

	recomendations = listOfRecommendations(new_df.index[-1])

	new_df.drop(new_df.index[-1])

	return recomendations