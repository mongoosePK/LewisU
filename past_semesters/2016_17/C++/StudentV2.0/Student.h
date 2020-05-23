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

// prevent multiple definitions of Studen class
#ifndef STUDENT_H
#define STUDENT_H

class Student {
private: 
	string name;
	int midTerm;
	int finalExam;
public:
	// constructors
	Student();
	Student(string, int, int);
	//DESTRUCTOR
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
};

#endif
	