/*
William Pulkownik
4 May 2016
Stockclass.h

*/
#include <iostream>
#include <string>
#include <iomanip>
#include <fstream>
using namespace std;


#ifndef STOCK_H
#define STOCK_H
enum Status { GAIN = 1, LOSS, EVEN};
enum Sector { TECHNOLOGY = 10, HEALTH = 20 , FINANCE = 30, GOODS = 40, UTILITIES = 50};
class Stock {
private:
	string name;
	string sym;
	Sector sec;
	int num;
	float pur;
	float cur;
public:
	// constructors
	Stock();
	Stock(string, string, Sector, int, float, float);

	// destructor
	~Stock();
	// mutators (aka setters) for private data
	void setName(string);
	void setSym(string);
	void setSec(Sector);
	void setNum(int);
	void setCur(float);
	void setPur(float);
	// accessors (aka getters) for private data
	// declared inline
	string getName() const { return name; }
	string getSym() const { return sym; }
	Sector getSec() const { return sec; }
	int getNum() const { return num; }
	float getpur() const { return pur; }
	float getcur() const { return cur; }
	//Tax
	static float tax;
	// functions to calculate values
	Status curStat();
	float curVal();
	float gainAmt();
	float taxGain();
	
	// grant friendship to function
	friend void SortStk(Stock s[], int size);
	friend void CalculatePortfolio(Stock s[], int size);
};

#endif
