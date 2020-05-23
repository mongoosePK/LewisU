/*
William Pulkownik
4 May 2016
UseStock.cpp

*/

#include "Stock.h"

int ReadStk(Stock s[], int maxSize);
void SortStk(Stock s[], int size);
void CalculatePortfolio(Stock s[], int size);
string statName(int stat);
string displaySector(Sector k);
//function to return enum as string to portfolio


int main()
{
	const int MAXSIZE = 25;
	Stock stocks[MAXSIZE];
	int elementsRead = ReadStk(stocks, MAXSIZE);
	SortStk(stocks, elementsRead);
	CalculatePortfolio(stocks, elementsRead);
	return 0;
}

//this functions reads from stock file and creates an array of stock data
int ReadStk(Stock s[], int maxSize)
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
	while (!inFile.eof() && i < maxSize)
	{
		string sym, name;
		int num;
		int sec;
		float pur, cur;

		inFile >> sym;
		s[i].setSym(sym);

		getline(inFile, name, '#');
		s[i].setName(name);
		
		inFile >> sec;
		s[i].setSec(static_cast<Sector>(sec));
		
		inFile >> num;
		s[i].setNum(num);

		inFile >> pur;
		s[i].setPur(pur);

		inFile >> cur;
		s[i].setCur(cur);
		i++;
	}
	inFile.close();
	return i;
}

//basic sort function. 

void SortStk(Stock s[], int size)
{
	Stock temp;
	bool swap;
	do
	{
		swap = false;
		for (int i = 0; i < (size - 1); i++)
		{
			if (s[i].sec < s[i + 1].sec)
			{
				temp = s[i];
				s[i] = s[i + 1];
				s[i + 1] = temp;
				swap = true;
			}
		}
	} while (swap);
}

//This Function writes to a user selected file

void CalculatePortfolio(Stock s[], int size)
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
	//outter loop steps through sectors
	for (Sector k = TECHNOLOGY; k <= UTILITIES; k = static_cast<Sector>(k + 10)) {
		float ttlGain = 0;
		float ttlTax = 0;
		outFile << "Symbol" << setw(13) << "Company" << setw(43) << "Status" << endl;
		outFile << "======" << setw(13) << "=======" << setw(43) << "======" << endl;
		for (int i = 0; i < size; i++) {
			if (s[i].sec == k) {
				int stat = s[i].curStat();
				stat = static_cast<Status>(stat);
				ttlGain += s[i].gainAmt();
				ttlTax += s[i].taxGain();
				outFile << left << setw(13) << s[i].sym << setw(43) << s[i].name << right << statName(stat) << endl;
				
			}
		}

		outFile << right << fixed << setprecision(2);
		outFile << setw(40) << "Summary for Sector:\t" << displaySector(k) << endl;
		outFile << setw(40) << "Gain amount:\t" << ttlGain << endl;
		outFile << setw(40) << "Tax on gain:\t" << ttlTax << endl;
	}
		


	outFile.close();
	cout << "Portfolio Analysis located in: " << endl << fname << endl;
}

string statName(int stat) {
	string name;
	switch (stat) {
	case GAIN:
		name = "GAIN";
		break;
	case LOSS:
		name = "LOSS";
		break;
	case EVEN:
		name = "EVEN";
		break;
	}
	return name;
}

string displaySector(Sector k) {
	string sctr;
	switch (k) {
	case TECHNOLOGY:
		sctr = "TECHNOLOGY";
		break;
	case HEALTH:
		sctr = "HEALTH";
		break;
	case FINANCE:
		sctr = "FINANCE";
		break;
	case GOODS:
		sctr = "GOODS";
		break;
	case UTILITIES:
		sctr = "UTILITIES";
		break;
	}
	return sctr;
}


/*if (stat == GAIN)
return "GAIN";
if (stat == LOSS)
return "LOSS";
if (stat == EVEN)
return "EVEN";
else
return "thanks 4 playing";*/
