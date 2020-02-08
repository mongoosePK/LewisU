// File: ElapsedTime.cpp

#include <iostream>
#include <ctime>
#include <stdlib.h>


using namespace std;
int count;
int main()
{
	int todayseconds = time(0);
    system ("date /T");
		{
			
		    cout << " since 1970, Jan 1, Midnight, GMT " << todayseconds <<  endl;
	
		}

    int currentmins = todayseconds / 60; 
    cout << " currentmins " << currentmins << endl;
    int currentseconds = todayseconds % 60;
    cout << " currentseconds " << currentseconds << endl;
	int currenthours = currentmins / 60;
	cout << " currenthours  "  << currenthours << endl;
    currentmins = currentmins % 60;
    cout << " currentmins  "  << currentmins << endl;
    int days = currenthours / 24;
    cout << " days  " << days << endl;
    currenthours = currenthours % 24;
    cout <<  " currenthours  "  << currenthours << endl;
    int years = days / 365;
    cout << " years " << years << endl;
	int currentday =  days % 365;
	cout << " currentday " << currentday << endl; 	
	cout <<   "current year " << years + 1970 <<"  day " << currentday << endl;
	cout << " approx month " << currentday / 30 << endl;
	return 0; 
}
/*
 Wed 09/26/2018
 since 1970, Jan 1, Midnight, GMT 1537939141
 currentmins 25632319
 currentseconds 1
 currenthours  427205
 currentmins  19
 days  17800
 currenthours  5
 years 48
 currentday 280
current year 2018  day 280
 approx month 9

--------------------------------
Process exited after 0.08904 seconds with return value 0
Press any key to continue . . .
--------------------------------
Process exited after 0.07154 seconds with return value 0
Press any key to continue . . .

*/

 


