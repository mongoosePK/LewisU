
import random

tDb = []
frequencyMap = {}
minSupport = 2

# Create or read in the database
for i in range(5) :
    transaction = random.sample(range(0,10),5)
    tDb.append(transaction)


# Generate the F[0]
def generateMap() :
    # Create a frequency set - F[0]
   
    for transaction in tDb :
        for item in transaction :
            if item in frequencyMap.keys() :
                frequencyMap[item] += 1
            else :
                frequencyMap[item] = 1

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




# 3  - Creating the sorted transactions
generateMap()

sortedTransactions = []
for transaction in tDb :
    newTransaction = sortUnique(transaction)
    sortedTransactions.append(newTransaction)


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
        else :
            newPath = parent.path.copy()
            newPath.append(transaction[childIndex])
            children = []
            # childIndex +1 is the new child
            newNode = Node(newPath,children,transaction[childIndex],1)
            parent.children.append(newNode)
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
    


def traverseTree(node) :

    # Minimum support of 2, for associations greater than 2
    if node.frequency > 1 and len(node.path) > 2 :
        print("Path %s  frequency %d " % (node.path,node.frequency))

    if len(node.children) == 0 :
        return

    for child in node.children :
        traverseTree(child)
                    
for transaction in sortedTransactions :
    # We building our FPgrowth tree, through each transaction
    addToTree(transaction,headNode,0)


#Travers the tree to find the associations

traverseTree(headNode)



