// File testSort.Incomplete.cpp

// algorithm: bubbleSort

/* 1. In a sorted list in ascending order:
      
	    If i < j then a[i] <= a[j], for any i, j, indexes of the array
	      
	2. In a sorted list in ascending order:
	
		(2) for all values of i, a[i] <= a[i + 1].
		
	3. We could put in order the array by taking pairs where (2) is not true
	
		we switch the values so (2) becomes true
		
	4. Step 3 is done by making i = 0, 1, 2, ... size - 2, making the switch if
 
		(2) is not true
		
	5. Step 4 is done until	making i = 0, 1, 2, ... size - 2, no switch  is done,
	
		i.e., (2) becomes true, te sort is done.
		
*/
#include <iostream>
void sort (int x[], int size);
using namespace std;
int main ()
{
    const int size = 20; 
    int a[size];
    a[0] = 1;
    a[1] = 2;
    a[2] = 3;
    cout << "\nBefore Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
	
	sort (a, 3);
    
    cout << "\nAfter Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    
    a[0] = 3;
    a[1] = 2;
    a[2] = 1;
    
    cout << "\nBefore Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    
    sort (a, 3);
    
    cout << "\nAfter Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    
    a[0] = 20;
    a[1] = 30;
    a[2] = -50;
    
    cout << "\nBefore Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    
    sort (a, 3);
    
    cout << "\nAfter Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    
}
int temp;
void sort (int x[], int size)
{
    bool switch_on = true; // a[] is not sorted 
	while (switch_on) 
	{
	    // set the switch correctly:
		
		switch_on = true;	
	    
	    for (int i = 0; i <= size - 2; i++) 
	    {
	      if (x[i] > x[i + 1])
	      {  
		  //interchange values and set switch_on correctly;
	         
          }
		}
	    
    }
}