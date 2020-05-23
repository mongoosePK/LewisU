/*
 FILE:   BinaryFile.cpp
 AUTHOR: William Pulkownik
 DATE:   29 FEB 2016
 DESCR:
 In-class example to show example of 1-D arrays
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	string fname;
	fstream inFile;
	const int SIZE = 25;
	int inpArray[SIZE], count = 0;
	cout << "Please input the data file to read: ";
	getline(cin, fname);
	inFile.open(fname, ios::in);
	if(inFile.fail())
	{
		cout << "couldnt open file" << fname << " for input" << endl;
		exit(-1);
	}
	while (count < SIZE && !inFile.eof())
	{
		inFile >> inpArray[count];
		count++;
	}
	//display data
	cout << "data read from file into array..." << endl;
	for (int ival: inpArray)
		cout << ival << ' ';
	cout << endl;

	cout << "# of elements read = " << count << endl;

	inFile.close();
	return 0;
}
