/*
William Pulkownik
Lab3.cpp
CIS 2541
7 FEB 2016
This Program creates an addition problem for a student-users then verifies the answer
*/

#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <ctime>
using namespace std;

int main()
{
	int ans, rNum1, rNum2;
	unsigned seed = time(0);
	srand(seed);
	
	rNum1 = rand() % 401 + 100;
	rNum2 = rand() % 401 + 100;
	cout << "Welcome to the Addition Tutor App." << endl;
	cout << "Please solve the following problem and enter your answer." << endl;
	cout << " " << rNum1 << endl;
	cout << "+" << rNum2 << endl;
	cout << setfill('-') << setw(5) << " " << endl;
	cout << " ";
	cin >> ans;
	if (ans == rNum1 + rNum2)
	{
		cout << "Awesome Job! \n";
		cout << "Come Back Soon!! \n";
	}
	else 
	{
		cout << "Try Again \n";
		cout << "The correct answer is " << rNum1 + rNum2 << endl;
	}
	return 0;
}

/*Welcome to the Addition Tutor App.
Please solve the following problem and enter your answer.
 240
+188
----
 999
Try Again
The correct answer is 428
Press any key to continue . . .

Welcome to the Addition Tutor App.
Please solve the following problem and enter your answer.
 413
+480
----
 893
Awesome Job!
Come Back Soon!!
Press any key to continue . . .
*/