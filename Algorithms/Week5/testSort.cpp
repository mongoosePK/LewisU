// William Pulkownik
// 10 OCT 2019
//
// File: testSort.cpp
// algorithm: bubbleSort and some chrono functions to time the sort
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
#include <chrono> //clock functions and nanosecond conversions

using namespace std;
using namespace std::chrono; //std::high_resolution_clock, std::nanoseconds

void sort (int x[], int size);


int main ()
{
    cout << "This thing sorts arrays in descending order! \n";
    const int size = 20; 
    int a[size];
    a[0] = 1;
    a[1] = 2;
    a[2] = 3;

    cout << "\nBefore Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;

    auto start = high_resolution_clock::now();
	sort (a, 3);
    auto stop = high_resolution_clock::now();
	auto difference = duration_cast<nanoseconds>(stop - start);
    // NOTE the .count() function is a member of chrono
	cout << "Actual time of work is: " << difference.count() << " nanoseconds";
    
    cout << "\nAfter Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    a[0] = 3;
    a[1] = 2;
    a[2] = 1;
    cout << "\nBefore Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;

    auto start1 = high_resolution_clock::now();
	sort (a, 3);
    auto stop1 = high_resolution_clock::now();
	auto difference1 = duration_cast<nanoseconds>(stop1 - start1);
	cout << "Actual time of work is: " << difference1.count() << " nanoseconds";

    cout << "\nAfter Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    a[0] = 20;
    a[1] = 30;
    a[2] = -50;
    cout << "\nBefore Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;
    
    auto start2 = high_resolution_clock::now();
	sort (a, 3);
    auto stop2 = high_resolution_clock::now();
	auto difference2 = duration_cast<nanoseconds>(stop2 - start2);
	cout << "Actual time of work is: " << difference2.count() << " nanoseconds";

    cout << "\nAfter Sort  " << a[0] << " " << a[1] << " " << a[2] << endl;    
}

void sort (int x[], int size)
{
    // bool switch_on = true; // a[] is not sorted 
	bool flag = true;
    // outter loop through the array n times and test for flag condition
    for (int i=0; i<size && flag; i++)
    {
        flag = false;
        // loop through array n-1 times. If x[j] < the next element, swap.
        for (int j=0; j< size-1 ; j++)
            if (x[j]> x[j+1])
            {
                swap(x[j],x[j+1]);
                flag = true; //work is truth
            }
            
    }
}

/* 

HERE IS SOME SAMPLE OUTPUT
-----
This thing sorts arrays in descending order! 

Before Sort  1 2 3
Actual time of work is: 138 nanoseconds
After Sort  1 2 3

Before Sort  3 2 1
Actual time of work is: 194 nanoseconds
After Sort  1 2 3

Before Sort  20 30 -50
Actual time of work is: 122 nanoseconds
After Sort  -50 20 30
-----

mongoose@mongooseP:~/School/LewisU/Algorithms/Week5$ ./testSort 
This thing sorts arrays in descending order! 

Before Sort  1 2 3
Actual time of work is: 681 nanoseconds
After Sort  1 2 3

Before Sort  3 2 1
Actual time of work is: 617 nanoseconds
After Sort  1 2 3

Before Sort  20 30 -50
Actual time of work is: 408 nanoseconds
After Sort  -50 20 30
----

mongoose@mongooseP:~/School/LewisU/Algorithms/Week5$ ./testSort 
This thing sorts arrays in descending order! 

Before Sort  1 2 3
Actual time of work is: 511 nanoseconds
After Sort  1 2 3

Before Sort  3 2 1
Actual time of work is: 481 nanoseconds
After Sort  1 2 3

Before Sort  20 30 -50
Actual time of work is: 321 nanoseconds
After Sort  -50 20 30

---------

This thing sorts arrays in descending order! 

Before Sort  1 2 3
Actual time of work is: 241 nanoseconds
After Sort  1 2 3

Before Sort  3 2 1
Actual time of work is: 212 nanoseconds
After Sort  1 2 3

Before Sort  20 30 -50
Actual time of work is: 140 nanoseconds
After Sort  -50 20 30
*/