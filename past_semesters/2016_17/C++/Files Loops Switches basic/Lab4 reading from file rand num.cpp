/*
William Pulkownik
24 FEB 2015
CIS 2541
Lab4.cpp
descr: loops and files
*/

#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>



using namespace std;


int main()
{
	int numNum = 0, sumNum = 0, fileInt;
	
	string line, fileName;

	cout << "please enter the full file name: " << endl;
	cin >>  fileName;
	fstream inFile(fileName, ios::in);
	if (!inFile)
	{
		cout << "error! cannnot open file for reading" << endl;
		exit(-1);
	}
	while (!inFile.eof())
	{
		inFile >> fileInt;
		sumNum += fileInt;
		numNum++; 
	}
	cout << "There are " << numNum << " Numbers in the file." << endl;
	cout << "The sum of the numbers in the file is " << sumNum << endl;
	
	cout << fixed << setprecision(3);
	float avgNum = float(sumNum) / float(numNum);
	cout << "The average of the numbers is " << avgNum << endl;
	return 0;
}
/*
please enter the full file name:
C:\Users\winxp\Desktop\Random.txt
There are 200 Numbers in the file.
The sum of the numbers in the file is 105527
The average of the numbers is 527.635
Press any key to continue . . .
*/

/*
please enter the full file name:
gobldygook
error! cannnot open file for reading
Press any key to continue . . .
*/