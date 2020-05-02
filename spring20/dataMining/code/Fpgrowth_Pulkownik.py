import random
import csv
from collections import Counter, defaultdict

tDb = []
minSupport = 2

with open("transactionDb.csv","r") as csv_file :
    csvReader = csv.reader(csv_file,delimiter=",")
    for line in csvReader :
        transaction = [ int(i) for i in line ]
        tDb.append(transaction)
csv_file.close()


# Generate the F[0]
def generateMap(tDb, minSupport) :
    freqMap = {}
    for transaction in tDb :
        for item in transaction :
            if item in freqMap.keys() :
                freqMap[item] += 1
            else :
                 freqMap[item] = 1
    for key in list(freqMap.keys()):
        if freqMap[key] < minSupport:
            del freqMap[key]
    return freqMap
    
def cut(freq, minSupport):
    for key in list(freq.keys()):
        if freq[key] < minSupport:
            del freq[key]
    return freq
########################################################################
# Order the transactions based on the highest frequency to lowest frequency
# There has to be consistant ordering of the ties

# change the transaction ordering to highest to lowest frequency order
# and have a the consistent ordering for items with the same frequency
def sortUnique(transaction) :

    transactionLength = len(transaction)
    transactionOutput = []
    while len(transactionOutput) < transactionLength :
        maxValue = 0
        candidates = [transaction[0]]
        for index in range(len(transaction)) :
            value = frequencyMap[transaction[index]]

            # Add the item to the candidates if there is a tie
            if value == maxValue :
                candidates.append(transaction[index])
            elif value > maxValue :
                candidates = [transaction[index]]
                maxValue = value
        # Pick the lowest item on our candidate list
        topCandidate = sorted(candidates)[0]
        transactionOutput.append(topCandidate)
        transaction.remove(topCandidate)
    return transactionOutput
########################################################################
# 3  - Creating the sorted transactions
frequencyMap = generateMap(tDb, minSupport)
coverList = {}

sortedTransactions = []
for transaction in tDb :
    newTransaction = sortUnique(transaction)
    sortedTransactions.append(newTransaction)

########################################################################
# Creating the Node data structure for the fpGrowth tree
class Node :
    def __init__(self,p,c,v,f) :
        # The path is the association set
        self.path = p
        # Children are any associations that include
        # this node as the next to last element
        # example Node - [0,5] - Children - [0,5,2],[0,5,3]
        self.children = c
        # item label
        self.value = v
        # Frequency  this is our F[len(path)]
        self.frequency = f
def containedIn(childItem,nodeList) :
    marker = -1
    for index, node in enumerate(nodeList) :
        if node.value == childItem :
            marker = index
    if marker == -1 :
        return marker
    
    return nodeList[marker]

    

def addToPath(pathList, path) :
    found = False
    for i, path in enumerate(pathList):
        for item in pathList:
                coverList[item] = cut(item, minSupport)
    
    # Add more to this function in order to maintain frequency cover for pathList
    # add path to pathList if cover holds

# 4  Generate the FpGrowth tree
headNode = Node([],[],"Head",0)
def addToTree(transaction,parent,childIndex) :
    # If the child index is transaction[childIndex]
    # Want to know if the childNode really a child within
    # the parent's children
    childNode = containedIn(transaction[childIndex],parent.children)
    
    #Base condition when we are at the end of the transaction
    if childIndex == len(transaction) -1 :
        if childNode != -1 :
            # Increasing frequency count of F[len(childNode.path)]
            childNode.frequency += 1
            path = childNode.path
            

            # You only need to modify here in order to add to the frequency cover list
            # Filter based on frequency and association size -- len(path)
            # You are adding the path (association) to the key (first item on the path)
            # remember only add this if the cover holds, and if this path (association)
            # is not contained in any other associations in the set of associations
            # associated with this key
            # use coverList and the addToPath function here
 
        else :
            newPath = parent.path.copy()
            newPath.append(transaction[childIndex])
            children = []
            # childIndex +1 is the new child
            newNode = Node(newPath,children,transaction[childIndex],1)
            newNode.frequency += 1
            parent.children.append(newNode)
            coverList = cut(frequencyMap, minSupport)
            
            temp = coverList
            if temp is not None:
                temp = newNode
                

    
        return

    if childNode != -1 :
        # Increasing frequency count of F[len(childNode.path)]
        childNode.frequency += 1
        addToTree(transaction,childNode,childIndex+1)
    else :
        newPath = parent.path.copy()
        newPath.append(transaction[childIndex])
        children = []
        # childIndex +1 is the new child
        newNode = Node(newPath,children,transaction[childIndex],1)
        parent.children.append(newNode)
        addToTree(transaction,newNode,childIndex+1)
        
        # Do the same procedure of add to the item list here
    
    


def traverseTree(node,outputFile) :

    # Minimum support of 2, for associations greater than 2


    if len(node.children) == 0 :
        if node.frequency > minSupport and len(node.path) > minSupport :
            outputFile.write("Associations %s  frequency %d \n" % (node.path,node.frequency))
        return

    for child in node.children :
        traverseTree(child,outputFile)
                    
for transaction in sortedTransactions :
    # We build our FPgrowth tree, through each transaction

    # each item has its opportunity to add its associations to the FPtree
    for item in frequencyMap.keys() :
        for index, tItem in enumerate(transaction) :
            if item == tItem :
                addToTree(transaction,headNode,index)
                




outputFile = open("Associations.txt","w")
traverseTree(headNode,outputFile)
outputFile.close()

# also print out the coverList map -- the item and the corresponding associations








