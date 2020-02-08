// binarySearchV2.cpp
#include <iostream>

// an array of size length sorted in ascending order
// the function returns bool , true if it finds the item, and false otherwise.
// Also find the index in the array if returns true, -1 otherwise.

using namespace std;
bool findbin_search(int item, int a[], int size, int & index_found)
{
     index_found = -1;
     int first = 0;
 	 int last = size - 1;
 	 int middle = (last + first)/2;
 	 int count = 0;
 	 bool found = false;
 	 while (!found && (last >= first))
 	 { 
	   if (item == a[middle])
	   {
		  count++;
	   	  found = true;	   
	   }
       else if (item < a[middle])
       {     
	   		 count++;
	   		 last = middle -1;
	   		 middle = (last + first)/2;
       } 
       else // item > a [middle]
       {
	         count++;
	         first = middle + 1;
	         middle = (last + first)/2;
       }
       
     } 
     
	 if (found)
	 {
	 	index_found = middle;
	 	cout << "Performed " << count << " comparisons\n";
     } 
	 return found; 
 }
 
 int main()
 {
    cout << "\nEnter size of the array:";
    int size;
    cin >> size;
    int *x = new int [size];
    
    if ( x == NULL)
    {  
	   cout << "COULD NOT ALLOCATE .. \n";
       return 1;
       
    }  
    cout << "\nEnter " << size << " integer values in ascending order: ";
    for (int k = 0; k < size; k++)
       cin >> x[k];
    
    cout << "\nEnter integer value to search for: ";
    
	int search_item;
    
	cin >> search_item;

 	int index;
 	
    bool found =  findbin_search(search_item, x, size, index );
 	 
    cout << "found: " << found << " index of found: "<< index << endl;
    
    cout <<"\nThe array is: ";
    for (int k = 0; k < size; k++)
      cout << x[k] << " ";
    cout << endl;
 	return 0;
}
/* Run the program binarySearchV2.cpp:



Enter size of the array:7

Enter 7 integer values in ascending order:
12
14
17
19
28
40
45

Enter integer value to search for: 17
found: 1 index of found: 2

The array is: 12 14 17 19 28 40 45

--------------------------------
Process exited with return value 0
Press any key to continue . . .



Enter size of the array:8

Enter 8 integer values in ascending order: 1
2
3
4
5
6
7
8

Enter integer value to search for: 8
Performed 4 comparisons
found: 1 index of found: 7

The array is: 1 2 3 4 5 6 7 8 
mongoose@goosebox:~/LewisU/Algorithms/finished work$ ./binarySearchV2 

Enter size of the array:9

Enter 9 integer values in ascending order: 0
1
2
3
4
5
6
7
7
8

Enter integer value to search for: 8
Performed 4 comparisons
found: 1 index of found: 8

The array is: 0 1 2 3 4 5 6 7 8 
mongoose@goosebox:~/LewisU/Algorithms/finished work$ ./binarySearchV2 

Enter size of the array:9

Enter 9 integer values in ascending order: 1
2
3
4
5
6
7
8
9

Enter integer value to search for: 9
Performed 4 comparisons
found: 1 index of found: 8

The array is: 1 2 3 4 5 6 7 8 9 

*/




