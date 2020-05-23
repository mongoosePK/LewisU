/*
     FILE:   CPPStringStuff.cpp
	 AUTHOR: William Pulkownik
	 DATE:   6APR2016
	 DESCR:
	 This is a sample program to demonstrate the use of
	 C++ strings.
*/

#include <iostream>
#include <string>
using namespace std;

int min(void)
{
	// use debugger to view
	string greeting;
	string greeting1("hi there");
	string greeting2("hi there", 2);
	string welcome(greeting1);
	string welcome1(greeting1, 0, 2);
	string sleepy(10, 'z');
	cout << "PLease input a string:";
	// getline with arguments 
	// ** the getline function is part of <string>
	getline(cin, greeting, '#');
	// standard cin stops at whitespace
	// cin >> greeting;
	cout<< "you entered greeting " << greeting << endl;
	//concantonate strings with c++ string class
	greeting += " hi there"; 
	cout<< "greeting ammended to " << greeting << endl;
	//Index a string
	cout<< "first character is: " << greeting[0] << endl;
	cout<< "first character is: " << greeting.at(0) << endl;
	cout<< "greeting length " << greeting.length() << endl;
	cout<< "greeting size " << greeting.size() << endl;
	cout<< "Capacity " << greeting.capacity() << endl;
	cout<< "front character is " << greeting.front() << endl;
	// read and append an integer
	int i;
	//cin.ignore arguments "ignores" 100 chars of standard input 
	// or until new line by dumping the buffer
	cin.ignore(100, '\n');
	cout << "enter an integer value: ";
	cin >> i;
	greeting += to_string(i);
	cout << "Your concatenated string is : "<< greeting << endl;
	cout<< "Which is " << greeting.length() << " characters." << endl;
	cout<< "with potential Capacity of " << greeting.capacity() << endl;

	return 0;
}
