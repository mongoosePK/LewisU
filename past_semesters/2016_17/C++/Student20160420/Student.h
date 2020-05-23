/*
   FILE:   Student.h
   AUTHOR: 
   DATE:   04/18/2016
   DESCR:
   This is the specification file for the
   Student class.
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
	static int numObj; //object counter 
public:
	// constructors
	Student();
	Student(string, int, int);
	Student(const Student&); //const keyword prevents modification
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
	static int getNumObj(); // return static data member
	//grant friendship to obj ** this allows us to eliminate the 'get' from display
	friend void DisplayStudent(Student& s);
	
	friend Student GetStudent(); //**does NOT work as is** <-- now we can not use 'set' in this function
	// the data is read in to the variables and shared here.
};

#endif
	