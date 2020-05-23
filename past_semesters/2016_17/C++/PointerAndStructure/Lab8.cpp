/*
	File: StructStuff.cpp
	Author: William Pulkownik (via Matt Weiss)
	Date: 4/11/16
	Prog: Chapter 11
	Descr: In class exercise to practice use of structured data types.

*/

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

// Car structure declaration
struct Car {
	string make;
	string name;
	int year;
	double cost;
};

void showCar(Car c) {
	
	cout << setw(15) << left << c.make<< setw(15) << c.name << setw(15) << c.year << setw(15) << c.cost<< endl;
	
	return;
}

int main()
{
	const int size = 10;
	Car carArray[size] = {{"Ford", "Taurus", 1997, 21000.00} , {"Honda", "Accord", 1992, 11000.00}, {"Lamborghini", "Aventador", 2011, 390000.00}};
	cout<< "\n***Vehicle Information***\n";
	cout << setw(15) << left << "Make" << setw(15) << "Model" << setw(15) << "Year" << setw(15) << "Cost" << endl;
	cout << fixed << setprecision(2);
	for (int i = 0; i < 3;  i++)
		showCar(carArray[i]);		
	return 0;
}

/*

***Vehicle Information***
Make           Model          Year           Cost
Ford           Taurus         1997           21000.00
Honda          Accord         1992           11000.00
Lamborghini    Aventador      2011           390000.00
Press any key to continue . . .
*/