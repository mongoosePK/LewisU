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
                    isContained = True
                    for item in newSet :
                        if item not in cSet :
                            isNotContained = False
                    if isNotContained == True :
                        addToCandidateSet= False
                            
                if addToCandidateSet :
                    candidateSet.append(newSet)
    return candidateSet

def doFilter(c_k):
    frequencyCount = {}
    f_k = []
    for transaction in tDb:
        # if any item is not in c_k then do not increment the frequesncy count
        for index, cset in enumerate(c_k):
            incrementFrequency = True
            for item in cset:
                if item not in transaction:
                    incrementFrequency = False
            if incrementFrequency == True:
                if index in frequencyCount.keys():
                    frequencyCount[index] += 1
                else:
                    frequencyCount[index] = 0

    for key in frequencyCount:
        if frequencyCount[key] >= minSupport:
            f_k.append(c_k[key])
    return f_k

c_1 = generateProduct(F[0])
print(f"the F[1] is {str(doFilter(c_1))}")
print("The candidate set is " + str(c_1))
k = 0

while len(F[k]) != 0:
    c_k = generateProduct(F[k])
    #filter c_k
    element = doFilter(c_k)
    F.append(element)
    k = k+1

for i in range(len(F)):
    print(f"F[{i}]: {str(F[i])}")