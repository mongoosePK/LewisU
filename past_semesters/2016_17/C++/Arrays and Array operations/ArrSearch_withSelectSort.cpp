/*
     FILE:   ArrSearchSortSelectSort2.1.cpp
	 AUTHOR: Carolyn England
	 DATE:   MM/DD/YYYY
	 DESCR:
	 This is a sample program to demonstrate the use of
	 searching and sorting arrays.
	 3/9/2016--CRE--added linear and binary search; added bubble sort
*/
#include <iostream>
using namespace std;

// function prototypes
void displayArray(int nums[], int size);
int linearSearch(const int nums[], int size, int value);
void bubbleSort(int nums[], int size);
void selectionSort(int nums[], int size);
int binarySearch(const int nums[], int size, int value);

int main(void)
{
	// create array using initializer list
	int iArr[] = {32, -15, 572, 0, -225, 66, -99, 572};
	int iSize = sizeof(iArr)/sizeof(int), searchValue, searchIndex;
	// search for value in array
	cout << "Input a value to search: ";
	cin >> searchValue;
	searchIndex = linearSearch(iArr, iSize, searchValue);
	if (searchIndex < 0)
		cout << "Sorry, " << searchValue << " not found!" << endl;
	else
		cout << searchValue << " was found at position " << searchIndex + 1 << endl;

	// display array
	displayArray(iArr, iSize);
	// sort the array choose bubble OR selection

	// bubbleSort(iArr, iSize);
    selectionSort(iArr, iSize);
	cout << "Sorted array...." << endl;
	displayArray(iArr, iSize);
	// ask user for new value
	cout << "Input a new value to search: ";
	cin >> searchValue;
	searchIndex = binarySearch(iArr, iSize, searchValue);
	if (searchIndex < 0)
		cout << "Sorry, " << searchValue << " not found!" << endl;
	else
		cout << searchValue << " was found at position " << searchIndex + 1 << endl;

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

// Function:   linearSearch
// Parameters: 1D array of integers, array size, and search value
// Returns:    integer index of found element or -1 if not found
// Descr:      uses linear search algorithm to look at all array
//             elements until found or end of array is reached
int linearSearch(const int nums[], int size, int value) {
	bool found = false;
	int position = -1;
	int index = 0;
	// loop through all elements until found or end of array is reached
	while(!found && index < size) {
		if (nums[index] == value) {
			found = true;
			position = index;
		}
		index++;
	}
	return position;
}

// Function:   bubbleSort
// Parameters: 1D array of integers, array size
// Returns:    nothing
// Descr:      uses bubble sort algorithm to sort all array elements
//             in increasing/ascending order 
void bubbleSort(int nums[], int size) {
	bool swap;
	do {
		swap = false;
		for(int count = 0; count < (size - 1); count++) {
			if(nums[count] > nums[count + 1]) {
				int temp = nums[count];
				nums[count] = nums[count + 1];
				nums[count + 1] = temp;
				swap = true;
			} // if
		} // for
	} while (swap);
}

// Function:   binarySearch
// Parameters: 1D array of sorted integers, array size, and search value
// Returns:    integer index of found element or -1 if not found
// Descr:      uses binary search algorithm to successively divide array
//             in half to until element is found or place in array 
//             is passed
int binarySearch(const int nums[], int size, int value) {
	int first = 0, last = size - 1, position = -1;
	bool found = false;
	while(!found && first <= last) {
		int middle = (first + last) / 2;
		if(nums[middle] == value) {
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

void selectionSort(int nums[], int size)
{
    int startScan, index, minValue, minIndex;
    for (startScan = 0; startScan < (size - 1); startScan++)
	{
        index = startScan;
        minIndex = startScan;
        minValue = nums[startScan];
        for(index = startScan + 1; index < size; index++)
		{
            if(nums[index] < minValue)
			{
                minValue = nums[index];
                minIndex = index;
			}
		}
        nums[minIndex] = nums[startScan];
        nums[startScan] = minValue;
	}
}