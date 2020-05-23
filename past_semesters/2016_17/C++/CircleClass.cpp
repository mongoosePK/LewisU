/* William Pulkownik
27 Apr 2016
CircleClass.cpp
CIS 2541
IMPLEMENTATION FILE FOR CIRCLE CLASS
*/

#include "Circle.h"

//default constructor
Circle::Circle() {
	radius = 0;
	pi = 3.14159;
}
//constructor
Circle::Circle(double r) {
	radius = r;
	pi = 3.14159;
}
//destructor
Circle::~Circle(){}

void Circle::setRadius(double r){
	radius = r;
}
double Circle::getArea(){
	return pi*radius*radius;
}
double Circle::getDiameter(){
	return radius*2;
}
double Circle::getCircumference(){
	return 2*pi*radius;
}
