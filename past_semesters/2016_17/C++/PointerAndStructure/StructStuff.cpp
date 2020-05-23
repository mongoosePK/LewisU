/*
	File: StructStuff.cpp
	Author: William Pulkownik (via Matt Weiss)
	Date: 4/11/16
	Prog: Chapter 11
	Descr: In class exercise to practice use of structured data types.

*/

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

// Union definition of the final grade
union FinalGrade {
	char letter;
	int ttlPoints;
	double percent;
};
// student structure declaration
struct Student {
	int stuID;
	string name;
	FinalGrade fg; //added union type
};

void showStudent(Student s) {
	cout<< "\n***Student Information***\n";
	cout << s.name << endl;
	cout << s.stuID << endl;
	cout << s.fg.letter << endl; //display letter final grade
	cout << s.fg.percent << endl; // diaplay percent fianl grade
	cout << s.fg.ttlPoints << endl; // display final points
	return;
}

Student getStudent() {
	// create Student variable
	Student s;
	cout << "Enter the student ID: ";
	cin >> s.stuID;
	cout << "Enter students first name: ";
	cin >> s.name;
	cout << "enter Student's final grade as an integer: ";
	cin >> s.fg.ttlPoints;
	return s;
}

int main() {
	// create variable of Student structure type
	Student stu1, stu2 = {222} , stu3 = {333, "Sagar"};
	stu1.stuID = 111;
	stu1.name = "Kevin";
	showStudent(stu1);
	Student st3= getStudent();
	showStudent(st3);
	//create pointer to student structure. this creates the variable
	Student *stPtr;
	// 
	stPtr = new Student;
	*stPtr = getStudent();
	// stPtr = &st3;
	cout << "\n\tName: " << (*stPtr).name << endl; //parenthesis for operator precedence, normally member dot occurs first
	cout <<"\tID: " << stPtr->stuID << endl;
	// create an array of structure variables
	Student stuArray[3] = {{888, "Sally"}}; //initialized first element
	stuArray[1].stuID = 999;
	stuArray[1].name = "Bob";
	stuArray[2] = getStudent();
	cout << "Displaying array elements..."<< endl;
	for(int i=0; i < 3; i++)
		showStudent(stuArray[i]);
	// change points for variable to be percent
	cout << "change points to percent..." << endl;
	double percent = stuArray[2].fg.ttlPoints / 1000.0; //make sure types work
	stuArray[2].fg.percent = percent;
	showStudent(stuArray[2]);
	// release memory
	delete stPtr;
	return 0;
}
