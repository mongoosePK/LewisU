numTransactions = 6

tDb =[]
frequencyMap = []
minSupport = 4
F = []
for transaction in tDb:
    for item in transaction:
        if item in frequencyMap.keys():
            frequencyMap[item] += 1
        else:
            frequencyMap[item] = 1
# create F[0]
newFSet = []
for key in frequencyMap:
    print(key, frequencyMap[key])
    if frequencyMap[key] >= minSupport:
        newSet =[]
        newSet.append(key)
        newFSet.append(newSet)

F.append(newFSet)

print(F)
print(F[0])

def generateProduct(f_k):
    candidateSet = []
    for sets in f_k:
        for item in F[0]:
            for item in sets:
                continue
            newSet = sets.copy()
            if item[0] not in newSet:
                newSet.append(item[0])
                #go thru candidate set to make sure its not in there
                addToCandidateSet = True
            for cSet in candidateSet:
                noDuplicate = True
                for item in newSet:
                    if item not in cSet:
                        duplicate = False
                addToCandidateSet = False
            candidateSet.append(newSet)
    return candidateSet

c_1 = generateProduct(F[0])
print(c_1)