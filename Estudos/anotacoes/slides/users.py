from math import *
import numpy as np

users = {
	"Angelica":{
		"Blues Traveler": 3.5,
		"Broken Bells": 2.0,
		"Norah Jones": 4.5,
		"Phoenix": 5.0,
		"Slighty Stoopid": 1.5,
		"The Strokes": 2.5,
		"Vampire Weekend": 2.0
	},
	"Bill":{
		"Blues Traveler": 2.0,
		"Broken Bells": 3.5,
		"Deadmau5": 4.0,
		"Phoenix": 2.0,
		"Slighty Stoopid": 3.5,
		"Vampire Weekend": 3.0
	},
	"Chan":{
		"Blues Traveler": 5.0,
		"Broken Bells": 1.0,
		"Deadmau5": 1.0,
		"Norah Jones":3.0,
		"Phoenix": 5.0,
		"Slighty Stoopid": 1.0,
	},
	"Dan":{
		"Blues Traveler": 3.0,
		"Broken Bells": 4.0,
		"Deadmau5": 4.5,
		"Phoenix": 3.0,
		"Slighty Stoopid": 4.5,
		"The Strokes": 4.0,
		"Vampire Weekend": 2.0	
	},
	"Hailey":{
		"Broken Bells": 4.0,
		"Deadmau5": 1.0,
		"Norah Jones": 4.0,
		"The Strokes": 4.0,
		"Vampire Weekend": 1.0
	},
	"Jordyn":{
		"Broken Bells": 4.5,
		"Deadmau5": 4.0,
		"Norah Jones": 5.0,
		"Phoenix": 5.0,
		"Slighty Stoopid": 4.5,
		"The Strokes": 4.0,
		"Vampire Weekend": 4.0
	},
	"Sam":{
		"Blues Traveler": 5.0,
		"Broken Bells": 2.0,
		"Norah Jones": 3.0,
		"Phoenix": 5.0,
		"Slighty Stoopid": 4.0,
		"The Strokes": 5.0,
	},
	"Veronica":{
		"Blues Traveler": 3.0,
		"Norah Jones": 5.0,
		"Phoenix": 4.0,
		"Slighty Stoopid": 2.5,
		"The Strokes": 3.0,
	}
}

def manhattan(rating1, rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])
	return distance

def computeNearestNeighbor(username, users):
	distances = []
	for user in users:
		if user != username:
			#distance = manhattan(users[user], users[username])
			distance = minkowski(users[user],users[username],2)
			#2 -> distancia euclidiana
			distances.append((distance, user))
	distances.sort()
	return distances
	
def recommend(username, users):
	# first find nearest neighbor
	nearest = computeNearestNeighbor(username,users)[0][1]
	recommendations = []
	# now find bands neighbor rated that user didn't
	neighborRatings = users[nearest]
	userRatings = users[username]

	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))

	#using the fn sorted for variety - sort is more efficient
	return sorted(recommendations,
		key=lambda artistTuple: artistTuple[1],
		reverse = True)

def minkowski(rating1, rating2, r):
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

def pearson(rating1, rating2):
	sum_xy = 0
	sum_x = 0
	sum_y = 0
	sum_x2 = 0
	sum_y2 = 0
	n = 0

	for key in rating1:
		if key in rating2:
			n += 1
			x = rating1[key]
			y = rating2[key]
			sum_xy += x * y
			sum_x += x
			sum_y += y
			sum_x2 += x**2
			sum_y2 += y**2
	# if no ratings in common return 0
	if n == 0:
		return 0
	# now compute denominator
	denominator = (sqrt(sum_x2 - (sum_x**2) / n) * 
		sqrt(sum_y2 - (sum_y**2) / n))

	if denominator == 0:
		return 0
	else:
  		return (sum_xy - (sum_x * sum_y) / n) / denominator

def cosine(rating1,rating2):
	sum_x = 0
	sum_y = 0
	xy = 0

	for key in rating1:
		sum_x += rating1[key]**2
		if key not in rating2:
			rating2[key] = 0.0

	for key in rating2:
		sum_y += rating2[key]**2
		if key not in rating1:
			rating1[key] = 0.0

	x = sqrt(sum_x)
	y = sqrt(sum_y)

	for key in rating1:
		xy += rating1[key]*rating2[key]

	cosine = xy / (x * y)

	return cosine
	