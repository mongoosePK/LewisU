/*
	William Pulkownik
	16 Mar 2016
	CIS 2541
	Ms. England
	Demonstation of  arrays, pointers and arithmetic operators.
*/

#include <iostream>
using namespace std;

int main()
{
	const int size = 5;
	int test[size] = {82, 95, 90, 63, 75};
	int *iPtr1, *iPtr2 =&test[size - 1];
//	iPtr1 = &test[0]; [OR USE]
	iPtr1 = test;

	cout << "displaying array with pointers" << endl;
	for(int i=0; i<size; i++)
		cout<<iPtr1[i]<< " ";
	cout << endl;
	
	cout << "displaying array without pointer " << endl;
	for(int i=0; i<size; i++)
		cout<< (iPtr1 + i)<< " ";
	cout << endl;

	cout << "Display in reverse" << endl;
	for(int i=0; i<size;i++)
		cout << *(iPtr2 - i) << " ";
	cout << endl;

	cout <<"Pointer difference \n" << "iPtr1 - iPtr2 = " << iPtr2 - iPtr1 << endl;
	cout <<"Display using changing pointer values \n";
	for(int *iPtr = test; iPtr <= iPtr2; iPtr++)
		cout << *iPtr << " ";
	cout<< endl;

	return 0;
}