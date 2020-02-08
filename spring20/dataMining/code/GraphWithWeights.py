#

nodeList = ['a', 'b','c','d','e','f','g']

connectivityList = 
[

    {'a' : [['e',1],['d',3],['b',2]]},
    {'b' : [['a',2],['c',2]]},
    {'c' : [['b',2],['d',3],['g',1]]},
    {'d' : [['f',2],['a',3],['c',1]},['g,'3]]},
    {'e' : [['f',5],['a',1]]},
    {'f' : [['e',5],['d',2]]},
    {'g' : [['d',3],['c',1]]}
   
]

class Node :
    def Node(self,value,neighbors, distance) :
        #NEIGHBORS is the dict of neighbor nodes and weights
        #id is the node value
        self.id = value
        self.neighbors
        self.dist = distance

# apply the shortest path algorithm

S = []
V = copy.deepcopy(nodeList)
S.appendnodeList.pop(0))

print(S)
print(V)

a = [['a',5], ['b',6]]
neighborlist =['a', 'b']
weightList = [5,6]
while len(S) < len(nodeList) :
    #iterate over all nodes in S
    minDistance = 10000
    foundNode = -1 #-1 when unassigned
    for nodeElement in S :
        sNode = nodeElement.id
        for vNode in V : 
            # Check if vNode's neighbors include sNode
            for neighbors in vNode.neighbors:
                #create a neighborlist from neighbors
                #create a weight list from neighbors
                if (neighbor[0] == sNode) :
                    distance = sNode.dist + neighbor[1]
                    if distance is less than minDistance : 
                        # mark this node with foundnode
                        #mark the node, assign distance to minDistance 
                