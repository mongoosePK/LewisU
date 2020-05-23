/*
     FILE:   L11_UseCircle.cpp
	 AUTHOR: William Pulkownik
	 DATE:   04 MAY 2016
	 DESCR:
	 This is a client file for the
	 Circle class.
*/

// specification file
#include "L11_Circle.h"

int main() {
	// output number of circle objects
	cout << "There exists " << Circle::getNumObj() << " Circles in my unvierse at this moment.\n";
	// create circle objects
	Circle c1("c1", 4.0, 1, 1), c2(c1), c3;
	// reset c2 properties
	c2.setName("c2");
	c2.setDiameter(6.0);
	// assign c2 properties to c3
	c3 = c2;
	// reset c3 properties
	c3.setName("c3");
	c3.setDiameter(8.0);
	// display circles
	cout << "**Circles***" << endl;
	cout << c1 << c2 << c3;
	// output number of circle objects
	cout << "There exists " << Circle::getNumObj() << " Circles in my unvierse at this moment.\n";
	return 0;
}

//There exists 0 Circles in my unvierse at this moment.
//**Circles***
//c2 diameter = 4.00 area = 12.57
//c2 diameter = 6.00 area = 28.27
//c3 diameter = 8.00 area = 50.27
//There exists 3 Circles in my unvierse at this moment.
//Press any key to continue . . .