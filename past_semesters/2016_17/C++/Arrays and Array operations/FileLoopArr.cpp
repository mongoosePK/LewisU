/*
     FILE:   FileLoopArr.cpp
	 AUTHOR: William Pulkownik
	 DATE:   2MAR2016
	 DESCR:
	 This is a sample program to loop and read data 
	 from a file into an array for subsequent processing.
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int man(void)
{
	fstream inFile;
	string fileName;
	const int MAX_INTS = 20;
	int inpIntArr[MAX_INTS] = {}, numInts, totalInts = 0;

	// open an existing file for input, fail if doesn't exist
	cout << "Please input a data file to read: ";
	getline(cin, fileName);
	inFile.open(fileName, ios::in);
	// check for file open errors
	if (inFile.fail()) {
		cout << "ERROR! Cannot open file for input!" << endl;
		exit(-1);
	}
	// using while loop, load all integers from file
	// or up to maximum number of array elements,
	// whichever comes first
	cout << "Reading integers from file..." << endl;
	numInts = 0;
	while (!inFile.eof() && numInts < MAX_INTS)
	{
		inFile >> inpIntArr[numInts];
		numInts++;
	}
	cout << "num of ints read from file: " << numInts << endl;
	// display array contents
	for(int iVar : inpIntArr)
		cout << iVar << ' ';
	cout << endl;
	
	for(int i = 0; i < numInts; i++)
		totalInts += inpIntArr[i];
	cout << "Total of ints read from file is " << totalInts << endl;
	cout << "Avg of all ints read is " << float(totalInts) / numInts << endl;
	// close file
	inFile.close();

	return 0;
}
