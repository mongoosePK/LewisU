/*
     FILE:   L11_Circle.cpp
	 AUTHOR: William Pulkownik
	 DATE:   5 MAY 2016
	 DESCR:
	 This is the implementation file for the
	 Circle class.
*/

// include specification file
#include "L11_Circle.h"

#define _USE_MATH_DEFINES  // enable non-standard mathematical constants
#include <math.h>

int Circle::numObj = 0;
// constructors
Circle::Circle() {
	name = new string("");
	diameter = 0; 
	centerX = 0; 
	centerY = 0;
	numObj++;
}

Circle::Circle(string n, double d, int x, int y) { 
	name = new string(n);
	diameter = d; 
	centerX = x; 
	centerY = y;
	numObj++;
}
Circle::Circle(const Circle& c) {
	name = new string("");
	name = c.name;
	diameter = c.diameter;
	centerX = c.centerX;
	centerY = c.centerY;
	numObj++;
}
// destructor
Circle::~Circle() {
	delete name;
	numObj--;
}

// mutators
void Circle::setName(string n) {
	*name = n;
}

void Circle::setDiameter(double d) {
	diameter = d;
}

void Circle::setCenterX(int x) {
	centerX = x;
}

void Circle::setCenterY(int y) {
	centerY = y;
}

// calculators
double Circle::calcArea() const {
	return M_PI * pow((diameter / 2), 2.0);
}

double Circle::calcPerimeter() const {
	return M_PI * diameter;
}

int  Circle::getNumObj() {
	return numObj;
}


// overloaded insertion operator as friend function
ostream& operator<< (ostream& lhs, const Circle& rhs) {
	lhs << *rhs.name << " diameter = " << fixed << setprecision(2) << rhs.diameter
		<< " area = " << rhs.calcArea() << endl;
	return lhs;
}

Circle& Circle::operator = (const Circle& rhs) {
	*name = *rhs.name;
	diameter = rhs.diameter;
	centerX = rhs.centerX;
	centerY = rhs.centerY;
	// return reference to obj
	return *this;
}