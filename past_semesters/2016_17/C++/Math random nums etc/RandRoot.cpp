/*
	RandRoot.cpp
	William Pulkownik
	3 Feb 2016
	This program generates a random number then displays the sqaure root.
*/

#include <ctime>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
using namespace std;

int backup() 
{
	// variable to hold user input max and random number
	int max, rNum;
	// get system time 
	unsigned int seed = time(0); 
	// seed the rand num gen
	srand(seed);
	cout << "random number is " << rand() << endl;
	// get maximum from user
	cout << "Please input a positive maximum integer number: ";
	cin >> max;
	
	//generate a random number between zero and the max
	rNum = rand() % abs(max);
	cout << "Random number between 0 and " << abs(max) << " is " << rNum << endl;
	//display sqRt of rand num
	cout << fixed << setprecision(2);
	cout << "Square root is " << sqrt(static_cast<double>(rNum)) << endl;
	return 0;
}