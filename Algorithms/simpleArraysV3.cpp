// File name: simpleArraysV3.cpp

// Properties:
// 1. All elements of a C++ array are the same
// 2. C++ does not check array's boundary. Check that the subscripts are
//    within the range

#include <iostream>
#include <stdlib.h>


using namespace std;

void DisplayArray(int x[], int size);
void InitArray (int x[], int size, int value);
int MaxArray (int x[], int size);
int MinArray (int x[], int size);
void bubbleSort (int x[], int size);
void swap (int* x, int* y);

const int INIT_VAL = 0;
int main ()
{
    cout <<"\n\nThis program tests functions designed to access arrays of integers. Welcome!\n\n";
    
	// We define an array a[]

	const int A_SIZE = 256;      
    int a[A_SIZE];  // This defines an array of A_SIZE, i.e., 256 integers
                    // Elements are starting at a[0] ... a[A_SIZE - 1]
                    // e.g., a[5] is the sixth element of the
                    // array.
                    
    // Init array a[] with value 0

	InitArray (a, A_SIZE, INIT_VAL);	    
    
    // Read in from the console the array
    
    // Display the array a[]
    

	// DisplayArray(a, A_SIZE);
    	
    // Make the sum of all elements of the array a[]
    
    // Calculate the max of array a[]
    
    a[0] = 3;
    a[1] = 7;
    a[2] = -2;
    a[3] = 52;
    a[4] = -5;
    
    DisplayArray(a, 10);
    bubbleSort(a,10);
    cout << "\nMax of array a[] of 5 elements is " <<MaxArray (a, 5);
    cout << "\nMin of array a[] of 5 elements is " <<MinArray (a, 5);
    cout << "\nthe sorted array is";
    DisplayArray(a, 10); 

    // Calculate the min of array a[]
    
    // Sort in descending order a[]
    
    // Sort in ascending order a[]
    
    // Test the above for arrays b[] of B_SIZE
    
    
    cout << endl <<endl;
    system ("PAUSE")
    return 0;
      
}

void swap (int* x, int* y)
{
    int temp = *x;
    *x = *y;
    *y = temp; 
}

void bubbleSort (int x[], int size)
{
    bool flag = true;
    while (flag)
    {
        for (int i=0;i<size-1;i++)
        {
            flag = false;
            if (x[i]< x[i+1])
            {
                swap(x[i],x[i+1]);
                flag = true;
            }
        }
    } 

}

void InitArray (int x[], int size, int value)
{
    for (int i = 0; i < size; i++)
    
    	x[i] = value;
}

void DisplayArray(int x[], int size)
{
    cout << "\nContents of the array of size " << size << endl;
    
    for (int i = 0; i < size; i++)
    {
    	
		if (i % 5 == 0)
  		{
  			
  			cout << "\n  " << i << " -->" << " \t" ;
 			
        
		}
		cout <<  x[i] << "  " ;
    }
	cout << endl; 
}
int MaxArray (int x[], int size)
{	
	int maxval = x[0];
	for (int k = 1; k < size; k++)
		if (x[k] > maxval)
		   maxval = x[k];
	return maxval; 
}

int MinArray (int x[], int size)
{	
	int minval = x[0];
	for (int k = 1; k < size; k++)
		if (x[k] < minval)
		   minval = x[k];
	return minval; 
}