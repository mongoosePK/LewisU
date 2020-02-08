// File vector_exploration.cpp

#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <sys\timeb.h>

using namespace std;

long timediff(clock_t t1, clock_t t2);

int main ()
{
    int const size = 500000;
		
	struct timeb start, end;
    int diff;
    
	int k;
	int a[size];
	int vasize = size;
	vector <int> va(vasize);
	
     
	ftime(&start); // time when it starts

    for (k = 0; k < size; k ++)
    {
    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;

    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;
		a[k] = 17;
    	a[k] = 17;

    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;

    	a[k] = 17;
    	a[k] = 17;
    	a[k] = 17;
		a[k] = 17;
    	a[k] = 50;
    }
    cout << "\nsee if assignment is effective ...  a[5] = " << a[5] << " a[size - 1] = " <<  a[size - 1] << endl;
    

    ftime(&end);	// recordts the time at the end 
    
   	diff = (int) (1000.0 * (end.time - start.time)
        + (int)(end.millitm - start.millitm));
        
   	printf("\nArray Operations took %u milliseconds\n\n", diff);

    ftime(&start); // time when it starts

    int * ap;
	int * lastap = &a[size - 1];
	k = 0;
	for (ap = &a[0]; ap <= lastap; ap ++)
    {
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
	    	
		*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	
    	    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
	    	
		*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 17;
    	*ap = 18;
    	
    }
    cout << "\nsee if assignment is effective ...  a[5] = " << a[5] << " a[size - 1] = " <<  a[size - 1] << endl;
    ftime(&end);	// recordts the time at the end 
    
   	diff = (int) (1000.0 * (end.time - start.time)
        + (int)(end.millitm - start.millitm));
        
   	
	
	printf("\nArray Operations with ptrs took %u milliseconds\n\n", diff);
   	
    ftime(&start); // time when it starts
   	
    // index range is unchecked
    cout << "indexe is not checked: value at index "<< size << "\n";
	va[size] = 33;
    cout << va[size]<<".....\n\n";
	
	for (k = 0; k < size; k ++)
    {
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;

    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;

    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 17;
    	va[k] = 19;

    } 
	cout << "\nsee if assignment is effective ... va[5] = " << va[5] << " va[size - 1] = " <<  va[size - 1] << endl;  	
    ftime(&end);	// recordts the time at the end 
    
   	diff = (int) (1000.0 * (end.time - start.time)
        + (int)(end.millitm - start.millitm));
        
   	printf("\nVector Operations took %u milliseconds\n\n", diff);
   	
   	// We find the time it takes to perform simple assignment, use at() method on vector elements

	ftime(&start); // time when it starts
	
	// checked assignment for boundaries:	
	va.at(size-5) = 33;
    cout << va.at(size-5) <<".....\n";

	for (k = 0; k < size; k ++)
    {
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;

    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;

    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 17;
    	va.at(k) = 20;
    } 
cout << " va[5] = " << va[5] << " va[size - 1] = " <<  a[size - 1] << endl;
	   
	ftime(&end);	// records the time at the end 
    
   	diff = (int) (1000.0 * (end.time - start.time)
        + (int)(end.millitm - start.millitm));
        
   	printf("\nVector Operations using at() method took %u milliseconds\n\n", diff);
	
   	cout << "enter an integer to terminate\n";
   	int awaits;
   	cin >> awaits;
	
	return 0;
	
}
/*


see if assignment is effective ...  a[5] = 17 a[size - 1] = 17

Array Operations took 10 milliseconds


see if assignment is effective ...  a[5] = 17 a[size - 1] = 17

Array Operations with ptrs took 6 milliseconds

indexe is not checked: value at index 500000
33.....


see if assignment is effective ... va[5] = 17 va[size - 1] = 17

Vector Operations took 49 milliseconds

33.....
 va[5] = 17 va[size - 1] = 17

Vector Operations using at() method took 121 milliseconds

enter an integer to terminate
5

--------------------------------
Process exited after 40.53 seconds with return value 0
Press any key to continue . . .


