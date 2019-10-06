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

//using namespace std;
//trying to break bad habits and be professional

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
    //and print
    for(auto& elem: arr)
        std::cout << elem << ' ';
        std::cout << '\n';
}