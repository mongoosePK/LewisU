/*
     FILE:   AddrFuncs.cpp
	 AUTHOR: CREngland
	 DATE:   MM/DD/YYYY
	 DESCR:
	 This program demonstrates the use of memory address type 
	 parameters in functions.
*/

#include <iostream>
using namespace std;

// function to return the input value doubled
// uses return value
int Dbl(int iVar)
{
	return iVar + iVar;
}

// function to return the input value doubled
// uses pass by reference parameter
void PBRefDbl(int& iVar)
{
	iVar = iVar + iVar;
}

void PBPtrDbl(int* iVar)
{
	*iVar = *iVar + *iVar;
}


int main()
{
	int iVar = 2;
	cout << "iVar = " << iVar << endl;

	// pass by value with return value
	iVar = Dbl(iVar);
	cout << "Dbl = " << iVar << endl;

	// pass by reference using reference variables
	PBRefDbl(iVar);
	cout << "PBRefDbl = " << iVar << endl;

	// pass by ref using pointer var
	PBPtrDbl(&iVar);
	cout <<" PBPtrDbl = " << iVar << endl;

	return 0;
}