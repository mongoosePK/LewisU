/*
     FILE:   ArrSearchSort.cpp
	 AUTHOR: William Pulkownik
	 DATE:   07 MAR 2016
	 DESCR:
	 This is a sample program to demonstrate the use of
	 searching and sorting arrays.
*/
#include <iostream>
using namespace std;

// function prototypes
void displayArray(int nums[], int size);
int linearSearch(int nums[], int size, int value);
void bubbleSort(int nums[], int size);
int binarySearch(const int nums[], int size, int value);

int main(void)
{
	// create array using initializer list
	int iArr[] = {32, -15, 572, 0, -225, 66, -99, 572};
	int iSize = sizeof(iArr)/sizeof(int), searchVal, searchIndex;
	cout << "Input value you seek: ";
	cin >> searchVal;
	searchIndex = linearSearch(iArr, iSize, searchVal);
	if (searchIndex < 0)
		cout << searchVal << "is not found." << endl;
	else
		cout << searchVal << " Was found at position " << searchIndex + 1 << endl;
	// display array then sort array
	displayArray(iArr, iSize);
	bubbleSort(iArr, iSize);
	cout << "Sorted array..." << endl;
	displayArray(iArr, iSize);
	cout << "Input value you seek: ";
	cin >> searchVal;
	searchIndex = binarySearch(iArr, iSize, searchVal);
	if (searchIndex < 0)
		cout << searchVal << "is not found." << endl;
	else
		cout << searchVal << " Was found at position " << searchIndex + 1 << endl;
	return 0;
}

// Function:   displayArray
// Parameters: 1D array of integers, array size
// Returns:    nothing
// Descr:      uses loop to display all elements to 
//             standard output
void displayArray(int nums[], int size) 
{ 
	for (int index = 0; index < size; index++) 
		cout << nums[index] << " "; 
	cout << endl; 
}

int linearSearch(int nums[], int size, int value)
{
	bool found = false;
	int position = -1;
	int index = 0;
	while(!found && index < size)
	{
		if (nums[index] == value)
		{
			found = true;
			position = index;
		}
		index++;
	}
	return position;
}

void bubbleSort(int nums[], int size)
{
	bool swap;
	do
	{
		swap = false;
		for(int count = 0; count <  (size - 1); count++)
		{
			if (nums[count] > nums[count + 1])
			{
				int temp = nums[count];
				nums[count] = nums[count +1];
				nums[count + 1] = temp;
				swap = true;
			}
		}
	}
	while (swap);
}

int binarySearch(const int nums[], int size, int value)
{
	int first = 0, last = size - 1, position = -1;
	bool found = false;
	while(!found && first <= last)
	{
		int middle = (first + last) / 2;
		if(nums[middle] == value)
		{
			found = true;
			position = middle;
		}
		else if (nums[middle] > value)
			last = middle - 1;
		else
			first = middle + 1;
	}
	return position;
}