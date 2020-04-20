import copy

nodeList = [ 'a','b','c','d','e','f','g' ]


connectivityList = [
    { 'a' : [['e',1],['d',3],['b',2]]},
    { 'b' : [['a',2],['c',2]] },
    { 'c' : [['b',2],['d',3],['g',1]]},
    { 'd' : [['f',2],['a',3],['c',1],['g',3 ]] },
    { 'e' : [['f',5],['a',1]] },
    { 'f' : [['e',5],['d',2]]},
    { 'g' : [['d',3],['c',1]] }
]

class Node :
    # Neighbors is the list of neighbor nodes and the weight
    # id is the character value
    def Node(self,value,neighbors,distance) :
        self.id = value
        self.neighbors = neighbors
        self.dist = distance


# Use the connectivityList to make the graph V, we will
# start 'a' as the head node


# Apply the shortes path algorithm
# node has distance ( distance to head node)
# node has a link to the previous node (backNode)

# Assign all of the nodes d -> large number
# Create a set S  - list of shortest path nodes,  add 'a' to the set and the node's distance is 0
# Create a set V - list of nodes that are not shortest path nodes

S = []
V = copy.deepcopy(nodeList)
headNode = nodeList.pop(0)
S.append(Node(headNode,connectivityList[headNode],0))

print(S)
print(V)

a = [ [ 'a',5], ['b', 6] ]
neigborList = [ 'a','b']
weightList = [5,6]

while len(S) < len(nodeList) :
    # Iterate over all the nodes in S
    minDistance = 10000
    foundNode = -1
    for nodeElement in S :
        sNode = nodeElement.id
        # iterate over the element in V
        for vNode in V :
            # Check if the vNode's neighbors include sNode            
            for index,neighbor in enumerate(vNode.neighbors) :
                # [ 'a',5], ['b', 6]
                if (neighbor[0] == sNode) :
                    distance = sNode.dist + neigbor[1]
                    if distance < minDistance :
                        # mark this node ( what is the new id of foundNode)
                        # change minDistance to distance
                        print("hello")






