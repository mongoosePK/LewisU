/* 
Author: Matt Weiss
Date: 3/30/16
File: DynMem.cpp
Descr: In class example tot demonstrate the use of 
dynamic memory allocation and deallocation
*/

#include <iostream>
#include <iomanip>
using namespace std;


void displayArray(const int *,const int );
int *copyArray(const int *source, const int size);

int main() {
	int size;
	int *iptr1 = new int();
	int *iptr2 = new int(15);
	// check for memory allocation errors
	if(iptr1 == nullptr || iptr2 == nullptr) {
		cerr << "Error allocating memory!" << endl;
		exit(-1);
	}

	cout << "Enter an initial integer value to store: ";
	cin >> *iptr1;
	cout << "Enter a size for a dynamic array: ";
	cin >> size;
	// allocated the dynamic array
	int *iarrptr = new int[size];
	if( iarrptr == nullptr) {
		cerr << "Error allocating memory for array!" << endl;
		exit(2);
	}
	for(int cntr = 0; cntr < size; cntr++) {
		cout << "\tInteger value " << cntr << ": ";
		cin >> iarrptr[cntr];
	}


	// display values
	cout << "*iptr1 = " << *iptr1 << endl;
	cout << "*iptr2 = " << *iptr2 << endl;
	displayArray(iarrptr, size);
	// copy and display copy
	int *icopy = copyArray(iarrptr, size);
	displayArray(icopy, size);

	

	// free allocated memory
	delete iptr1, iptr2;
	delete [] iarrptr;
	delete [] icopy;
	return 0;
}

void displayArray(const int* arr, const int size) {
	cout << "\nArray: ";
	for(int cntr = 0; cntr < size; cntr++) {
		cout << arr[cntr] << " ";
	}
	cout << endl;
}

int *copyArray(const int *source, const int size) {
	// create a new array
	int *target = new int[size];
	if(target != nullptr) {
		for(int i =0; i < size; i++) {
			target[i] = source[i]; //*(source + i);
		}
	}
	return target;
}

/*Enter an initial integer value to store: 5
Enter a size for a dynamic array: 10
        Integer value 0: 1
        Integer value 1: 2
        Integer value 2: 3
        Integer value 3: 4
        Integer value 4: 5
        Integer value 5: 6
        Integer value 6: 7
        Integer value 7: 8
        Integer value 8: 9
        Integer value 9: 0
*iptr1 = 5
*iptr2 = 15

Array: 1 2 3 4 5 6 7 8 9 0

Array: 1 2 3 4 5 6 7 8 9 0
Press any key to continue . . .*/
/*
int mn() {
	char c = 0xFF;
	cout << "c: " << c << endl;
	for(int i = 32; i > 0; i--) {
		int k = 8;
		for(int j = 8; j > 0; j--) {
			cout << setw(6) << i*k-(8-j)-1 << ":" << c << " ";
			c--;
		}
		k--;
		cout << endl;
	}
	return 0;
}
*/