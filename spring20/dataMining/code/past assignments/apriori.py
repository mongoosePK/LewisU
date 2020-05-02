# apriori.py
# William Pulkownik
# Data Mining Spring 2020

# my version of the apriori project for data mining
# I tried to do it all in Dataframes and Dicts at first
# But it ended up being a lot more work because I would have
# had to rewrite most of the driver code you gave us

import random
import pandas as pd
import itertools
from itertools import combinations
from collections import defaultdict, Counter

# this block reads csv into a dataframe, drops NaN, and creates a list  
data = pd.read_csv('data/transactionList.csv',header=None)
data = data.dropna(axis='columns')
transactions = data.values.tolist()

# here we create dict of lists for transactions by user for every 10 transactions
# UserTransactions = {1:[[transaction1],[transaction2],[transaction3],[...]]
#                     2:[[transaction1],[transaction2],[transaction3],[...]]
#                      ...
#                     10:[[transaction1],[transaction2],[transaction3],[...]]}
userTransactions = defaultdict(list)
new_user=0
for index, transaction in enumerate(transactions):
    if index % 10 == 0:
        new_user += 1
    userTransactions[new_user].append(transaction)
for i in range(1,11):
    print(f'User {i}:\n {userTransactions[i]}\n')


# This function generates the list F[0]
# which contains all of the single elements meeting the minimum support
# and appends those values to the list passed into the function
def generateF_0(userFrequencySet):
    frequencyMap = {}
    for transaction in tDb:
        for item in transaction:
            if item in frequencyMap.keys():
                frequencyMap[item] += 1
            else :
                frequencyMap[item] = 1
    newFSet = []
    for key in frequencyMap :
        if frequencyMap[key] >= minSupport :
            newSet = []
            newSet.append(key)
            newFSet.append(newSet)

    userFrequencySet.append(newFSet)

# this function generates the catesian cross product of the Fk] and F[0]

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

# This function filters sequenced item sets that do not meet the minimum support

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

# this function generates the cross product for sequenced transactions
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

# this function filters out nonsequenced item sets that don't meet the support
def doFilter(c_k) :
    frequencyCount = {}
    f_k = []
    for transaction in tDb:
        # if any item is not in c_k then do not increment the frequency count
        for index, cset in enumerate(c_k) :
            incrementFrequency = True
            for item in cset :
                if item not in transaction:
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

###################
# Begin Driver code
###################
minSupport = int(input("Enter the minimum support : "))
kValue = int(input("Enter the k value to show the sequence\
    frequency set for the list of users: "))
kValue1 = int(input("Enter the k value to show the non sequence \
    frequency set for the list of users: "))
userListsequenceDb = [ ]
userListnonsequenceDb = []

for user in userTransactions:
    # here we pass in the userTransactions dict one entry at a time
    tDb = list(userTransactions[user])
    nonSequenceF = []
    generateF_0(nonSequenceF)
    k = 0

    # Here is the non-sequence Apriori call for each user
    while len(nonSequenceF[k]) != 0 :
        c_k = generateProduct(nonSequenceF[k],nonSequenceF[0])
        element = doFilter(c_k)
        nonSequenceF.append(element)
        k = k+1
    if kValue1 < len(nonSequenceF) :
        userListnonsequenceDb.append(nonSequenceF[kValue1])

    sequenceF = []
    generateF_0(sequenceF)
    k = 0
    # Generating the sequence set Apriori call for each user
    while len(sequenceF[k]) != 0 :
        sequenceF.append(generateSequenceProduct(sequenceF[k],sequenceF[0]))
        k = k +1

    if kValue < len(sequenceF) :
        userListsequenceDb.append(sequenceF[kValue1])
    print("Sequence F[k] for user " + str(user) + " : ")
    print(sequenceF)

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

# this is where I find the most sommon occurence of items sets
# purchased among all user transactions
hiscore = Counter()
for transaction in transactions:
    combos = combinations(transaction, minSupport)
    for c in combos:
        if hiscore.get(c):
            hiscore[c] += 1
        else:
            hiscore[c] = 1

print(f'most common combination among all users: {hiscore.most_common(1)}')