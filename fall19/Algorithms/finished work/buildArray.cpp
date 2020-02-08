// William Pulkownik
// BuildArray.cpp
//

#include <iostream>
#include <stdlib.h>
#include <array>
#include <string>

using namespace std;

int main()
{
    //instantiate an array
    array<string,15> a;
    
    for (int i=0; i < a.size(); i++)
    {
        cout << "enter an integer array element: ";
        cin >> a[i];
    }

    for(const auto& elem: a)
        cout << elem << ' ';
        cout << '\n';
}
