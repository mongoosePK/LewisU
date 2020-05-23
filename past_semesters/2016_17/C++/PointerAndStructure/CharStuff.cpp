/*
William pulkownik
CharStuff.cpp
4Apr2016
*/

#include <iostream>
using namespace std;

int main()
{
    char testString[] = "TESTING";
    cout << "length of" << testString << " is " << strlen(testString) << endl;
    cout << "num elements is " << sizeof(testString)/sizeof(char) << endl;
    const int SIZE = 20;
    char inpCStr[SIZE + 1];
    cout << "input a C sfloating point number: ";
    
	cin.getline(inpCStr, SIZE +1);
	cout << "length of" << inpCStr << " is " << strlen(inpCStr) << endl;
    cout << "num elements is " << sizeof(inpCStr)/sizeof(char) << endl;
    // create new string consisting of combined lengths
    char *combinedStr = new char[strlen(testString) + strlen(inpCStr) + 1];
    //copy string
    strcpy(combinedStr, testString);
    strcat(combinedStr, inpCStr);
    cout << "length of" << combinedStr << " is " << strlen(combinedStr) << endl;
    char *cStrPtr = strstr(combinedStr, "sample");
    if(cStrPtr)
        cout << "substring found" << endl;
	else
        cout << "substring not found" << endl;
    float fVar = atof(inpCStr);
    cout << "converted float value is " << fVar << endl;
    //release memory
    delete [] combinedStr;
    return 0;
}

/*
int charStuff(){
    int inpChar;
    cout << "Please input a character: ";
    cin.get(inpChar);
    if(isalpha(inpChar)){
        cout << inpChar<< " is a letter of the alphabet." << endl;
        if(islower) //without static cast you get the ASCII euiv
            cout << static_cast<char>(toupper(inpChar)) << " is the uppercase equivalent" << endl;
	}
    if(isalnum(inpChar))
        cout << inpChar << " is a letter of the alphabet or a digit." << endl;
    if(isprint(inpChar))
        cout << inpChar<< " is  a printable character." << endl;

    return 0;
}*/