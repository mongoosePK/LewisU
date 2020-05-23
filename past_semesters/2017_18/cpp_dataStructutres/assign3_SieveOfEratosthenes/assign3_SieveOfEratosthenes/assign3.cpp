/*
William Pulkownik
z-1805341
CSCI_340_003
Due:Feb/Mar - Extended due to illness
assignment3.cc

*/

#include <iostream>
#include <set>
#include <iomanip>
#include <string>
#include <iterator>

using std::set;
using std::iterator;
using std::cout;
using std::cin;
using std::string;

// sieve() is the actual algorithm. it removes all non-prime numbers from the set 's' by finding multiples of 2,
// removing them, and repeating with successive numbers that are left and less than the upper bound . 
void sieve(set<int>& s, const int lower, const int upper) {
	set<int>::iterator it;
	int m = 2;
	// the first loop increments m (the prime surrogate) and makes sure it's square isn't larget than upper
	// the second loop iterates through the set
	// if the iterator is a factor of m but not m itself it is erased
	for (m; m*m < upper + 1; ++m) {
		for (it = s.begin(); it != s.end(); ) {
			if (*it != m && *it % m == 0) {
				set<int>::iterator pre = it++; // if iterator is not prime, copy it, increment it, delete copy
				s.erase(pre);
			}
			else { ++it; }
		}
	}
}
// print_primes takes the set and bounds and prints the set's contents using modulo for 8-column rows of width=6
void print_primes(const set<int>& s, const int lower, const int upper) {
	int colCount = 1;
	cout << "\n" << "there are " << s.size() << " prime numbers between " << lower << " and " << upper << ":\n";
	for (set<int>::iterator i = s.begin(); i != s.end(); i++)
	{
		if (*i >= lower) {
			cout << std::setw(6) << *i;
			if ((colCount) % 8 == 0) 
				cout << std::endl;
			colCount += 1;
		}
	}
	cout << "\n";
}
// run_game loops while user does not answer "no". the function takes user input, error checks the values for order.
// it constructs the set if lower < upper
// then it runs seive, print, and takes the user reply
void run_game(set<int>& s) {
	std::string line, Slower, Supper, reply; //string versions of lower and upper to use with getline and user reply

	while (reply != "no") {
		do {
			cout << "Please input lower bound and upper bound and hit enter (e.g. 10 100): ";
			std::getline(cin, line, ' ');
			Slower = line;
			std::getline(cin, line);
			Supper = line;
		} while (stoi(Slower) > stoi(Supper)); //error check
		int lower = (stoi(Slower)); //if everthing looks good, convert the strings to ints and  assign them
		int upper = (stoi(Supper));
		// construct the set
		for (int i = lower; i <= upper; i++)
			s.insert(i);
		sieve(s, lower, upper); //call sieve
		print_primes(s, lower, upper); // call print function
		s.clear(); //empty set for future use
		cout << "Do you want to continue or not? Please answer yes or no and hit enter : ";
		cin >> reply;
		
	}
}

int main() {
	set<int> s;
	run_game(s);
	return 0;
}
