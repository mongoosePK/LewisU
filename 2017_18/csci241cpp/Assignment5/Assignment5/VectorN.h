/***********************************************************************
PROGRAM:    CSCI 241 Assignment 5
PROGRAMMER: William Pulkownik
LOGON ID:   z-1805341
DUE DATE:   25

FUNCTION:   This program defines the VectorN
class.
***********************************************************************/

#ifndef VECTORN_H
#define VECTORN_H

#include <iostream>
#include <stdexcept>

class VectorN {
private:
	double* varray;
	size_t vcap;

public:
	VectorN();
	VectorN(const double*, size_t);
	VectorN(const VectorN& other);
	~VectorN()
	{
		delete[] varray;
	}
	void clear();
	size_t size() const;
};



#endif VECTORN_H
