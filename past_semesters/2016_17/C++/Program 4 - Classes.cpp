#include "Program 4.h"
#include <fstream>

// function prototypes
int ReadStkData(Stock stks[], int maxSize);
void SortStks(Stock stks[], int size);
void CalculatePortfolio(Stock stks[], int size);

int main()
{
	const int MAXSIZE = 25;
	Stock stocks[MAXSIZE];
	int elementsRead = ReadStkData(stocks, MAXSIZE);
	// call sort
	SortStks(stocks, elementsRead);
	// create report
	CalculatePortfolio(stocks, elementsRead);
	return 0;
}
//This controlling function creates the needed variable
//parameters, calls the function to read the stock data
//from file, the function to sort the read stock data,
//and then the function to output the stock portfolio
//report to file.

int ReadStkData(Stock stks[], int maxSize)
{
	ifstream inFile;
    string fname;
    cout << "Please input the stock file to read: ";
    getline(cin, fname);
    inFile.open(fname, ios::in);
    if (inFile.fail())
    {
        cout << "Unable to open \"" << fname << "\" for input!" << endl;
        exit(-1);
    }
	int i = 0;
	while (!inFile.eof() && i < maxSize )
	{
		string trade, company;
		int sect;
		int shares;
		double purchP, currP;
	
			inFile >> trade;
			stks[i].setTrSymbol(trade); 

			getline(inFile, company, '#');
			stks[i].setCompanyName(company);

			inFile >> sect;
			stks[i].setSector(static_cast<Sector>(sect));

			inFile >> shares;
			stks[i].setShares(shares);

			inFile >> purchP;
			stks[i].setPurchasePrice(purchP);

			inFile >> currP;
			stks[i].setCurrentPrice(currP);
		i++;
	}
	inFile.close();
	return i;
}

// This function prompts the user for a file name
// reads data from the file (until end of file or maxSize has been reached)
// closes the file returns the number of elements read from the file.

void SortStks(Stock stks[], int size)
{
	bool swap;
    do
    {
        swap = false;
        for (int i = 0; i < (size - 1); i++)
        {
            if(stks[i].sector < stks[i + 1].sector)
            {
                Sector temp = stks[i].sector; 
                stks[i].sector = stks[i + 1].sector;
                stks[i + 1].sector = temp;
                swap = true;
            }
        }
    }
    while (swap);
}

//This function sorts the array of passed Stock objects
//according to increasing sector value.



// display through CONTROL BREAK REPORT/SUB SUMMARY REPORT
void CalculatePortfolio(Stock stks[], int size)
{
	ofstream outFile;
    string fname;
    cout << "Input the file to write to: ";
    getline(cin, fname);
    outFile.open(fname, ios::out);
    if (outFile.fail())
    {
        cout << "Unable to open \"" << fname << "\" for output!" << endl;
        exit(-1);
    }

	outFile << "Prepared Portfolio Analysis Summarized by Sector" << endl;
	outFile << "Long Term Capital Gain Tax Rate = 0.15\n\n";

	outFile << "Symbol" << setw(13)<< "Company" << setw(43) << "Status" << endl;
	outFile << "======" << setw(13)<< "=======" << setw(43) << "======" << endl;

	int i = 1;
	outFile << Stock::currStatus(stks[i].currentPrice, stks[i].purchasePrice);
	outFile << setw(40) << "Summary for Sector:\t" << endl;
	outFile << setw(40) << "Gain amount:\t" << endl;
	outFile << setw(40) << "Tax on gain:\t" << endl;

	
	
	outFile.close();
	cout << "Portfolio report has been created at: " << endl << fname << endl;
}

//This function prompts the user for a file name, opens
//the file, writes out the stock portfolio report to
//file, closes the file, and displays an output message
//to the user indicating the report has been created.