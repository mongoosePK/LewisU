/*
Author:William Pulkownik
Date: 3/30/16
File: lab6.cpp
Descr: array modifier
*/

#include <iostream>
#include <iomanip>
using namespace std;

int* arrMod(const int* orig, const int size)
{
	int* space = new int[size + 1];
	if (space != nullptr)
	{
		space[0] = 0;
		for (int i = 1; i < size + 1; i++)
			space[i] = orig[i - 1];
	}
	return space;
}

int main()
{
	const int size = 5;
	int arr[size] = { 1,2,3,4,5};
	
	cout << "The contents of original array are: \n";
	for (int cntr = 0; cntr < size; cntr++)
		cout << arr[cntr] << " ";
	cout << endl;
	int* arr2 = arrMod(arr, size);
	cout << "The contents of new array are: \n";
	for (int i=0; i < 6; i++)
		cout << arr2[i] << " ";
	cout << endl;
	delete [] arr2;
	return 0;
}