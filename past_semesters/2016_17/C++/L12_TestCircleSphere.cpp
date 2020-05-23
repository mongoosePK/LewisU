/*
     FILE:   L12_TestCircleSphere.cpp
	 AUTHOR: William Pulkownik
	 DATE:   12 MAY 2016
	 DESCR:
	 This is a test program for the Circle and
	 Sphere classes.
*/

#include <iostream>
#include "L12_Circle.h"
#include "Sphere.h"
using namespace std;

int main()
{
   double radius;   // To hold the sphere's radius

   // Get the radius from the user
   cout << "Enter a radius..." << endl;
   cout << "Radius: ";
   cin >> radius;

   // Define a Circle object and use the dimension
   // entered by the user.
   Circle myCircle(radius);

   // Define a Sphere object and use the dimension
   // entered by the user.
   Sphere mySphere(radius);

   // Display the Circle object's properties.
   cout << "\nHere are the Circle's properties:\n";
   cout << "Radius: " << myCircle.getRadius() << endl;
   cout << "Area: " << myCircle.getArea() << endl;

   // Display the Sphere object's properties.
   cout << "\nHere are the Sphere's properties:\n";
   cout << "Radius: " << mySphere.getRadius() << endl;
   cout << "Surface Area: " << mySphere.getArea() << endl;
   cout << "Volume: " << mySphere.getVolume() << endl;

   return 0;
}

/*
Enter a radius...
Radius: 5.25

Here are the Circle's properties:
Radius: 5.25
Area: 86.5901

Here are the Sphere's properties:
Radius: 5.25
Surface Area: 346.361
Volume: 606.131
Press any key to continue . . .
*/