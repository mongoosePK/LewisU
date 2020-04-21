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

#print(tDb)
#print()

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
    # print(key,frequencyMap[key])
    if frequencyMap[key] >= minSupport :
        newSet = []
        newSet.append(key)
        newFSet.append(newSet)

F.append(newFSet)

#F newFset   1itemSet
#[ [         [ ] ,     [ ]....  ]  ]

#print(F)
#print(F[0])

# Generate F[0]  X   F[K]

# F[0]
#[ [ 1 item ] ,     [ ]....  ]  

#F[K]  sset
# #[ [ k item ] ,     [ ]....  ]

#C[K+1] = F[0] X F[K]

# newSet -  possibly the new cset
# conditions for newSet - F[0] must not be in any of the sets (items in F[k]

# Conditions for cset - do not want any duplicates  - if at least 1 item in newSet is in cset, then it is not a duplicate, if this is the case
# for every cset then we can add newset to C[k+1]
#C[K+1] =  [ [cset],...  ]

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
                    isAllContained = True
                    for item in newSet :
                        if item not in cSet :
                            isAllContained = False
                    if isAllContained == True :
                        addToCandidateSet= False
                            
                if addToCandidateSet :
                    candidateSet.append(newSet)
    return candidateSet

def doSequenceFilter(candidateSet) :

    cSize = len(candidateSet)
    cSetString = ''.join(map(str,candidateSet))
    minimumSupportCount = 0
    for transaction in tDb :
        # Looking at index + cSize in the transaction list
        # if this matches the candidate set then return true
        # otherwise we advance to the next index and to the same

        # One solution put transaction array index - index + size into
        # a string, can candidate set into a string then do a comparison

        for index,character in enumerate(transaction) :

            # Check the out of bound error condition
            if index + cSize < len(transaction) :
                miniSet = []
                for i in range(index,index+cSize) :
                    miniSet.append(transaction[i])

                # Generate the string of the transaction subset 
                miniSetString = ''.join(map(str,miniSet))

                # Compare the strings, if the two match, increment
                # the minimum support count
                if (cSetString == miniSetString) :
                    minimumSupportCount += 1
                    break
        
    if minimumSupportCount >= minSupport :
        return True
    else :
        return False
        

#F[0] x F[K] and filter 
def generateSequenceProduct(f_k) :
    f_k_1 = []

    for sets in f_k :
        for item in F[0] :
            if item in sets :
                continue
            newSet = sets.copy()
            if item[0] not in newSet :
                # This newSet is going into f_k+1 only if it meets sequenced minimum
                # support over the databse
                newSet.append(item[0])
                addToSet = doSequenceFilter(newSet)
                if addToSet == True :
                    f_k_1.append(newSet)
    return f_k_1

def doFilter(c_k) :
    frequencyCount = {}
    f_k = []
    for transaction in tDb :
        # if any item is not in c_k then do not increment the frequency count
        for index, cset in enumerate(c_k) :
            incrementFrequency = True
            for item in cset :
                if item not in transaction :
                    incrementFrequency = False
            if incrementFrequency == True :
                if index in frequencyCount.keys() :
                    frequencyCount[index] += 1
                else :
                    frequencyCount[index] = 0

    for key in frequencyCount :
        if frequencyCount[key] >= minSupport :
            f_k.append(c_k[key])
    return f_k

c_1 = generateProduct(F[0])
#print("The F[1] is " + str(doFilter(c_1)))

#print()
#print("The candidate set is " + str(c_1))
k = 0

val = int(input("Enter the type of Apriori algorithm 0 - non sequence, 1 - sequence: "))

if val == 0 : 
    # Here is the non-sequence version
    while len(F[k]) != 0 :
        c_k = generateProduct(F[k])
        element = doFilter(c_k)
        F.append(element)
        k = k+1
else :
    while len(F[k]) != 0 :
        F.append(generateSequenceProduct(F[k]))
        k = k +1
    
    

print(tDb)

for i in range(len(F)) :
    print( "F[" +str(i) + "] :" + str(F[i]) )

    
    



    



