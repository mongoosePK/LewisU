/*
   FILE:   Student.h
   AUTHOR: 
   DATE:   04/18/2016
   DESCR:
   This is the specification file for the
   Student class.
   4/20 -- added destructor
   4/25 -- added static class members, copy constructor, friend functions
  
*/

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

// prevent multiple definitions of Student class
#ifndef STUDENT_H
#define STUDENT_H

class Student {
private: 
	string name;
	int midTerm;
	int finalExam;
	static int numObj; // object counter
public:
	// constructors
	Student();
	Student(string, int, int);
	Student(const Student&);
	// destructor
	~Student();
	// mutators (aka setters) for private data
	void setName(string);
	void setMidTerm(int);
	void setFinalExam(int);
	// accessors (aka getters) for private data
	// declared inline
	string getName() const {return name;}
	int getMidTerm() const {return midTerm;}
	int getFinalExam() const {return finalExam;}
	// functions to calculate values
	int getTtlPoints();
	float getAverage();
	static int getNumObj();  // return static data member
	// grant friendship to function
	friend void DisplayStudent(Student& s);
	//overload = operator as member function
	// right hand side member is const -- we dont want it to change
	Student& operator = (const Student& rhs);
	//overload extraction operator as friend function
	friend istream& operator >> (istream& lhs, Student& rhs);
};

#endif
	