##Author: William Pulkownik
##10 Nov 2015
##CIS 1400 Lab_9.py
##Description: Sort and search names


def main() :
    names = ['Ross Harrison', 'Hannah Beauregard', 'Bob White', 'Ava Fischer',
             'Chris Rich', 'Xavier Adams', 'Sasha Ricci', 'Danielle Porter',
             'Gordon Pike', 'Matt Hoyle']

    insertionSort(names, len(names))
    displayMod(names)
    
    search = input('Please enter the name for which you wish to search: ') 

    index = binarySearch(names, search, len(names))
    if index > -1 :
        print('This person is number ', index + 1, ' on the list.')
    else :
        print('Error. The name you are searching for is not on the list.')


def insertionSort(array, arraySize) :
    #loop counter
    index = int(0)
    #variable to scan through array
    scan = int(0)
    #value to locate position
    unsortedValue = int(0)
    #outer loop to take unsorted value
    for index in range(1, arraySize) :
        unsortedValue = array[index]
        scan = index
        #inner loop to locate position and shift elements
        while scan > 0 and array[scan - 1] > unsortedValue :
            array[scan] = array[scan - 1]
            scan = scan - 1
        #place unsorted element in to final sorted subarray
        array[scan] = unsortedValue

def binarySearch(array, value, arraySize) :
    first = int(0)
    last = arraySize - 1
    position = -1
    found = False
    middle = int(0)
    while not found and first <= last :
        middle = int((first + last) / 2)
        if array[middle] == value :
            found = True
            position = middle
        elif array[middle] > value :
            last = middle - 1
        else :
            first = middle + 1

    return position

def displayMod(names) :
    print('Here is a list of the names in the group, in alphabetical order:')
    print(names)

main()

##>>> 
##Here is a list of the names in the group, in alphabetical order:
##['Ava Fischer', 'Bob White', 'Chris Rich', 'Danielle Porter', 'Gordon Pike',
## 'Hannah Beauregard', 'Matt Hoyle', 'Ross Harrison', 'Sasha Ricci', 'Xavier
## Adams']
##Please enter the name for which you wish to search: Gordon Pike
##This person is number  5  on the list.
##>>> 
