# William Pulkownik
# nodes.py
# this python work is for Algorithms and Data Struct
# Fall 2019

#our Node class has a two data members
class Node:
    def __init__(self, info=None, next=None):
        self.info = info # member to hold value
        self.next  = next #member for pointer to next node

    def __str__(self):
        return str(self.info)

# Node instance containing int
node1 = Node (1)
print ("\nnode1 is ", node1)

# Node instance containing string
node2 = Node ("RED")
print ("\nnode2 is ", node2)

# point nodes at each other then print each other's info
node1.next = node2
node2.next = node1
print ("\nnode1.next is ", node1.next)
print ("\nnode2.next is ", node2.next) 

node2.next = None  # make sure the node chain has an end

def print_list(node):
    print ("\n< ", end=" ")
    while node:
        print (node, end=" ")
        node = node.next
           
    print (" >")
    return

#make a new node and place it at the head of the set
node3 = Node("BLUE", node1)

print_list(node3)

print_list(node1)
