/*
	William Pulkownik
	16 Mar 2016
	CIS 2541
	Ms. England
	#63 MidTerm
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;
const int MAX_NUMS = 50;

bool openFile(fstream &file, string name)
{
	bool status;
	file.open(name, ios::in);
	if(file.fail())
		status = false;
	else
		status = true;
	return status;
}

void trackNums(int data[], int &negs, int &pos, int &zeros)
{
	int index; 
	for (int index = 0; index < MAX_NUMS; index++)
	{
		if (data[index] > 0)
			pos += 1;
		else if (data[index] <0)
			negs += 1;
		else
			zeros +=1;
	}
}

int main()
{

	int fData[MAX_NUMS];
	int negs = 0, pos = 0, zeros = 0, i = 0, count = 0;
	
	string fName;
	fstream(myFile);
	bool status;

	cout << "Please enter the file name: ";
	cin >> fName;
	status = openFile(myFile, fName);
	if (status == false)
	{
		cout << "The file you chose cannot be opened.";
		exit(-1);
	}
	while (!myFile.eof())
	{
		for (i = 0; i < MAX_NUMS; i++)
		{
			myFile >> fData[i];
			count++
		}
	}
	
	cout << "total # of integers read from file = " << count << endl;
	trackNums(fData, negs, pos, zeros);
	cout << "there are " << negs << " Negative numbers." << endl;
	cout << "there are " << pos << " positive numbers." << endl;
	cout << "there are " << zeros << " Zeros." << endl;
	
	
	return 0;
}

/*
Please enter the file name: C:\Users\winxp\Desktop\MTTester.txt
total # of integers read from file = 200
there are 34 Negative numbers.
there are 12 positive numbers.
there are 4 Zeros.
Press any key to continue . . .
*/