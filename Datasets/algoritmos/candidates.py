from math import *
import voters_provider_2 as voters
import numpy as np

number_areas = 7
voters = voters.getVoters()

def rateOfCandidates(voter):
	for candidate in voter:
		mean = 0
		rating = list(voter[candidate].values())
		voter[candidate] = np.median(rating)
	return voter

def minkowski(rating1, rating2, r = 1):
	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True
	if commonRatings:
		return pow(distance, 1/r)
	else:
		return 0

def neighbor(votername):
	distances = []
	for voter in voters:
		if voter != votername:
			#distance = manhattan(users[user], users[username])
			distance = minkowski(voters[voter], voters[votername])
			#2 -> distancia euclidiana
			distances.append((distance, voter))
	distances.sort()
	return distances

def recommend(votername):
	nearest = neighbor(votername)[0][1]
	recommendations = []

	neighborRatings = voters[nearest]
	voterRatings = voters[votername]

	for candidate in neighborRatings:
		if not candidate in voterRatings:
			recommendations.append((candidate, neighborRatings[candidate]))

	return sorted(recommendations,
		key=lambda artistTuple: artistTuple[1],
		reverse = True)	


#for voter,voter_rate in voters.items():
#	rateOfCandidates(voter_rate)
