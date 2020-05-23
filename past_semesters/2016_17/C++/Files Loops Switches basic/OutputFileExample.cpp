/*
William Pulkownik
24 FEB 2015

descr: write decimal and binary data to outputfile
*/
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;
//prototype needs function type name and parameter only
string Dec2Bin(int decNum);

int main()
{
	fstream outFile("C:\\Users\\winxp\\Desktop\\Dec2Bin.txt", ios::out);
	// check for open errors
	if (!outFile)
	{
		cout << "error! cannnot open file for output" << endl;
		exit(-1);
	}
	//display table headings
	outFile << setw(10) << "Decimal" << setw(15) << "Binary" << endl;
	outFile << setw(10) << "=======" << setw(15) << "======" << endl;
	
	//output from file decimal and binary equivalents
	for (int decNum = 1; decNum <= 20; decNum++)
		outFile << setw(10) << decNum << setw(15) << Dec2Bin(decNum) << endl;


	outFile.close();
	return 0;
}