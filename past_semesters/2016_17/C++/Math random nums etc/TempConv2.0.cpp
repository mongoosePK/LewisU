/*
   FILE:   TempConv.cpp
   AUTHOR: 
   DATE:   01/27/2016
   DESCR:
   This program performs a fahrenheit to celsius
   temperature conversion.
*/

#include <iostream> // pre-processor directives are not C++ statements. c++ statements end with semicolons
#include <string>
#include <iomanip>
using namespace std;

int main () 
{
	// variables to hold data numeric and character
	float fahr, cels;
	string name;
	char hotOrCold;
	// constant conversion factor *auto* sets type to used type in variable 
	const auto CNV_FCTR = 5.0f/9;
	cout << "Please input your name: ";
	getline(cin, name); // cin is 'c input'
	
	// fahr = 212; // OBSOLETE initialize fahrenheit
	// the slash-n terminates the line making endl unneeded
	string greeting = "Fahrenheit to Celsius Conversion\n";
	cout << "Welcome " << name << '\n' << greeting;
	//prompt user for F temp input
	cout << "Please input a Farenheit temp to convert: ";
	cin >> fahr;
	//clear out input stream
	cin.ignore();
	cout << "is this tempo hot or cold (H or C): ";
	cin.get(hotOrCold);
	// convert temperature to celsius
	cels = CNV_FCTR * (fahr - 32);
	//modify output format with showpoint, fixed (more precise), or setprecision(n)
	cout << fixed << setprecision(2);
	// output original and converted value
	cout << setw(30) << "Fahrenheit = " << setw(10) << fahr << endl;
	cout << setw(30) << "Celsius = " << setw(10) << cels << endl; // '/t' tabs the output. setw(n) width. left or right align affects later ouput
	cout << "this temp is " << hotOrCold << endl;
	return 0;
}
