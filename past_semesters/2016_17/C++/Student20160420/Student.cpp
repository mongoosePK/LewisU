/*
   FILE:   Student.cpp
   AUTHOR: 
   DATE:   04/18/2016
   DESCR:
   This is the implementation file for the
   Student class.
*/
#include "Student.h"

int Student::numObj = 0; // def of static member -- allocates memory
// constructors ** only one constructor called at a time ** 
Student::Student() {  // default constructor
	cout << "\n\tStudent Default Constructor...\n";
	name = "";
	midTerm = 0;
	finalExam = 0;
	numObj++; // increment static counter
}

Student::Student(string n, int mt, int fnl) {  // parameter constructor
	cout << "\n\tStudent Parameter Constructor...\n";
	name = n;
	midTerm = mt;
	finalExam = fnl;
	numObj++; // increment static counter
}

Student::Student(const Student& s) {
	cout << "\n\tStudent Copy Constructor...\n";
	name = s.name;
	midTerm = s.midTerm;
	finalExam = s.finalExam;
	numObj++;
}

// destructor
Student::~Student() {
	cout << "\n\tStudent Destructor...\n";
	numObj--; // decrement 
}

// mutators
void Student::setName(string n) {
	name = n;
}

void Student::setMidTerm(int mt) {
	midTerm = mt;
}

void Student::setFinalExam(int fnl) {
	finalExam = fnl;
}

// functions to calculate and return values
int Student::getTtlPoints() {
	return midTerm + finalExam;
}

float Student::getAverage() {
	return (midTerm + finalExam)/2.0F;
}

// static function to retrieve static num obj
int Student::getNumObj() {
	
	return numObj;
}