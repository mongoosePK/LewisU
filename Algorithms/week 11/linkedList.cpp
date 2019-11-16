

//
//     File LinkedList.cpp
//
# include <iostream>
# include <stdlib.h>
# include <stdexcept>
# include <string>

using namespace std;

template<typename T>
class Node
{
public:
	T element;     // Element contained in the node
	Node<T> *next; // Pointer to the next node
	
	Node()         // no-argument constructor
	{
		next = NULL;
	}
	
	Node(T element) //constructor
	{
		this -> element = element;
		next = NULL;
	}
		
};

template<typename T>
class Iterator/*: public std::iterator <std :: forward_iterator_tag, T>*/
{
public:
		Iterator(Node<T> *p)
		{
			current = p;
		};
		
		Iterator operator++()
		{
			current = current -> next;
			return *this;
		}
		
		Iterator operator++(int)
		{
			Iterator old = *this;
			current = current -> next;
			return old;
		}
		
		T &operator*()
		{
			return current -> element;
		}
		
		bool operator == (const Iterator<T> &iterator)
		{
			return current == iterator.current;
		}		
		
		
		bool operator != (const Iterator<T> &iterator)
		{
			return current != iterator.current;
		}
private:
		Node<T> *current;
};

template<typename T>
class LinkedList
{
public:
		LinkedList();
		LinkedList(LinkedList<T> &list);
		~LinkedList();
		
		void addFirst(T element);
		void addLast(T element);		
		T getFirst() const;
		
		T getLast() const;
		T removeFirst() throw (runtime_error);
		T removeLast();
		void add(T elelemt);		
		void add(int index, T element);
		
		void clear();
		bool contains(T element) const;
		T get(int index) const;
		T indexOf(T element) const;
		bool isEmpty()const;
		
		int LastIndexOf(T element) const;
		void remove(T element);
		int getSize() const;
		T removeAt(int index);
		T set(int index, T element);
		
		Iterator<T> begin()
		{
			return Iterator <T> (head);
		};
		
		Iterator<T> end()
		{
			return Iterator <T> (tail -> next);
		};
private:
	    Node<T> *head, *tail;
	    int size;
};

template<typename T>
LinkedList<T>::LinkedList()
{
	    head = tail = NULL;
	    size = 0;
}

template<typename T>
int LinkedList<T>::getSize() const
{
		return size;
}

template<typename T>
LinkedList<T>::LinkedList(LinkedList<T> &list) // copy constructor
{	   
		head = tail = NULL;
		size = 0;
		Node<T> *current = list.head;
		while (current != NULL)
		{
			this -> add(current -> element);
			current = current -> next;
		}
}

template<typename T>
LinkedList<T>::~LinkedList()
{
	     clear();
}

template<typename T>
void LinkedList<T>::clear()
{
		while (head != NULL)
		{
			Node<T> *temp = head;
			head = head -> next;
			delete temp;
		}
		tail = NULL;
		
}

template<typename T>
void LinkedList<T>::add(T element)
{
	     addLast(element);
}

template<typename T>
void LinkedList<T>::addLast(T element)
{
         if (tail == NULL)
		 {
		 	head = tail = new Node<T>(element);
		 }
		 else
		 {
		 	tail -> next = new Node<T>(element);
		 	tail = tail -> next;
		 }	 
		 
		 size ++;
}

template<typename T>
T LinkedList<T>:: getLast() const
{
		if (size == 0)
			throw runtime_error("index out of range");
		else
			return tail->element;
}
template<typename T>
T LinkedList<T>:: getFirst() const
{
	    if (size ==0)
	    	throw runtime_error("List is Empty");
	    else
	    	return head -> element;
	    	
}
typedef struct 
	{
	 char first [30]; 
	 char last [30];
	 char grade [2];
	} Student;

int main (void)
{
	
	// A new object defined to hold int type elements:
	
	
	LinkedList<int> myListInt;
	
	cout << "\n\nmyListInt object is defined to hold int type elements \n";
	
	cout << "\nBefore addLast, myListInt.size() is: "
	     << myListInt.getSize() << endl;
	
	myListInt.addLast(1);
	cout << "\nLast is: " <<myListInt.getLast()<<endl;
	
	myListInt.addLast(2);
	cout << "\nLast is: " <<myListInt.getLast()<<endl;

	myListInt.addLast(3);
	cout << "\nLast is: " <<myListInt.getLast()<<endl;
	
	myListInt.addLast(4);
	cout << "\nLast is: " <<myListInt.getLast()<<endl;
	
	
	cout << "\nAfter addLast, myListInt.size() is: "
	     << myListInt.getSize() << endl;
	     
	cout << "\nmyListInt.getFirst(): " <<  myListInt.getFirst() << endl;
	cout << "\nmyListInt.getLast() " << myListInt.getLast() <<endl;
	
	   
	int k =0;
	for (Iterator<int> iterator = myListInt.begin();
	     iterator != myListInt.end();
		 iterator ++)
	     {
	     	cout << " in the loop " << k << "element " << *iterator << endl;
			k ++; 
	     } 
	
	// A new Linked ist object defined to hold double type elements:
	
	cout << "\n\nA new Linked List object is defined to hold double type elements";
	cout << "\n----------------------------------------------------------------";
	LinkedList<double> myListDouble;
	
	cout << "\n\nmyListDouble object is defined \n";
	
	cout << "\nBefore addLast, myListDouble.size() is: "
	     << myListDouble.getSize() << endl;
	
	myListDouble.addLast(1.5);
	cout << "\nLast is: " <<myListDouble.getLast()<<endl;
	
	myListDouble.addLast(2.5);
	cout << "\nLast is: " <<myListDouble.getLast()<<endl;

	/*
    Continue the main similar to the int type T template:

	*/ 
	
	// A new Linked ist object defined to hold student type elements:
	
	cout << "\n\nA new Linked List object is defined to hold student type elements";
	cout << "\n----------------------------------------------------------------";
	/*
	
	LinkedList<Student> myListS;
	
	myListS.addLast("John" "Smith" "A");
	*/
	
	
	return 0;

}




