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

/*
OUTPUT FROM PROGRAM

mongoose@goosebox:~/LewisU/Algorithms$ ./a.out 
enter an integer array element: 1
enter an integer array element: 2
enter an integer array element: 3
enter an integer array element: 4
enter an integer array element: 5
enter an integer array element: 6
enter an integer array element: 7
enter an integer array element: 8
enter an integer array element: 
9
enter an integer array element: 10
enter an integer array element: 11
enter an integer array element: 12
enter an integer array element: 13
enter an integer array element: 14
enter an integer array element: 15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
mongoose@goosebox:~/LewisU/Algorithms$ ./a.out 
enter an integer array element: 1
enter an integer array element: 2
enter an integer array element: 3
enter an integer array element: 4
enter an integer array element: five
enter an integer array element: 6
enter an integer array element: 7
enter an integer array element: 8
enter an integer array element: 9
enter an integer array element: ten
enter an integer array element: 11
enter an integer array element: 12
enter an integer array element: 13
enter an integer array element: 14
enter an integer array element: 15
1 2 3 4 five 6 7 8 9 ten 11 12 13 14 15 
mongoose@goosebox:~/LewisU/Algorithms$ 
/*