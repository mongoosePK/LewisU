class Empty(Exception):
 """ Error attempting to access an element of an empty container."""
 pass
   
class LinkedStack:
  """ LIFO Stack Implementation, uses a single link list for storage """

#---------------- nested _Node class -----------------------
  class _Node:
    __slots__ = '_element', '_next'		# streamline memory usage
    def __init__(self, element, next):  # initialize node's fields 
      	self._element = element			# reference to user's element
      	self._next = next				# reference to next node
      	

#-----------------stack methods ------------------------------
  def __init__(self):    
      self._head = None                # create a head node
      self._size = 0                   # number of stack elements
	  
  def __len__(self):
      return self._size
      
  def is_empty(self):
      return self._size == 0 
	  
  def push(self, e):
      self._head = self._Node(e, self._head)
      self._size += 1;  
	  
  def top(self):
      if self.is_empty():
         raise Empty('Stack is empty') 
      return self._head._element
	  
  def pop(self):
       if self.is_empty():
          raise Empty('Stack is empty')  # print ('Stack is empty')
       answer = self._head._element
       self._head = self._head._next     # bypass the former top node
       self._size -= 1
       return answer  

c = LinkedStack()

print ("\nis c empty\n", c.is_empty())

print ("c._head", c._head)

##print (c.top()) just to see it catches the error

## a grave programming error
c._size = 25

print ("\nc is empty\n", c.is_empty())
 
print ("c._size", c._size)

## 
c._size = 0

print ("\nc is empty\n", c.is_empty())

print ("c._size", c._size)


c.push(25)

print (c)

print ("\nc is empty\n", c.is_empty())

print ("c._size", c._size)

print ("\ntop of stack is ", c.top())

c.push (125)

print ("\ntop of stack is ", c.top())

print ('\n\nc.pop()', c.pop())

print ("\ntop of stack is ", c.top())


