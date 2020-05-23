// aboutTime.cpp
#include <iostream>
#include <time.h>
#include <iomanip>
#include <chrono>
// see http://pubs.opengroup.org/onlinepubs/007908775/xsh/time.h.html
using namespace std;
using namespace std::chrono;

int main ()
{

	cout << "\nI am going to do a lot, napping, driving forbiden\n\n";
		
	auto start = high_resolution_clock::now();
	for (int i = 0; i < 999999; i++)
    {
		cout << i << endl;
    } 
	auto stop = high_resolution_clock::now();
	auto difference = duration_cast<microseconds>(stop - start);
	
	cout << "Actual time of rest (after nap)is: " << difference.count() << endl;
	
	return 0;
}
	
	
	                          