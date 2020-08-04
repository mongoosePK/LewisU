import random

# Randomly generate a datbase

numTransactions = 6

# List of transactions
tDb =[ ]

# Randomly create 6 transactions
for i in  range(numTransactions) :
    # creating 10 random items in a transaction
    transaction = random.sample(range(10),5)
    tDb.append(transaction)

print(tDb)
print()

# minimum support
minSupport = 2

#Frequency set
F = [ ]

# Create a frequency set - F[0]
frequencyMap = {}
for transaction in tDb :
    for item in transaction :
        if item in frequencyMap.keys() :
            frequencyMap[item] += 1
        else :
            frequencyMap[item] = 1



# Create F[0]
newFSet = []
for key in frequencyMap :
    print(key,frequencyMap[key])
    if frequencyMap[key] >= minSupport :
        newSet = []
        newSet.append(key)
        newFSet.append(newSet)

F.append(newFSet)

print(F)
print(F[0])

def generateProduct(f_k) :
    candidateSet = []
    for sets in f_k :
        for item in F[0] :
            if item in sets :
                continue
            newSet = sets.copy()
            if item[0] not in newSet :
                newSet.append(item[0])
                # Go through the candidate set
                # to make sure it is not in there
                addToCandidateSet = True
                duplicateCount = 0
                for cSet in candidateSet :
                    duplicate = True
                    for item in newSet :
                        if item not in cSet :
                            duplicate = False
                    if duplicate == True :
                        addToCandidateSet= False
                            
                if addToCandidateSet :
                    candidateSet.append(newSet)
    return candidateSet


c_1 = generateProduct(F[0])

print("The candidate set is " + str(c_1))




    



