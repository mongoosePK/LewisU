/*
   FILE:   Student.cpp
   AUTHOR: 
   DATE:   04/18/2016
   DESCR:
   This is the implementation file for the
   Student class.
   4/20 -- added destructor
   4/25 -- added static class members, copy constructor, friend functions

   */
#include "Student.h"

int Student::numObj = 0; // definition of static member

// constructors
Student::Student() {  // default constructor
	name = "";
	midTerm = 0;
	finalExam = 0;
	numObj++; //increment static counter
}

Student::Student(string n, int mt, int fnl) {  // parameter constructor
	name = n;
	midTerm = mt;
	finalExam = fnl;
	numObj++; //increment static counter
}

Student::Student(const Student& s) {  // copy constructor
	name = s.name;
	midTerm = s.midTerm;
	finalExam = s.finalExam;
	numObj++; //increment static counter
}

// destructor
Student::~Student() {
	numObj--; //decrement static counter
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

// static function to retrieve static number of objects

int Student::getNumObj() {
	return numObj;
}
//overload = operator as member function
//copy over private data ( :: <-- scope resolution operator)
Student& Student::operator = (const Student& rhs) {
	//'this' pointer passed as a hidden argument 
	// refers to the object itself --both methods are equivalent
	(*this).name = rhs.name;
	this->midTerm = rhs.midTerm;
	finalExam = rhs.finalExam;
	// return reference to obj
	return *this;
}