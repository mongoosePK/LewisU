adjacencyList = [ {1 : [2,3] }, { 2 : [1,4] }, {3 : [4]}, {4 : [3]}]

nodeSize = len(adjacencyList)

visitedNodeList = []
stack = []
class Node:
    def __init__(self,id,color):
        self.id = id
        self.color = color
#we add the head

headNode = Node(1,'red')
stack.append(headNode)
isBiPartite = False

def checkList(currentList, nodeID):
    for element in currentList:
        if element.id == nodeID:
            foundElement = element
            break
    return foundElement

while len(visitedNodeList) < nodeSize:
    currentNode = stack.pop()
    neighborlist = adjacencyList[currentNode]
    # if the cirrent node is in the neighboe list 
    # then it is not a bi-partitw graph, exit loop
    if currentNode in neighborlist:
        isBiPartite = False
        break

    # Check if the neighbors are in the list or stack
    for  neighborNode in neighborlist:
        foundNode = checkList(visitedNodeList, neighborNode.id)
        # return -1 if there is no node within visited list
        isFound = False
        if foundNode != 0:
            isFound = False
            #this node has already been visited
            if neighborNode.color == foundNode.color:
                isBiPartite = False
                break

    if currentNode.color == 'red':
        neighborNode.color = 'black'
    else:
        neighborNode.color = 'red'

    newNode = Node(neighborNode)
    # Adding neighbor to stack
    if isFound == False:
        stack.append(neighborNode)