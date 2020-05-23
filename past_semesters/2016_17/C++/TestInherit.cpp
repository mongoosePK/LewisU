/*
     FILE:   TestInherit.cpp
	 AUTHOR: 
	 DATE:   MM/DD/YYYY
	 DESCR:
	 This is a test program for the 
	 Cube class.
*/

#include <iostream>
//#include "Rectangle.h" <-- dont need this because cube.h includes it
#include "cube.h"
using namespace std;

int main(){
   double recWidth;   // To hold the rectangle's width
   double recLength;  // To hold the rectangle's length
   double height;

   // Get the width and length of
   // the rectangle from the user.
   cout << "Enter the dimensions of a Rectangle:\n";
   cout << "Width: ";
   cin >> recWidth;
   cout << "Length: ";
   cin >> recLength;
   cout << "Height: ";
   cin >> height;
   // Define a Rectangle object and use the dimensions
   // entered by the user. then do it for a cube
   Rectangle myRec(recWidth, recLength);
   Cube myCube(recWidth, recLength, height);

   // Display the Rectangle object's properties.
   cout << "Here are the Rectangle's properties:\n";
   cout << "Width: " << myRec.getWidth() << endl;
   cout << "Length: " << myRec.getLength() << endl;
   cout << "Area: " << myRec.getArea() << endl;
   
   cout << "Here are the cube's properties:\n";
   cout << "Width: " << myCube.getWidth() << endl;
   cout << "Length: " << myCube.getLength() << endl;
   cout << "height:" << myCube.getHeight() << endl;
   cout << "Area: " << myCube.getArea() << endl;
   cout << "Volume: " << myCube.getVolume() << endl;
   return 0;
}