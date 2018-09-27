from math import *
import voters
import numpy as np

number_areas = 7
voters = voters.getVoters()

def rateOfCandidates(voter):
	for candidate in voter:
		mean = 0
		#for area,rating in voter[candidate].items():
		rating = list(voter[candidate].values())
		voter[candidate] = np.median(rating)
		#print(np.mean(rating), np.median(rating))
		#print(np.mean(list(voter[candidate].values())))
		#	mean += rating
		#voter[candidate] = round(mean/number_areas)
	return voter

def minkowski(rating1, rating2, r = 2):
	distance = 0
	commonRatings = False
	for key in rating1:
		if key in rating2:
			distance += pow(abs(rating1[key] - rating2[key]), r)
			commonRatings = True
	if commonRatings:
		return pow(distance, 1/r)
	else:
		return 0 #Indicates no ratings in common

def computeNearestNeighbor(votername):
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
	# first find nearest neighbor
	nearest = computeNearestNeighbor(votername)[0][1]
	recommendations = []
	# now find bands neighbor rated that user didn't
	neighborRatings = voters[nearest]
	voterRatings = voters[votername]

	for candidate in neighborRatings:
		if not candidate in voterRatings:
			recommendations.append((candidate, neighborRatings[candidate]))

	#using the fn sorted for variety - sort is more efficient
	return sorted(recommendations,
		key=lambda artistTuple: artistTuple[1],
		reverse = True)	


for voter,voter_rate in voters.items():
	rateOfCandidates(voter_rate)