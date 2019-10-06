// file cppArrays.cpp
// Author: P. Turcu
// Demo the definition, initializes, read, displays, sums, array
// Uses functions with arrays as arguments.
// Note that the array passing is done by reference.

#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {

	cout << "Hello ... we are going to experiment with arrays !!\n\n";

	int a[3]; // an integer type array is declared, for 3 elements
	          // elelemnts with index 0, 1 and 2 are defined
	// sizeof (a) gives the size of the array

	double b;

	cout << "\n size of a[] is " << sizeof(a) << endl;

	a[0] =5;

	cout << "\n enter number  2 " <<endl;

	int i;

	cin >> i;

	cout << "\n value of a[0] is "<< a[0] << endl;

	cout << "\n a[1 + i] is " << a [1 + i] << endl; // element with index 1+i does not exist.

	a[i + 1] = 25;

	cout << "\n a[1+i] is " << a[1+i] << endl;
	{
    int array[2];
    array[0] = 1;
    array[1] = 2;
    array[3] = 3;
    array[4] = 4;
    cout << array[3] << endl;
    cout << array[4] << endl;
	}
	return 0;
}