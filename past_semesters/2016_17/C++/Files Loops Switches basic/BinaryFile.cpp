/*
 FILE:   BinaryFile.cpp
 AUTHOR: <Your Name Here>
 DATE:   MM/DD/YYYY
 DESCR:
 In-class example to show example
 of byte file writing and reading for
 various data types.
 Uses reinterpret_cast to write different
 data types: http://www.cppreference.com/wiki/keywords/casting_comparison
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// function prototypes
void CreateBinFile(string);
void DisplayBinFile(string);

/*
	Function: main
	Parms:    none
	Returns:  none
	Calls:    CreateBinFile, DisplayBinFile
	Descr:
	Prompts user for filename to use for
	binary data.  Calls CreateBinFile to 
	create the file and DisplayBinFile
	to verify written data.
*/
int main(void)
{
	// variable declarations
	string fname;

	// prompt user for filename and read
	cout << "Please enter an output filename: ";
	getline(cin, fname);
	
	// write binary data to file
	CreateBinFile(fname);

	// verify binary file contents
	DisplayBinFile(fname);

	return 0;
}

/*
	Function: CreateBinFile
	Parms:    string -- file name
	Returns:  none
	Calls:    none
	Descr:
	Opens binary file for output.  Writes
	integer, float, character, and c-String
	variables.
*/
void CreateBinFile(string fn)
{
	// data to write
	int iVar = 12345;
	float fVar = 12.345f;
	char cVar = 'b', csVar[] = "hello";

	// defines and opens binary file for input
	fstream outFile(fn, ios::out|ios::binary); 

	// write some data to binary file
	if (outFile)
	{
		// write returns reference to ifstream so you can chain several together
		outFile.write(reinterpret_cast<char *>(&iVar), sizeof(iVar)); // 4 bytes
		outFile.write(reinterpret_cast<char *>(&fVar), sizeof(fVar)); // 4 bytes
		outFile.write(&cVar, sizeof(cVar)); // 1 byte
		outFile.write(csVar, sizeof(csVar)); // 6 bytes
		cout << "Binary data written to file...\n";
	}
	else
	{
		cout << "Could not open " << fn << " for binary output!\n";
		exit(-1);
	}

	// close file
	outFile.close();
	return;
}

/*
	Function: DisplayBinFile
	Parms:    string -- file name
	Returns:  none
	Calls:    none
	Descr:
	Opens binary file for input.  Reads
	integer, float, character, and c-String
	variables and displays them.
*/
void DisplayBinFile(string fn)
{
	// variable declarations
	int iVar;
	float fVar;
	char cVar, csVar[6];
	// defines and opens binary file for input
	fstream inFile(fn, ios::in|ios::binary); 

	// read from binary file and display
	if (!inFile.fail())
	{
		// read returns reference to ifstream so you can chain several together
		inFile.read(reinterpret_cast<char *>(&iVar), sizeof(iVar));
		inFile.read(reinterpret_cast<char *>(&fVar), sizeof(fVar));
		inFile.read(&cVar, sizeof(cVar));
		inFile.read(csVar, sizeof(csVar));
		cout << "The binary data read from file: "
			<< "\n\t" << iVar
			<< "\n\t" << fVar
			<< "\n\t" << cVar
			<< "\n\t" << csVar << endl;
	}
	else
	{
		cout << "Could not open " << fn << " for binary input!\n";
		exit(-2);
	}

	// close file
	inFile.close();
	return;
}