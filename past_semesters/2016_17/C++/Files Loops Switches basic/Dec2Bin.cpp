#include <string>
using namespace std;

/*
 Function:   Dec2Bin
 Parameters: int -- value representing integer base 10 number
 Returns:    string -- value representing input number converted to base 2
 Descr:      convert input decimal number to binary by successively
             dividing number by 2 and creating a string of remainder
			 digits
*/
string Dec2Bin(int decNum) {
	string biNum;   // string to hold binary number
	char hold;      // character to hold binary digit
	// loop until all powers of 2 have been extracted
    while(decNum != 0)
    {
		// get remainder
        hold = decNum % 2 + '0';  // get ASCII value for number
        biNum = hold + biNum;     // add character to binary number
		// remove power of 2
        decNum /= 2;
    }
	return biNum;
}