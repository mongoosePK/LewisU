// 
// NAME:William Pulkownik
// DATE: 6Apr 2016
// PROGRAM: L7_WordCounter.cpp
// DESCR:
// Chapter 10, Programming Challenge 3: Word Counter
//

#include <iostream>
#include <string>
using namespace std;

// Function Prototype
int wordCount (char *userEntry, int MAX_LENGTH)
{
	int i = 0;
	int counter = 0;
	while (userEntry[i] != '\0')
	{
		if (userEntry[i] == ' ')
			counter++;
		i++;
	}
	
	return counter;
}

int main()
{
    // Constants
    const int MAX_LENGTH = 150;

    // Local variables
    char userWords[MAX_LENGTH+1] ;
    int wCount = 0;
	char* cStr = userWords;

	

    // Get the user input line of text.
	cout << "Enter text less than or equal to " << MAX_LENGTH << " characters: \n";
	cin.getline(userWords, MAX_LENGTH+1);

    
	// Count the number of words entered.
    wCount = wordCount (cStr, MAX_LENGTH);
	cout << "There are " << wCount + 1 << " words in your sentence." << endl;

    // Display the number of words entered
    //cout << "\nNumber of words in the entered text is: " << wCount << endl;
    return 0;
}

/*
Enter text less than or equal to 150 characters:
hi there england
There are 3 words in your sentence.
Press any key to continue . . .
*/