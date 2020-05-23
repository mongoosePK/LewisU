/*William Pulkownik
  12 APR 2016
  StockLookUp.cpp
  Descr: a program that reads stock information in to dynamic parallel arrays
		using pointers
*/

#include <iostream>
#include <string>
#include <fstream>
#include <cctype>
#include <iomanip>
using namespace std;


bool openFile(fstream &file, string name)
{
	bool status;
	file.open(name, ios::in);
	if (file.fail())	
		status = false;
	else
		status = true;
	return status;
}

void selectionSort(string arr[], int size)
{
	int startScan, index, minIndex;
	string minValue;
	for (startScan = 0; startScan < (size - 1); startScan++)
	{
		index = startScan;
		minIndex = startScan;
		minValue = arr[startScan];
		for (index = startScan + 1; index < size; index++)
		{
			if (arr[index] < minValue)
			{
				minValue = arr[index];
				minIndex = index;
			}
		}
		arr[minIndex] = arr[startScan];
		arr[startScan] = minValue;
	}
}
void toUpper(string& symb)
{
	for (int i = 0; i < symb.length(); i++)
		symb[i] = toupper(symb[i]);
}
int symbolSearch(string symArr[], string user, int size)
{
	bool found = false;
	int position = -1;
	int index = 0;
	while (!found && index < size)
	{
		if (symArr[index] == user)
		{
			found = true;
			position = index;
		}
		index++;
	}
	return position;
}

int main()
{
	string fname, symbol;
	fstream myFile;

	bool status;
	int numStock;

	cout << "Enter the filename: ";
	cin >> fname;
	status = openFile(myFile, fname);
	if (status == false)
	{
		cout << "The file you chose cannot be opened.";
		exit(-1);
	}
	myFile >> numStock;

	string* symbols = new string[numStock];
	string* names = new string[numStock];
	int* shares = new int[numStock];
	float* prices = new float[numStock];
	int count = 0;
	while (count < numStock && !myFile.eof())
	{
		myFile >> symbols[count];
		getline(myFile, names[count], '#');
		myFile >> shares[count];
		myFile >> prices[count];
		count++;
	}
	//close file
	myFile.close();
	//create pointer to symbols.... sort pointer array
	string* stockPtr = new string[numStock];
	for (int j = 0; j < numStock; j++)
		stockPtr[j] = symbols[j];
	selectionSort(stockPtr, numStock);

	// display sorted stock selection
	cout << "available stocks: " << endl;
	for (int i = 0; i < numStock; i++) {
		cout << stockPtr[i] << ' ';
		if ((i + 1) % 3 == 0)
			cout << endl;
	}
	cout << endl;

	//accept user search
	cout << "Enter the symbol: ";
	cin >> symbol;
	toUpper(symbol);
	int searchIndex = symbolSearch(symbols, symbol, numStock);
	cout << fixed << setprecision(2);
	if (searchIndex < 0)
		cout << "Stock not found" << endl;
	else
	{
		cout << left << setw(30) << "Company Name: " << setw(25) << right<< names[searchIndex] << endl;
		cout << left << setw(30) << "Number of Shares: " << setw(25) << right << shares[searchIndex] << endl;
		cout << left<< setw(30) << "Current Price (per share): " << setw(25) << right << prices[searchIndex] << endl;
		cout << left<< setw(30) << "Current Value: " << setw(25) << right << shares[searchIndex] * prices[searchIndex] << endl;
	}
	delete[] symbols;
	delete[] names;
	delete[] shares;
	delete[]prices;
	delete[] stockPtr;
	return 0;
}

/*
Enter the filename: C:\Users\William\Desktop\P3_stkPort.txt
available stocks:
BA F HD
MCD WMT
Enter the symbol: hd
Company Name:                      The Home Depot, Inc.
Number of Shares:                                    31
Current Price (per share):                       115.54
Current Value:                                  3581.74
Press any key to continue . . .
*/