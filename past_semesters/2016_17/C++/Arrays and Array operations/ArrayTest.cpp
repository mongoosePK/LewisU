/*
 FILE:   BinaryFile.cpp
 AUTHOR: William Pulkownik
 DATE:   29 FEB 2016
 DESCR:
 In-class example to show example of 1-D arrays
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void doubleArray(int nums[], int size)
{
	for (int i = 0; i < size;)
		nums[i++] *= 2;
}
void displayArray(int * nums, int size)
{
	for (int i= 0; i < size; i++)
		cout << nums[i] << ' ';
	cout << endl;
}

int main()
{
	const int SIZE = 3;
	int arr1[3];
	int arr2[SIZE];
	int arr3[SIZE] = {1, 2};
	int arr4[] = {1, 2, 3, 4,};
	
	for(int i = 0; i < SIZE; i++)
	{
		cout << "please input an integer: ";
		cin >> arr2[i];
	}
	// or initialize with loop
	//for(int i = 0; i < SIZE; i++)
	//	cout << "Arr2[" << i << "] = " << arr2[i] << endl;
	cout << "contents of arr2..." << endl;
	for(int ival : arr2)
		cout << ival << ' ';
	cout << endl;
	cout << "doubling array2" << endl;
	//double the elements of the array
	doubleArray(arr2, sizeof(arr2)/sizeof(int));
	displayArray(arr2, SIZE);


	return 0;
}