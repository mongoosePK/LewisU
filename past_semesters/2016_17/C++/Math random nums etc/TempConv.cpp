/*
  FILE: TempConv.cpp
  Author: William Pulkownik
  27JAN2015
  Description: This program performs a F to C temp conversion
*/

#include <iostream> // preprocessor directives are not C++ statements. c++ statements end with semicolons
#include <string>
using namespace std;

int main() 
{
	// variables to hold data
	float fahr, cels;
	// constant conversion factor
	const auto CNV_FCTR = 5/9.0; 
	fahr = 212;
	string greeting = "Farenheit to Celcius Converter";
	cout << greeting << endl;
	//convert temp to C
	cels = CNV_FCTR * (fahr - 32);
	//output original and converted value
	cout << "Farenheit = " << fahr << " degrees" << endl;
	cout << "Celcius = " << cels << " degrees" << endl;
	return 0;
}

