/*
William Pulkownik
z1805341
CSCI_340_003
Assignment4.cc
Due: EXTENDED DUE TO ILLNESS
*/

#include <stack>
#include <queue>
#include <iostream>
#include <string>
#include <iomanip>
#include "assignment4.h"

using std::setw;
using std::cin;
using std::endl;
using std::cout;
using std::cerr;
using std::string;



bool Stack::empty() const {
	return (q1.empty() && q2.empty());
}

int Stack::size() const {
	return (q1.size() + q2.size());
}

int Stack::top() {
	return (q1.empty() ? q2.back() : q1.back());
}

void Stack::push(const int& val) {
	(q1.empty() ? q2.push(val) : q1.push(val));
}

void Stack::pop() {
	
	if (q1.empty())
	{
		for (size_t i = 0; i < q2.size(); i++)
		{
			q1.push(q2.front());
			q2.pop();
		}
		q2.pop();
	}
	else if (q2.empty())
	{
		for (size_t i = 0; i < q1.size(); i++)
		{
			q2.push(q1.front());
			q1.pop();
		}
		q1.pop();
	}
}

int main() {
	Stack s;
	string op;
	int val = 0;

	cout << "operation -- size front end" << endl;
	cin >> op;
	while (!cin.eof()) {
		if (op == "push") {
			cin >> val;
			s.push(val);
			cout << op << " " << val << "    -- ";
		}
		else if (op == "pop") {
			s.pop();
			cout << op << "       -- ";
		}
		else {
			cerr << "Error input: " << op << endl;
			return 1;
		}
		cout << setw(3) << s.size() << setw(5) << s.top() << endl;
		cin >> op;
	}

	while (!s.empty())
		s.pop();
	cout << "End -- size of Stack is: " << s.size() << endl;

	return 0;
}
