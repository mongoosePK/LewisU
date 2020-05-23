/*
  FILE: Lab1.cpp
  Author: William Pulkownik
  27JAN2015
  Description:
*/

#include <iostream>
#include <string>
using namespace std;

int main() 
{
	float purch = 95;
	const float S_TAX = 0.04;
	const float C_TAX = 0.02;
	cout << "Lab 1" << endl;
	cout << "State Tax: $ " << purch * S_TAX << endl;
	cout << "County Tax: $ " << purch * C_TAX << endl;
	cout << "Total sale amount: $ " << purch + (purch * S_TAX) + (purch * C_TAX) << endl;
	return 0;
}


