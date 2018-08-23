from math import *

max_r = 5
min_r = 1

users = {
	"David":{
		"Imagine Dragons": 3,
		"Daft Punk": 5,
		"Lorde": 4,
		"Fall Out Boy": 1
	},
	"Matt":{
		"Imagine Dragons": 3,
		"Daft Punk": 4,
		"Lorde": 4,
		"Fall Out Boy": 1
	},
	"Ben":{
		"Kacey Musgraves": 4,
		"Imagine Dragons": 3,
		"Lorde": 3,
		"Fall Out Boy": 1
	},
	"Chris":{
		"Kacey Musgraves": 4,
		"Imagine Dragons": 4,
		"Daft Punk": 4,
		"Lorde": 3,
		"Fall Out Boy": 1	
	},
	"Tori":{
		"Kacey Musgraves": 5,
		"Imagine Dragons": 4,
		"Daft Punk": 5,
		"Fall Out Boy": 3
	}
}

def computeSimilarity(band1, band2, userRatings):
	averages = {}
	for (key,ratings) in userRatings.items():
		averages[key] = (float(sum(ratings.values())) / len(ratings.values()))

	num = 0
	den1 = 0
	den2 = 0
	for(user, ratings) in userRatings.items():
		if band1 in ratings and band2 in ratings:
			avg = averages[user]
			num += (ratings[band1] - avg) * (ratings[band2] - avg)
			den1 += (ratings[band1] - avg)**2
			den2 += (ratings[band2] - avg)**2
			
	return num / (sqrt(den1) * sqrt(den2))

def normalize(rating):
	return (2*(rating - min_r) - (max_r - min_r))/(max_r - min_r)

def unnormalize(rating):
	return ((0.5 * ((rating + 1)*(max_r - min_r))) + min_r)


def recommend(ratings, item):
	similarity = {}
	num = 0
	den = 0

	if item in ratings:
		return ratings[item]

	for band in ratings:
		similarity[band] = computeSimilarity(item,band,users)
		ratings[band] = normalize(ratings[band])

		num += ratings[band] * similarity[band]
		den += abs(similarity[band])

	p = unnormalize(num / den)
	return p


