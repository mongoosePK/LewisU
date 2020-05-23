/*
William Pulkownik
Cube.h
9May2016
defihnition of inheritedd cube class from parent rectangle class
*/

#ifndef CUBE_H
#define CUBE_H

#include "Rectangle.h"

class Cube: public Rectangle {
private:
    double height;
public:
	Cube() : Rectangle() { height = 0.0; }
	double getHeight() const { return height; }
	Cube(double w, double len, double h) : Rectangle(w, len) { height = h;}
	double getArea() const { return 2 * (width * length) + 2 * (width *height) + 2* (length * height);}
	double getVolume() const {return length * width * height;}
};
#endif