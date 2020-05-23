/*
     FILE:   MDArrFunc.cpp
	 AUTHOR: 
	 DATE:   MM/DD/YYYY
	 DESCR:
	 This is a sample program to demonstrate the use of
	 passing arrays as parameters.
*/
#include <iostream>
using namespace std;

// function prototypes
// pass by value and pass by reference parameters
// const keyword prevents modification of pass by 
// reference array
void sum1DArr(const int inArr[], int size, int& sum);
// overloaded functions -- same name but different parameters
int sumArr(int inArr[], int size);
int sumArr(int inArr[][3], int size);
int sumArr(int inArr[][3][5], int size);
// sum rows 2D array
void sumRows(int inArr[][3], int size);
int main(void)
{
	// create arrays using initializer lists
	int arr1D[] = {1, 2};
	int arr2D[][3] = {1, 2, 3, 4, 5, 6};
	int arr3D[][3][5] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
		13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
		27, 28, 29, 30};

	int ttl = 0;
	sum1DArr(arr1D, 2, ttl);
	cout << "Sum of 1D array = " << ttl << endl;
	cout << "Sum of 1D array = " << sumArr(arr1D, 2) << endl;
	cout << "Sum of 2D array = " << sumArr(arr2D, 2) << endl;
	cout << "Sum of 3D array = " << sumArr(arr3D, 2) << endl;
	cout << "Summing row of 2D array..." << endl;
	sumRows(arr2D, 2);
	return 0;
}

// Function:   sum1DArr
// Parameters: 1D array of integers, array size, and sum
// Returns:    sum of array elements through pass by reference
//                parameter sum
// Descr:      uses loop to sum all elements in array
void sum1DArr(const int inArr[], int size, int& sum)
{
	for (int iCntr = 0; iCntr < size; ++iCntr)
		sum += inArr[iCntr];
	return;
}

// Function:   sumArr
// Parameters: 1D array of integers and array size
// Returns:    sum of array elements
// Descr:      uses loop to sum all elements in array
int sumArr(int inArr[], int size)
{
	int sum = 0;
	for (int iCntr = 0; iCntr < size; ++iCntr)
		sum += inArr[iCntr];
	return sum;
}

// Function:   sumArr
// Parameters: 2D array of integers and size of 1st dimension
// Returns:    sum of array elements
// Descr:      uses loop to sum all elements in array
int sumArr(int inArr[][3], int size)
{
	int sum = 0;
	for (int iCntr = 0; iCntr < size; ++iCntr)
		for (int jCntr = 0; jCntr < 3; ++jCntr)
			sum += inArr[iCntr][jCntr];
	return sum;
}

// Function:   sumArr
// Parameters: 3D array of integers and size of 1st dimension
// Returns:    sum of array elements
// Descr:      uses loop to sum all elements in array
int sumArr(int inArr[][3][5], int size)
{
	int sum = 0;
	for (int iCntr = 0; iCntr < size; ++iCntr)
		for (int jCntr = 0; jCntr < 3; ++jCntr)
			for (int kCntr = 0; kCntr < 5; ++kCntr)
				sum += inArr[iCntr][jCntr][kCntr];
	return sum;
}

void sumRows(int inArr[][3], int size)
{
	for(int row = 0; row < size; row++)
	{
		int rowTotal = 0;
		for(int col = 0; col < 3; col++)
			rowTotal += inArr[row][col];

		cout << "row " << (row + 1) << " total = " << rowTotal << endl;
	}
}