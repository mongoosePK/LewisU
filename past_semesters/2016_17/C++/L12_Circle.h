/*
     FILE:   L12_Circle.h
	 AUTHOR: William Pulkownik
	 DATE:   12 MAY 2016
	 DESCR:
	 This is the definition of the base Circle class.
*/

#ifndef CIRCLE_H
#define CIRCLE_H

#define _USE_MATH_DEFINES  // enable non-standard mathematical constants
#include <math.h>

class Circle
{
protected:
	double radius;
public:
	// Default constructor
	Circle() { radius = 0.0; }

	// Constructor #2
	Circle(double r) { radius = r; }

	// Accessors
	double getRadius() const { return radius; }

	// Calculations
	double getArea() const { return M_PI * pow((radius), 2.0); }
};
#endif 


