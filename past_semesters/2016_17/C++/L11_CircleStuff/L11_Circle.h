/*
     FILE:   L11_Circle.h
	 AUTHOR: William Pulkownik
	 DATE:   4 MAY 2016
	 DESCR:
	 This is the specification file for the
	 Circle class.
*/

// using declarations for std namespace
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

// prevent multiple definitions of Student class
#ifndef CIRCLE_H
#define CIRCLE_H



class Circle 
 {
 private:
	 string* name;
	 double diameter;
	 int centerX;
	 int centerY;
	 static int numObj;
 public:
	 // constructor
	 Circle();
	 Circle(string, double, int, int);
	 Circle(const Circle& c);
	 // destructor
	 ~Circle();
	 // inline accessors
	 string getName() const {return *name;}
	 double getDiameter() const {return diameter;}
	 int getCenterX() const {return centerX;}
	 int getCenterY() const {return centerY;}
	 // mutators
	 void setName(string);
	 void setDiameter(double);
	 void setCenterX(int);
	 void setCenterY(int);
	 // calculators
	 double calcArea() const;
	 double calcPerimeter() const;
	 static int getNumObj();
	 // overloaded insertion operator as friend function
	 Circle& Circle::operator = (const Circle& rhs);
	 friend ostream& operator<< (ostream&, const Circle&);
 };



#endif