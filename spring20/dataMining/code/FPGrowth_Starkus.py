# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:40:19 2019

@author: tjsta
"""

growthFile = open("transactionDb.txt","r")

data = []

# Create the unorganized data
for line in growthFile :
    lineCharArray = line.strip('\n').split(',')
    lineArray = []
    for element in lineCharArray :
        lineArray.append(int(element))
	
    data.append(lineArray)
    
#print(data)

tree = data

minsup = 2

frequencyMap = {}
# Organize the tree
for transactions in data :
    #print(transactions)
    for item in transactions :
        #print(item)
        if item in frequencyMap.keys() :
            frequencyMap[item] += 1 
        else :
            frequencyMap[item] = 1

print("frequencyMap " + str(frequencyMap))
print()
sortedFreq = sorted(frequencyMap, key=frequencyMap.get)
print("Sorted frequencyMap keys (ascending) " + str(sortedFreq))
print()

# Removing items below minimum support
for transactions in tree :
    for index,items in enumerate(transactions) :
        for elements in frequencyMap :
            #print(frequencyMap[elements])
            if frequencyMap[elements] <= 2 and elements in transactions : 
                #print(transactions)
                transactions.remove(elements)
                #print(transactions)
                
#print()
#print()
#print()            

# What I want to do here is if the transaction has 3, put 3 at the beginning and move on
# I think I should start with the lowest and pop to the front

for tIndex,transaction in enumerate(tree) :
    for sElements in sortedFreq :
        #print("ok")
        for index,tElements in enumerate(transaction) :
            #print(index)
            if str(sElements) == str(tElements) :
                #print(sElements)
                tree[tIndex].pop(index)
                #transaction.pop(index)
                tree[tIndex].insert(0,tElements)
                #transaction.insert(0,tElements)
                #print(transaction)
                #print()
                
print("Sorted data " + str(tree))
print()
    
# Creating the adjacencyMap
adjacencyMap = {}
adjacencyMatrix = []
for i,transaction in enumerate(tree) :
    for element in transaction : 
        adjacencyMap[element] = []

#print(adjacencyMap)   
    
for n,transactions in enumerate(tree) :
    for x,elements in enumerate(transactions) :
        if x != (len(transactions)-1) :
            adjacencyMap[elements].insert(0,transactions[x+1])
            # removes duplicates
            adjacencyMap[elements] = list(set(adjacencyMap[elements]))
    
print("adjacencyMap "+ str(adjacencyMap))
print()

# creating associationMap
associationMap = {}
for i,transaction in enumerate(tree) :
    for element in transaction : 
        associationMap[element] = []

#print(associationMap)

for n,transactions in enumerate(tree) :
    #print(transactions)
    for x,elements in enumerate(transactions) :
        if elements in transactions :
            associationMap[elements].extend(transactions)
            associationMap[elements] = list(set(associationMap[elements]))
            associationMap[elements].remove(elements)

print("My data is bad for the associationMap because the remaining numbers")     
print("after minimum support all happen to be associated with each other.")
print()
print("The code does generate an associationMap properly on the data.")   
print()
print("associationMap " + str(associationMap))
        






















