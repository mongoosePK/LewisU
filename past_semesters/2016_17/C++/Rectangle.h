/*
     FILE:   Rectangle.h
	 AUTHOR: 
	 DATE:   MM/DD/YYYY
	 DESCR:
	 This is the definition of the base Rectangle class.
*/

#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle
{
protected:
	double width;
	double length;
public:
	// Default constructor
	Rectangle() { width = 0.0; length = 0.0; }

	// Constructor #2
	Rectangle(double w, double len)
	{ width = w; length = len; }

	// Accessors
	double getWidth() const { return width; }
	double getLength() const { return length; }

	// Calculations
	double getArea() const { return width * length; }
};
#endif 