//student report card
//this program reads information from a document and creats a new document
// that reports students repost cards.
//Written by Chris James, CIS2485-003, HW10 11/28/2016

#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <vector> //include vector library to use with students
#include <sstream> //library for string manipulation
#include "student.h" //include student class
using namespace std;

bool openfile(ifstream &, const char* name); //you shouldn't need to 
											 //change name to char*
void outPrint(ostream& out, const student& s)
{
	out << "Student Name:" << s.nameh << endl;
	out << "Student ID Number:" << s.idh << endl;
	out << " " << endl;
	out << "Course Code		Course Credit		Course Grade " << endl;
	out << "--------------------------------------------------------------" << endl;
}

int main()
{
	ifstream inFile;
	ofstream  outfile;
	//string code, id, name, grade;
	//int credits;
	bool status;
	vector<student> studs;
	char* inputFile = "C:\\Users\\William.WILLPOWER\\OneDrive\\Documents\\Visual Studio 2015\\Projects\\CJmain\\CJmain\\studentroster.txt";
	status = openfile(inFile, inputFile);

	//open file for output
	outfile.open("C:\\Users\\William.WILLPOWER\\OneDrive\\Documents\\Visual Studio 2015\\Projects\\CJmain\\CJmain\\studentGrades.txt");
	if (!outfile)
	{
		cerr << "Unable to open file  studentGrades.txt\n";
		//system("pause"); // commented these out 
		//exit(2);         // because my cpu didn't like them
	}

	//now we create students from the roster text file

	while (!inFile.eof()) //while the file has data
	{
		student newStud;
		inFile >> newStud.idh;
		inFile >> newStud.nameh;
		inFile >> newStud.codeh;
		inFile >> newStud.creditsh;
		inFile >> newStud.gradeh;
		studs.push_back(newStud);
	}
	outPrint(outfile, studs[0]); //print the first outputfile 
								 // student heading 
	for (unsigned int i = studs.size(); i >= 0; --i)
	{	
		
		((studs[i] == studs.at(i + 1)) ? studs[i].print(outfile) :
			outPrint(outfile, studs[i+1]));
	}

	inFile.close();
	outfile.close();
	//system("pause");
	return 0;
}

bool openfile(ifstream & inFile, const char* name)
{	//open input file
	bool isopen = true;

	inFile.open(name);
	if (!inFile)
	{
		isopen = false;
		cerr << "Unable to open file  studentroster.txt\n";
		//system("pause");
		//exit(-1);
	}
	return (isopen);
}

