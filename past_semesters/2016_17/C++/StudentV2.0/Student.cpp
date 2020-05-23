/*
   FILE:   Student.cpp
   AUTHOR: 
   DATE:   04/18/2016
   DESCR:
   This is the implementation file for the
   Student class.
*/
#include "Student.h"

// constructors
Student::Student() {  // default constructor
	cout << "\n\tStudent Default constructor...\n";
	name = "";
	midTerm = 0;
	finalExam = 0;
}

Student::Student(string n, int mt, int fnl) {  // parameter constructor
	cout << "\n\tStudent parameter constructor...\n";
	name = n;
	midTerm = mt;
	finalExam = fnl;
}
// DESTRUCTOR
Student::~Student() {
	cout << "\n\tStudent Destructor...\n";
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