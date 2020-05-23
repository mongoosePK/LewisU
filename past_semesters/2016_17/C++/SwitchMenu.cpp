/* 
William Pulkownik
10 Feb 2016

In class switch example: multi branch

*/

#include <iostream>

using namespace std;

int main()
{
	char inpChar;
	cout << "Input your class status \n"
		<< "\t (F)reshman, So(P)homore, (J)unior, (S)enior: ";
	cin >> inpChar;
	//display type
	switch (inpChar) 
	{
	case 'f' :
	case 'F' :
		cout << "You are a Freshman \n";
		break;
	case 'P' :
	case 'p' :
		cout << "You are a Sophomore \n";
		break;
	case 'J' :
	case 'j' :
		cout << "You are a junior \n";
		break;
	case 'S' :
	case 's' :
		cout << "Jigga, You made it \n";
	}

	return 0;
}