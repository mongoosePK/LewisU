import random
import csv
import pandas as pd
import itertools

#user databse
userDatabase = [ ]

    

with open("data/transactionList.csv") as csv_file :
    myFile = csv.reader(csv_file,delimiter=',')

    newList = []
    for index, line in enumerate(myFile) :
        if index == 0 :
            continue
        
        # Every 10th transaction is a new user user
        if index % 10 == 0 :

            newLine = []
            for x in line :
                if x == '' :
                    continue
                newLine.append(int(x))
            
            newList.append(newLine)
            userDatabase.append(newList)
            newList  = []
            continue

        newLine = []
        for x in line :
            if x == '' :
                continue
            newLine.append(int(x))
        newList.append(newLine)
        
        

print(userDatabase[0])
print()
print()
print(userDatabase[5])




def generateDb(userIndex) :

    # For your project - read transactionList file
    # userIndex was 0 , read lines 0 - 9
    # userIndex 1 - 10 - 19
    transactionDatabase = []
    numTransactions = 6
    # Randomly create 6 transactions
    for i in  range(numTransactions) :
        # creating 10 random items in a transaction
        transaction = random.sample(range(10),5)
        transactionDatabase.append(transaction)
    return transactionDatabase
    

def generateF_0(userFrequencySet) :
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

    userFrequencySet.append(newFSet)
    



# newSet -  possibly the new cset
# conditions for newSet - F[0] must not be in any of the sets (items in F[k]

# Conditions for cset - do not want any duplicates  - if at least 1 item in newSet is in cset, then it is not a duplicate, if this is the case
# for every cset then we can add newset to C[k+1]
#C[K+1] =  [ [cset],...  ]

def generateProduct(f_k,F_0) :
    candidateSet = []
    for sets in f_k :
        for item in F_0 :
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
def generateSequenceProduct(f_k,F_0) :
    f_k_1 = []

    for sets in f_k :
        for item in F_0 :
            if item in sets :
                continue
            
            if item[0] not in sets :
                # This newSet is going into f_k+1 only if it meets sequenced minimum
                # support over the databse
                newSet = sets.copy()
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


# minimum support
minSupport = int(input("Enter the minimum support : "))
kValue = int(input("Enter the k value to show the sequence" +
                   "frequency set for the list of users: "))
kValue1 = int(input("Enter the k value to show the non sequence" +
                   "frequency set for the list of users: "))

numberUsers = 3

#  Read in transaction database  - transactionList.csv

# For each user generate the F[0]
# Use the call generateF_0

# For each  user generate non sequence F[k]  > non-sequence.txt and sequence F[k] > sequence.txt

# creating the user F[k] database  - in this example - userListnonsequenceDb  and userListsequenceDb - this is based on the input

# Find the F[k] from those two databases

userListsequenceDb = [ ]
userListnonsequenceDb = []
for user in range(numberUsers) :
    tDb = generateDb(user)

    # print("Transactions for user: " + str(user))
    #print(tDb)

    nonSequenceF = []
    generateF_0(nonSequenceF)
    k = 0

    
    # Here is the non-sequence version
    while len(nonSequenceF[k]) != 0 :
        c_k = generateProduct(nonSequenceF[k],nonSequenceF[0])
        element = doFilter(c_k)
        nonSequenceF.append(element)
        k = k+1
    if kValue1 < len(nonSequenceF) :
        userListnonsequenceDb.append(nonSequenceF[kValue1])

    #print("Non sequence F[k] for user " + str(user) + " : ");
    # print(nonSequenceF)

    sequenceF = []
    generateF_0(sequenceF)
    k = 0
    # Generating the sequence set
    while len(sequenceF[k]) != 0 :
        sequenceF.append(generateSequenceProduct(sequenceF[k],sequenceF[0]))
        k = k +1

    if kValue < len(sequenceF) :
        userListsequenceDb.append(sequenceF[kValue1])
    print("Sequence F[k] for user " + str(user) + " : ")
    print(sequenceF)

    # Now that you you have the two databases find the  F[users k value] on those databases  - usersSequenceFset.txt usersNonsequenceFset.txt


print("Users non sequence database " + str(kValue1) )
for element in userListnonsequenceDb :
    print(element)
    print("------")

print()
print()

print("Users sequence database " + str(kValue) )
for element in userListsequenceDb :
    print(element)
    print("------")
    
#print(userListnonsequenceDb)
#print(userListsequenceDb)
    
    

#print(tDb)

#for i in range(len(F)) :
#    print( "F[" +str(i) + "] :" + str(F[i]) )

    
    



    



