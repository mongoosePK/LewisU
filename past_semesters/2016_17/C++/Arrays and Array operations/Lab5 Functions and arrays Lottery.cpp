/*
     FILE:   Lab 5.cpp
	 AUTHOR: William Pulkownik
	 DATE:   2MAR2016
	 DESCR:
	 Lab Assignment
*/

#include <iostream>
#include <string>
#include <ctime>
#include <cmath>
using namespace std;

void generateNumbers(int lottery[], int size);
int checkMatches(int lottery[], int user[], int size); 
int main()
{
	int lottery[5], user[5];
	int matches;
	const int SIZE = 5;	
	cout << "Please enter your picks (numbers 0-9): " << endl;
	for (int i = 0; i < SIZE; i++)
		cin >> user[i];
	cout << "Here are your picks: ";
	for (int iVar : user)
		cout << iVar << ' ';
	cout << endl;
	generateNumbers(lottery, SIZE);
	cout << "Here are the lottery numbers: ";
	for (int iVar : lottery)
		cout << iVar << ' ';
	cout << endl;
	matches = checkMatches(lottery, user, SIZE);
	cout << "You matched " << matches << " numbers." << endl;
	if (matches == 5)
		cout << "You hit the JACKPOT";
	
	return 0;
}

void generateNumbers(int lottery[], int SIZE)
{
	unsigned seed = time(0);
	srand(seed);
	for (int i = 0; i < SIZE; i++)
		lottery[i] = rand() % 10 + 0;

}

int checkMatches(int lottery[], int user[], int SIZE)
{
	int matches = 0;
	for ( int i = 0 ; i < SIZE ; i++)
	{
		if (lottery[i] == user[i])
		matches++;
	}
	return matches;
}

/*
Please enter your picks (numbers 0-9):
2
5
4
6
9
Here are your picks: 2 5 4 6 9
Here are the lottery numbers: 7 7 3 2 9
You matched 1 numbers.
Press any key to continue . . .

*/