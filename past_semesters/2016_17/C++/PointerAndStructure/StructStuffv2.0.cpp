/*
	File:   StructStuff.cpp
	Author: 
	Date:   04/11/2016
	Descr:
	In class exercise to practice the use of
	structured data types.
*/

#include <iostream>
#include <string>  // for C++ string class
using namespace std;

// union definition of FinalGrade
union FinalGrade {
	char letter;
	int ttlPoints;
	double percent;
};
//enumerated type for grade level in school
enum Year {FRESHMAN =1, SOPHOMORE, JUNIOR, SENIOR};

// student structure declaration
struct Student {
	int stuID;
	string name;
	FinalGrade fg;  // adding union type
	Year yr; // adding enumerated data type
};

// function to display student information
void showStudent(Student s) {
	cout << "\n***Student Information***\n";
	cout << s.name << endl;
	cout << s.stuID << endl;
	cout << s.fg.letter << endl;  // display letter final grade
	switch(s.yr) {
	case FRESHMAN:
		cout << "FRESHMAN" << endl;
		break;
	case SOPHOMORE:
		cout << "SOPHOMORE" << endl;
		break;
	case JUNIOR:
		cout << "JUNIOR" << endl;
		break;
	case SENIOR:
		cout << "SENIOR" << endl;
		break;
	}
	return;
}

// function to get student information and return
Student getStudent() {
	// create Student variable
	Student s;
	int year;
	// get student details
	cout << "Enter the student ID: ";
	cin >> s.stuID;
	cout << "Enter the student first name: ";
	cin >> s.name;
	cout << "Enter the student final grade as a character: ";
	cin >> s.fg.letter;
	cout << "Enter year of school (1-Freshman, 2-Sophomore, 3-Junior, 4-Senior)" << endl;
	cin >> year;
	// need to cast first before assigning to enum type
	s.yr = static_cast<Year>(year);
	return s;
}

int main() {
	// create variable of Student structure type
	Student stu1, stu2 = {222}, stu3 = {333, "Sagar"};
	stu1.stuID = 111;
	stu1.name = "Kevin";
	stu1.fg.letter = 'A';
	// display student st1
	showStudent(stu1);
	// create new student and get information
	Student st3 = getStudent();
	showStudent(st3);
	// create pointer to student structure
	Student *stPtr;
	stPtr = new Student; // allocate memory
	*stPtr = getStudent();
	cout << "\n\tName: " << (*stPtr).name << endl;
	cout << "\tID: " << stPtr->stuID << endl;
	// create array of structure variables
	Student stuArray[3] = {{888, "Sally"}}; // initialized first element
	stuArray[1].stuID = 999; // set values for second element
	stuArray[1].name = "Bob";
	stuArray[2] = getStudent();
	cout << "Displaying array elements..." << endl;
	for(int i = 0; i < sizeof(stuArray)/sizeof(Student); i++)
		showStudent(stuArray[i]);
	// release memory
	delete stPtr;
	return 0;
}