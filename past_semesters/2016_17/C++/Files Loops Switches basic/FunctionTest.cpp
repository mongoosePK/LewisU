/* William Pulkownik
   22 FEB 2016
   FunctionTest.cpp
   Description : example of function used to convert temperatures
   */

#include <iostream>
#include <iomanip>
using namespace std;

//global constant
const float FTOC_FACTOR = 5.0f/9; //5.0 is double by default... 5.0f is float, using less memory

// function prototype to satisfy compiler errors
float ftoc(float = 212.0f);
void menuPrompt(); 
void getVal(char&);
void getVal(float&);
// main controlling function
int main()
{
	float inpFahr, outCels;
	char inpChar;
	menuPrompt();
	getVal(inpChar);

	if (toupper(inpChar) == 'F')
	{
		cout << "Please input a fahrenheit valut to convert to Celsius : ";
		getVal(inpFahr);
		outCels = ftoc(inpFahr);
		cout << "Celsius = " << outCels << endl;
	}
	else
	cout << "default call ftoc = "<< ftoc() << endl;
	
	return 0;
}

// ftoc function definition
/* Function name ftoc
Parameters: fahr -- float
Return: cels -- float
descr: takes F and converts to C [ cels = 5 * (fahr - 32) / 9 
*/

float ftoc(float fahr)
{
	float cels;
	cels = FTOC_FACTOR * (fahr - 32);
	return cels;
}

void getVal(char& cVar)
{
	cin.get(cVar); //cin.get only works with characters
}

void getVal(float& fVar)
{
	cin >> fVar;
}