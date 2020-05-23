# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Prog9_6.py
# Descr:
# In-class exercise to create the Python implementation
# of Insertion Sort Program 9-6 in Gaddis
def main():
    # Constant for the array size
    SIZE = 6
    # An array of Integer
    numbers = [4, 6, 1, 3, 5, 2]
    # Loop counter
    index = int()
    # Display the array in its original order
    print('Original order:')
    for index in range (0, SIZE):
        print(numbers[index])
    # Sort the numbers
    selectionSort(numbers, SIZE)
    # Display the sorted array
    print('Sorted order:')
    for index in range (0, SIZE):
        print(numbers[index])
    

def selectionSort(array, arraySize) :
    startScan = int(0) ; minIndex = int(0) ; minValue = int(0) ; index = int(0)
    #outer loop of scan
    for startScan in range(0, arraySize - 1) :
        #set minimums
        minIndex = startScan
        minValue = array[startScan]
        #inner loop to find smallest
        for index in range(startScan + 1, arraySize) :
            if array[index] < minValue :
                minValue = array[index]
                minIndex = index
            #swap values
            array[minIndex] = array[startScan]
            array[startScan] = minValue
# start program
main()
