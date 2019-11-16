// File listANDnodes.cpp
/*
	This program is a sample of simple concepts used to define
	nodes and lists of nodes in C++;
	
*/
#include <iostream>

using namespace std;

int main (void)
{
	int a =5;
	
	cout << "\n\nvalue of a is: " << a << endl;
	
	int* ptr_a; // define pointer ptr_a
	ptr_a = &a; // store in ptr_a the address of a as integer;
	
	// --- 1. We can use the address of a or a as identifyer.
	
	cout << "value of a is: " << a << " and *ptr_a is: " << *ptr_a << endl;
	cout << "\n\n" << "ptr_a  value is "<< ptr_a << " and value is " << *ptr_a << endl;
	
	int* b;
	b = ptr_a;
	
	cout << "\n(why 1) Contents of b is : " << b << " why why why " << endl;
	
	cout << "\n\n(why 2) Address in variable b points to an integer whose value is: " << *b << "  why why why " << endl << endl;
	
	// --- 2. Space allocated using declarations or we could use dynamic allocation
	
	int* A_ptr;
	A_ptr = new int;
	*A_ptr= 25;
	cout << A_ptr << " " << *A_ptr;
	
	struct student_record
	{
		int student_id;
		char name [30];
		char grade;
		student_record * next;
	};
	
	// --- 3. Create a dynamic variable of type  student_record
	
	student_record *s_ptr;
	s_ptr = new student_record;
	if (s_ptr == NULL)
		{
			cout << "\nBIG Problem! s_ptr is NULL, no space allocated";
			return(1);
		}
	else
		{
			cout << "\nALLOCATION Successful";
		}
	//
	
	cout << "\nEnter studen name, use _ for name, eg. John_Smith: ";
	cin >> s_ptr -> name;
	cout << "\nEnter student id, id is an integer: "; 
	cin >> s_ptr -> student_id;
	cout << "\nEnter grade, A, B, C, D, F allowed: ";
	cin >> s_ptr -> grade;
	s_ptr -> next = NULL;
	
	cout << "\nRecord Entered: " << s_ptr -> name <<", " << s_ptr -> student_id << ", " << s_ptr -> grade << endl;
	
	// --- 4 Change the code to enter two student records and link the second record to the first:
	
	
	
	return(0);
	
}
