/*
author: William Pulkownik
class:  CSCI 340-03
due:	31 JAN 2016
program: assignment1
*/

//include libraries
#include <algorithm>
#include <vector>
#include <iostream>
#include <iomanip>
using std::setw;
using std::vector;
using std::cout;
using std::endl;
// set constants
const int DATA_RANGE = 100;
const int DATA_SIZE = 100;
const int DATA_SEED = 7;
const int SEARCH_SEED = 9;
// linear_search inspects each element of the input vector for integer X
// it modifies the comparisons total for each comparison, and quits searching if it gets a hit.
// returns true on success and false otherwise
bool linear_search(const vector<int>& inputVec, const int x, int& comparisons) {
	bool found = false;
	comparisons = 0;
	for (unsigned i = 0; i < inputVec.size(); i++)
	{
		comparisons++;
		if (inputVec[i] == x)
		{
			return found = true;
		}
	}
	return found;
}
// binary_search divides a sorted vector in half 
// compares the pivot point to the search value and divides again until found
// it counts comparisons and returns true of found
bool binary_search(const vector<int>& inputVec, const int x, int& comparisons) {
	
	bool found = false;
	int last = inputVec.size() - 1, first = 0, middle;
	comparisons = 0;
	while (first <= last && !found)
	{
		middle = (first + last) / 2;
		comparisons++;
		if (inputVec[middle] == x)
		{
			found = true;
		}
		else
			(inputVec[middle] < x ? first = middle + 1 : last = middle - 1);
	}

	return found;
}
// print_vec displays the elements of a vector with a simple loop
// 10 elements per line, column width == 6
void print_vec(const vector<int>& vec) {
	for (unsigned i = 0; i < vec.size(); i++)
	{
		cout << setw(6) << vec[i];
		if ((i + 1) % 10 == 0)
			cout << endl;
	}
}

void average_comparisons(const vector<int>& inputVec, const vector<int>& searchVec, bool(*search)(const vector<int>&, const int, int&)) {
	int i, comparison = 0, sum = 0, found = 0;
	bool res;
	for (i = 0; i<(int)searchVec.size(); i++) {
		res = search(inputVec, searchVec[i], comparison);
		sum += comparison;
		if (res)
			found++;
	}
	cout << found << " numbers are found. The average number of comparisons in each search: " << (double)sum / (double)searchVec.size() << endl << endl;
}

int random_number() {
	return rand() % DATA_RANGE + 1;
}

int main() {

	// -------- create unique random numbers ------------------//
	vector<int> inputVec(DATA_SIZE);
	srand(DATA_SEED);
	generate(inputVec.begin(), inputVec.end(), random_number);
	sort(inputVec.begin(), inputVec.end());
	vector<int>::iterator it = unique(inputVec.begin(), inputVec.end());
	inputVec.resize(it - inputVec.begin());
	random_shuffle(inputVec.begin(), inputVec.end());

	cout << "------ Data source: " << inputVec.size() << " unique random numbers ------" << endl;
	print_vec(inputVec);
	cout << endl;

	// -------- create random numbers to be searched ---------//
	vector<int> searchVec(DATA_SIZE / 2);
	srand(SEARCH_SEED);
	generate(searchVec.begin(), searchVec.end(), random_number);

	cout << "------ " << searchVec.size() << " random numbers to be searched: ------" << endl;
	print_vec(searchVec);
	cout << endl;

	cout << "Linear search: ";
	average_comparisons(inputVec, searchVec, linear_search);
	cout << "Binary search: ";
	average_comparisons(inputVec, searchVec, binary_search);

	sort(inputVec.begin(), inputVec.end());
	cout << "------- numbers in data source are now sorted ---------" << endl << endl;
	cout << "Linear search: ";
	average_comparisons(inputVec, searchVec, linear_search);
	cout << "Binary search: ";
	average_comparisons(inputVec, searchVec, binary_search);

	return 0;

}