/*
William Pulkownik
15 FEB 2015

descr: use of variety of loop structures
*/

#include <iostream>
using namespace std;

int main()
{
	int numInt, inpInt, ttlInts = 0, intCntr = 0;
	cout << "please input a positive num of integers to read: " ;
	cin >> numInt;
/*	COMMENT OUT WHILE AND DOWHILE LOOPS
	// using a WHILE loop to validate a pos num is put in
	while (numInt <= 0)
	{
		cout << "ERROR! please input a positive number: ";
		cin >> numInt;

	}
	// add a series of numbers based on user input with DO-WHILE
	do 
	{
		cout << "Enter an integer number: ";
		cin >> inpInt;
		ttlInts += inpInt; // keeps a running total
		intCntr++;	
	}
	while (intCntr < numInt); 
	//display the total and count
	cout << "The number of integers entered is " << intCntr << endl;
	cout << "The sum of integers entered is " << ttlInts << endl;
*/
	//for loop to add integers
	for (ttlInts = 0, intCntr = 0; numInt > 0 && intCntr < numInt; intCntr++)
	{
		cout << "Enter an integer number: ";
		cin >> inpInt;
		// skip accumulating if neg num entered only accumulate pos numbers using 'continue' to continue back to beginning of loop
		// also, break statement has effect of ending loop
		if (inpInt < 0)
			continue;
		ttlInts += inpInt;
	}
	cout << "The number of integers entered is " << intCntr << endl;
	cout << "The sum of integers entered is " << ttlInts << endl;
	return 0;
}
