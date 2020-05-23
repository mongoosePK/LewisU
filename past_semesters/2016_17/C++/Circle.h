/* William Pulkownik
27 Apr 2016
Circle.h
CIS 2541
SPECIFICATION FILE
*/

#include <iomanip>
#include <iostream> 
#include <string>
using namespace std;

#ifndef CIRCLE_H
#define CIRCLE_H

class Circle {
private:
	double radius;
	double pi;

public:
	//constructors
	Circle();
	Circle(double);
	//destructor
	~Circle();
	//mutators-setters
	void setRadius(double);
	//getters
	double getRadius() const {return radius;}
	//calculation functions
	double getArea();
	double getDiameter();
	double getCircumference();
};

#endif