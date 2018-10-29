import random

rating = [1,2,3,4,5]
candidates = ["alckmin","alvaro","amoedo","bolsonaro","boulos","ciro","daciolo","goulart","haddad","marina","meirelles"]

maxOfVoters = 10
voters = {}

for i in range(1,maxOfVoters):
    numberOfCandidates = random.randint(3, len(candidates))
    
    aux = {}
    for _ in range(numberOfCandidates):
        candidate = candidates[random.randint(0, len(candidates) - 1)]
        
        while candidate in aux.keys():
            candidate = candidates[random.randint(0, len(candidates) - 1)]

        aux[candidate] = random.choice(rating)

    voters["voter" + str(i)] = aux

def getVoters():
	return voters