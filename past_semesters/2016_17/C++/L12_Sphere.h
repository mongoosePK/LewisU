/*
     FILE:   Sphere.h
	 AUTHOR: William Pulkownik
	 DATE:   12 MAY 2016
	 DESCR:
	 This is the definition of the base Sphere class.
*/

#include "L12_Circle.h"

#ifndef SPHERE_H
#define SPHERE_H

class Sphere: public Circle
{
public:
	//default constructor
	Sphere() : Circle() {radius = 0.0;}
	//parameter constructor
	Sphere(double r) : Circle(r) {radius = r;}

	//functions to calculate area and volume of sphere
	double getArea() const { return 4 * M_PI * pow((radius), 2.0); }
	double getVolume() const { return (4/3.0f) * M_PI * pow((radius), 3.0); }
};
#endif


