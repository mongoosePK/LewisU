// ArraysPointersAllocation.cpp
// 

#include <stdlib.h>  // for malloc
#include <stdio.h>
#include <iostream>

using namespace std;

int main (void)
{
//  	Example 1: Definition of Arrays of integers
	
	   	int A[100];  // defines array of integers A[0], A[1], .. A[99]
	   
//	 	Example 2:  A[100] occupies 400 bytes 4 bytes/(1 integer) * 400

		cout << "Storage occupied by int A[100] " << sizeof(A) << endl; 
		
//      Example 3: Definition of arrays of chars (characters

		char B[1000]; // defines array of characters B[0], B[1], ... B[999]
		
				
//      Example 4: B[1000] occupies 1000 bytes, 1 byte per char (it's ASCII not UNICODE)

		cout << "Storage occupied by B[1000] " << sizeof(B) << endl; 
		
//      Example 5: Array A content is the address of A[0], similarly with B

		if (A == &A[0])
			cout << "Indeed A's content is the address of A[0]\n";
		else
		    cout << "Not true\n";
		    
		
		if (B == &B[0])
			cout << "Indeed B's content is the address of B[0]\n";
		else
		    cout << "Not true\n";
		    
//  	int A; is not allowed as a scalar (sinle) variable - reserved to keep the address of A[100]
//             defined before.

//////////////////// POINTERS //////////////////////

//		Example 6: A pointer is a variable which keeps an address. Pointers have type of the object whose address is.

		int * a_ptr;  // a_ptr could have a value of a pointer of integer variable.
		
		int a;
		
		a= 35;
		
		a_ptr = &a;  // &a contains the address of variable a (note & operator) contains 
		
		// *a_ptr can get to the value of a; *a_ptr it is the content pointed by a_ptr
		
		cout << "Value of a is " << a << ", also value of *a_ptr is " << *a_ptr << endl;
		
//		Example 7: 

		A[0] = 56;
		a_ptr = &A[0];
		
		cout << " explain " << A[0] << " " << *A << " " << *a_ptr;
		
//      Example 8: pointers to structures

	    struct DATE{
	    	int day;
	    	int month;
	    	DATE * next;
	    };

		DATE d1, d2, d3;
		
		DATE top;
		
		top.next = NULL;
		
		top.next = &d1;
		d1.next = &d2;
		d2.next = &d3;
		d3.next = NULL;
		
		cout << "\nSize of DATE structure " << sizeof (DATE) << endl;
        for (DATE *p = top.next; p != NULL ; p = p -> next)
		{
			cout << "\nEnter day month of the students, e.g., 1 and 7 for Jan 7:\n";
            cin >> p->day >> p->month;
        }
		 
	    for (DATE *p = top.next; p != NULL ; p = p -> next)
		{
			
            cout << "\ndate: " << p->day << " " << p->month << endl;
        }

//      Example 9: allocate memory: for a variable 


		double* pvalue  = NULL; 
		
		pvalue = new double; // allocates memory from the heap, space for a double pointer by pvalue.
        if(pvalue  == NULL)
        {
            cout << "Error: out of memory." <<endl;
            return 0;

        }
        *pvalue = 2.314;
        cout << "\nValue of the double is " << *pvalue << " address is " << pvalue << endl;
        
        delete (pvalue);
        
        cout << "\nValue of the double delete() is " << *pvalue << " address is " << pvalue << endl;
        
        cout << "\nValue of pvalue after delete() is " << pvalue << endl;
        
        

//      Example 10:  Allocate for an array: new and delete

		int *array_ptr = NULL;
		array_ptr = new int [100];
		
		array_ptr[0] = 12; // 
		
		cout << "\n array_ptr[0] is " << array_ptr[0] << " at address " << array_ptr << endl;
		
		delete (array_ptr);
		
		cout << "\n after delete(), val of array_ptr[0] is " << array_ptr[0] << " at address " << array_ptr << endl;				
		
		array_ptr = new int [100];
		
		array_ptr[0] = 55;
		cout << "\n new allocation, array_ptr[0] is " << array_ptr[0] << " at address " << array_ptr << endl;
		
		delete (array_ptr);
		
		// delete (array_ptr); // frred again, should be in error?
		
		cout << "\n after a second delete(), array_ptr[0] is " << array_ptr[0] << " at address " << array_ptr << endl;
		
//     Example 11:  Allocate for an array: malloc(), free(), reloc()
		
		array_ptr = (int *) malloc(400);  // 400 locations in bytes
		                                  // malloc()returns a pointer to the allocated memory, or NULL if the request fails.
		
		array_ptr[22] = 22;
		
		cout << "\n after malloc(), val of array_ptr[22] is " << array_ptr[22] << " at address " << array_ptr << endl;
		
		free(array_ptr); // frees the memory allocated
		
		cout << "\n after free(), val of array_ptr[22] is " << array_ptr[22] << " at address " << array_ptr << endl;
		
		//free((int *)array_ptr); // frees the memory allocated again, it should be an error
		
		array_ptr = (int *) malloc(400);  // 100 locations in bytes
		
		if (array_ptr == NULL)
            cout << "\nAllocation Failure\n";
            
		cout << "\n after free(), malloc() array_ptr : " << array_ptr << endl;
		
		array_ptr[2] = 2;
		array_ptr [99] = 99;
		
	    cout << "\nvalue address is " << array_ptr << " values in index 2 and index 99 are " << array_ptr [2] << " and " << array_ptr [99] << endl;
		
		// Reallocating memory
		
        array_ptr = (int *)realloc(array_ptr, 4000);
        
        if (array_ptr == NULL)
            cout << "\nAllocation Failure\n";
        
        
        
        cout << "\nRelocation address is " << array_ptr << " values in index 2 and index 99 are " << array_ptr [2] << " and " << array_ptr [99] << endl;
   
         
		
		return 0;	
}



