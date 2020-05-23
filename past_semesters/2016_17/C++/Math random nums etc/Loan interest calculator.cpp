/*
FILE:   ProgramAssignment1.cpp
AUTHOR: William Pulkownik
CIS 2541
DATE:   01/27/2016
Assgnmnt:
Monthly payment calculator
*/

#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main()
{
	// initialize variables
	float rate, annRate, L, payment, amt;
	int N;
	// greet user and accept input values
	cout << "Welcome to the loan payment calculator." << endl;
	cout << "Please enter the amount of your loan: ";
	cin >> L;
	if(L >= 0)
	{
		cout << "Please enter the annual interest rate on the loan as a percent: %";
		cin >> annRate;
		cout << "enter the number of payments: ";
		cin >> N;

		// perform calculations
		rate = (annRate / 12) * .01;
		payment = (rate * pow(1 + rate, N) * L) / (pow(1 + rate, N) - 1);

		//format output
		cout << fixed << setprecision(2);
		cout << left;
		// output
		cout << setw(30) << "Loan amount: " << "$ " << setw(10) << right << L << endl;
		cout << left << setw(30) << "Annual interest rate: " << setw(10) << right <<  annRate << "%" << endl;
		cout << left << setw(30) << "Number of payments: " << setw(10) << right << N << endl;
		cout << left << setw(30) << "Monthly payment: " << "$ " << setw(10) << right << payment << endl;
		cout << left << setw(30) << "Amount paid back: " << "$ " << setw(10) << right << payment * N << endl;
		cout << left << setw(30) << "Interest paid: " << "$ " << setw(10) << right << (payment * N) - L << endl;
	}
	else
	{
		cout << "this program does not recognize negative loans" << endl;
	}
	return 0;
}

/*
Welcome to the loan payment calculator.
Please enter the amount of your loan: 10000
Please enter the annual interest rate on the loan as a percent: %12
enter the number of payments: 36
Loan amount:                  $   10000.00
Annual interest rate:              12.00%
Number of payments:                   36
Monthly payment:              $     332.14
Amount paid back:             $   11957.15
Interest paid:                $    1957.15
Press any key to continue . . .
*/