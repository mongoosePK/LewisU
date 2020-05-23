/*
     FILE:   L11_CarStruct.cpp
	 AUTHOR: William Pulkownik
	 DATE:   20 Apr 2016
	 DESCR:
	 CIS-2541 Lab #8
	 Create and use a Car structure variable to hold the
	 details of a Car: make, model, year, and cost.
*/

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

enum Purpose {BUSINESS = 1, PERSONAL = 2};
// Car structure definition
struct Car
{
	string carMake;
	string carModel;
	int yearModel;
	double cost;
	Purpose prp;
};



// function with Car parameter
void displayCar (Car c) {
	cout << "\n**Car Information**" << endl;
	cout << "Make: " << c.carMake << endl;
	cout << "Model: " << c.carModel << endl;
	cout << "Year: " << c.yearModel << endl;
	cout << "Cost: " << fixed << setprecision(2) << c.cost << endl;
	switch(c.prp) {
	case BUSINESS:
		cout << "BUSINESS" << endl;
		break;
	case PERSONAL:
		cout << "PERSONAL" << endl;
		break;
	}
	return;
}

Car getCar() {
	string carMake;
	string carModel;
	int yearModel;
	double cost;
	int purpose;
	Car c;
	cout << "\n\tInput make: ";
	cin >> c.carMake;
	cout << "\n\tInput model: ";
	cin >> c.carModel;
	cout << "\n\tInput model year: ";
	cin >> c.yearModel;
	cout << "\n\tInput cost: ";
	cin >> c.cost;
	cout << "\n\tWhat is your car's purpose (1-Business, 2-Personal)";
	cin >> purpose;
	c.prp = static_cast<Purpose>(purpose);
	return c;
}



int main(void)
{
	// create array of Car structures with first 3 initialized
	Car carArray[10] = {{"Ford", "Taurus", 1997, 21000, BUSINESS},
						{"Honda", "Accord", 1992, 11000, BUSINESS},
						{"Lamborghini", "Aventador", 2011, 390000, PERSONAL}};
	carArray[3] = getCar();

	// loop and display array elements
	for(int i = 0; i < 4; i++)
		displayCar(carArray[i]);

	return 0;
}

/*

        Input make: Honda

        Input model: CRX

        Input model year: 1990

        Input cost: 600

        What is your car's purpose (1-Business, 2-Personal)2

**Car Information**
Make: Ford
Model: Taurus
Year: 1997
Cost: 21000.00
BUSINESS

**Car Information**
Make: Honda
Model: Accord
Year: 1992
Cost: 11000.00
BUSINESS

**Car Information**
Make: Lamborghini
Model: Aventador
Year: 2011
Cost: 390000.00
PERSONAL

**Car Information**
Make: Honda
Model: CRX
Year: 1990
Cost: 600.00
PERSONAL
Press any key to continue . . .
*/