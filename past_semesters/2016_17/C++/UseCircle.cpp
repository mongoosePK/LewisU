/* William Pulkownik
27 Apr 2016
UseCircle.cpp
CIS 2541
DEMONSTRATION FILE
*/

#include "Circle.h"

void DisplayCircle(Circle c){
	cout << fixed <<  setprecision(3);
	cout << "The radius of your circle is " << c.getRadius() << endl;
	cout << "The area of your circle is " << c.getArea() << endl;
	cout << "The diameter of your circle is " << c.getDiameter() << endl;
	cout << "The circumference of your circle is " << c.getCircumference() << endl;
}


Circle GetCircle() {
	Circle c;
	double r;
	cout << "Please input a radius for a circle: ";
	cin >> r;
	c.setRadius(r);
	return c;
}
int main(){
	Circle c1 = GetCircle();
	DisplayCircle(c1);
	return 0;
}

/*
Please input a radius for a circle: 3.5
The radius of your circle is 3.500
The area of your circle is 38.484
The diameter of your circle is 7.000
The circumference of your circle is 21.991
Press any key to continue . . .
*/
