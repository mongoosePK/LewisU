/*
     File:   DataLoop.cpp
	 Author: William Pulkownik
	 Date:   02/15/2016
	 Descr:
	 In class example to demonstrate the use of
	 a variety of looping structures.
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	int inpInt, ttlInts = 0, intCntr = 0;
	string fileName;
	ifstream inputFile;

	//get filename from user
	cout << "Please enter the file name: ";
	cin >> fileName;
	//open file and check for open errors like invalid name
	inputFile.open(fileName);

	if (inputFile.fail())
	{
		cout << "Error cannot open file for input" << endl;
		exit(-1); //exit(-1) exits program from any module or function
	}
	for (ttlInts = 0, intCntr = 0 ; !inputFile.eof() ; intCntr++) 
	{
		inputFile >> inpInt;
		// skip accumulating if negative number entered
		// only accumulate positive numbers
		if (inpInt < 0)
			continue;
		ttlInts += inpInt;
	}

	// display the total and count
	cout << "The number of integers entered is " << intCntr << endl;
	cout << "The sum of positive integers entered is " << ttlInts << endl;

	inputFile.close();
	return 0;
}