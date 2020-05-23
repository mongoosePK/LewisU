/*
	William Pulkownik
	16 Mar 2016
	CIS 2541
	Ms. England
	Demonstation of pointers and reference variables
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int iVar, &iRef = iVar;
	iRef = 10;
	//create pointer
	int *iPtr = NULL;
	iPtr = &iVar;


	cout << "iVar = " << iVar << "\t &iVar = " << &iVar << endl;
	cout << "iRef = " << iRef << "\t &iRef = " << &iRef <<endl;
	cout << "iPtr = " << iPtr << "\t &iPtr = " << &iPtr << "\t *iPtr = " << *iPtr << endl;
	cout << "*&iVar = " << *&iVar << endl;
	cout << "the indirection (or dereferencing) operator can only be used with pointer type variables (variables modified with address locator(&)) \n";  
	if (iPtr != nullptr)
		cout << "*iPtr = " << iPtr << endl;
	cout << "*&iVar = " << *&iVar << endl;

	return 0;
}

/*
iVar = 10        &iVar = 0045FBE0
iRef = 10        &iRef = 0045FBE0
iPtr = 0045FBE0  &iPtr = 0045FBC8        *iPtr = 10
the indirection (or dereferencing) operator can only be used with pointer type v
ariables
Press any key to continue . . .
*/
