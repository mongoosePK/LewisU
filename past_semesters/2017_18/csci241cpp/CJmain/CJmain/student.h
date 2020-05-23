#ifndef student_h
#define student_h

#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>


using std::string;
using std::ostream;
class student
{
	friend bool operator==(const student& s1, const student& s2);
//private:
public:
	string creditsh, codeh, idh, nameh, gradeh;



	// student class constructor
	student(const string& code = " ", const string& id = " ", \
		const string& name = " ", const string& grade = " ", \
		const string& credits = " ")
	{
		codeh = code;
		idh = id;
		nameh = name;
		gradeh = grade;
		creditsh = credits;
	}
	void print(ostream& fout) // prints to outfile
	{
		fout << codeh << "\t" << creditsh << "\t" << gradeh << "\n";
	}
};
#endif

//overload equality operator
bool operator==(const student& s1, const student& s2)
{
	return (s1.idh == s2.idh);
}