/*
William Pulkownik
StockSales.cpp
CIS 2541
23 FEB 2016
Descr: Program that reads stock data from a file and computes profit
*/

#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>

using namespace std;
//function prototypes
float getProfit(int NS, float PP, float PC, float SP, float SC);
bool openFile(fstream& , string );

int main()
{
	int NS, allShares = 0;
	string stock, fileName;
	fstream(myFile);
	float SP, SC, PP, PC, profit, total = 0.0;
	bool status;
	cout << "Enter the file name: ";
	cin >> fileName;
	status = openFile(myFile , fileName);
	if (status == false)
	{
		cout << "there has been an error opening the file." << endl;
		exit(-1);
	}
	cout << "File successfully opened" << endl;
	cout << fixed << setprecision(2);
	cout << left;

	cout << setw(10) << "Stock" << setw(10) << "Shares" << setw(10) << "P Price" << setw(10) << "S Price" << setw(10) << "Profit (Loss)" << endl;
	cout << setw(10) << "-----" << setw(10) << "-----" << setw(10) << "-------" << setw(10) << "-------" << setw(10) << "-------------" << endl;
	
	while (!myFile.eof())
	{
		myFile >> stock >> NS >> PP >> PC >> SP >> SC;
		profit = getProfit(NS, PP, PC, SP, SC);
		cout<< left << setw(10) << stock << setw(5)<< right<< NS <<setw(12)<< PP <<setw(10)<< SP <<setw(16)<< profit << endl;
		total += profit;
		allShares += NS;
	}
	cout << endl;
	cout << "Your total Profit (or loss) on " << allShares <<" shares is $"<< total << endl;
	myFile.close();
	return 0;
}

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

float getProfit(int NS, float PP, float PC, float SP, float SC)
{
	float profit;
	profit = ((NS * SP) - SC) - ((NS * PP) + PC);
	return profit;
}

/*
Enter the file name: C:\Users\winxp\Desktop\P2_stocks.txt
File successfully opened
Stock     Shares    P Price   S Price   Profit (Loss)
-----     -----     -------   -------   -------------
AAPL         23      102.30     96.25         -157.05
GE           15       23.00     28.87           70.15
MSFT         30       58.50     52.06         -213.10
GOOG         10      540.20    695.03         1528.40

Your total Profit (or loss) on 78 shares is $1228.40
Press any key to continue . . .
*/
