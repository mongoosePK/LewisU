/*
William Pulkownik
4 May 2016
Stock.cpp

*/

#include "Stock.h"

float Stock::tax = 0.15; // definition of static member

						 // constructors
Stock::Stock() {  // default constructor
	name = "";
	sym = "";
	sec = TECHNOLOGY;
	num = 0;
	pur = 0;
	cur = 0;
	
}

Stock::Stock(string n, string sy, Sector sc, int nbr, float p, float c) {  // parameter constructor
	name = n;
	sym = sy;
	sec = sc;
	num = nbr;
	pur = p;
	cur = c;
	
}

// destructor
Stock::~Stock() {}

// mutators
void Stock::setName(string n) {
	name = n;
}
void Stock::setSym(string sy) {
	sym = sy;
}
void Stock::setSec(Sector sc) {
	sec = sc;
}
void Stock::setNum(int nbr) {
	num = nbr;
}
void Stock::setPur(float p) {
	pur = p;
}
void Stock::setCur(float c) {
	cur = c;
}

// functions to calculate and return values
float Stock::curVal() {
	return num * cur;
}

Status Stock::curStat() {
	if (cur > (pur + .05))
		return GAIN;
	else if (cur < (pur - .05))
		return LOSS;
	else
		return EVEN;
}

float Stock::gainAmt() {
	if (curStat() == GAIN)
		return (curVal() - pur*num);
	else
		return 0.0;
}
float Stock::taxGain() {
	if (gainAmt() >= 0.0)
		return (gainAmt() * tax);
	else
		return 0.0;
}



