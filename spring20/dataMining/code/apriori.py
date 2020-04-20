# apriori.py
# William Pulkownik
# my version of the apriori project for data mining

import random
import pandas as pd
import itertools
from itertools import combinations
from collections import defaultdict
#formatting options for pandas
pd.set_option("display.max_rows", None, "display.max_columns", None)

# this block reads csv into a dataframe, drops NaN, and creates a list  
data = pd.read_csv('data/transactionList.csv',header=None)
data = data.dropna(axis='columns')
transactions = data.values.tolist()

#create dict of lists to store all transactions by user for every 10 transactions
userTransactions = defaultdict(list)
new_user=0
for index, transaction in enumerate(transactions):
    if index % 10 == 0:
        new_user += 1
    userTransactions[new_user].append(transaction)
for i in range(1,11):
    print(f'User {i}:\n {userTransactions[i]}\n')

def generateF_0(userFrequencySet):
    frequencyMap = {}
    for transaction in transactions:
        for item in transaction:
            if item in frequencyMap.keys():
                frequencyMap[item] += 1
            else :
                frequencyMap[item] = 1
    newFSet = []
    for key in frequencyMap :
        # print(key,frequencyMap[key])
        if frequencyMap[key] >= minSupport :
            newSet = []
            newSet.append(key)
            newFSet.append(newSet)

    userFrequencySet.append(newFSet)

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
    for transaction in userTransactions :
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
    for transaction in userTransactions :
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


minSupport = int(input("Enter the minimum support : "))
kValue = int(input("Enter the k value to show the sequence \
    frequency set for the list of users: "))
kValue1 = int(input("Enter the k value to show the non sequence \
    frequency set for the list of users: "))
userListsequenceDb = [ ]
userListnonsequenceDb = []
for user in userTransactions:
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

# temp = defaultdict(list)
# for i in range(1,len(userTransactions)+1):
#     for j in userTransactions[i]:
#         combos = combinations(j,3)
#         for c in combos:
#             if temp.get(c):
#                 temp[c] += 1
#             else:
#                 temp[c] = 1
#     #comboList.append(temp)
# combodf = pd.DataFrame(columns=['itemSet','support'])

# key = ','.join(map(str,c))
#     frequencies = pd.DataFrame(temp, columns=['itemSet', 'support'])
#     return frequencies