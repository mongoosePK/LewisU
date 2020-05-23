/* 
a4.cpp
William Pulkownik
5 OCT 2019
This program demonstrates C++ arrays. It builds and array with 
random numbers. It uses a min function to find the smallest element. 
It then implements a bubble sort and prints the results before 
and after so you will believe it worked.
*/

#include <iostream>
#include <stdlib.h>
#include <array>
#include <string>
#include <random>
//#include <algorithm>
#include <iomanip>

using namespace std;
  /*
   This function finds the min value in the array passed to it
   and returns the value as an integer
  */
int MinArray (array arr)
{	
	int minval = arr[0];
	for (int k = 1; k < arr.size(); k++)
		if (arr[k] < minval)
		   minval = arr[k];
	return minval; 
}

void sort (array x)
{
    // bool switch_on = true; // a[] is not sorted 
	bool flag = true;
    // outter loop through the array n times and test for flag condition
    for (int i=0; i<x.size() && flag; i++)
    {
        flag = false;
        // loop through array n-1 times. If x[j] < the next element, swap.
        for (int j=0; j< x.size()-1 ; j++)
            if (x[j]> x[j+1])
            {
                swap(x[j],x[j+1]);
                flag = true; //work is truth
            }
            
    }
}

int main()
{
    std::random_device ran;
    std::minstd_rand gen(ran());
    std::uniform_int_distribution<> nums(-50,100);
    //instantiate a 25 element array called foo
    //then fill it up
    std::array<int,25> arr;
    for(auto& elem : arr)
        elem = nums(gen);
    //print 5 per row
    int i=0;
    for(const auto& elem: arr) {
        std::cout << std::setw(3) << elem << ' ';
        ++i;
        if (i % 5 == 0)
            std::cout << '\n';
    }
    
    


    std::cout << "the sorted array is ";
    sort(arr);
    for(const auto& elem: arr) {
        std::cout << std::setw(3) << elem << ' ';
        ++i;
        if (i % 5 == 0)
            std::cout << '\n';
    }
    int min = MinArray(arr);
    std::cout << "the minimum value is " <<  std::endl;
}