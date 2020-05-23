##Author: William Pulkownik
##2 Nov 2015
##Python Bubble search of array

def bubbleSort(array, arraySize) :
    maxElement = int(0)
    index = int(0)
    #decrementing outer For Loop (goes from (size-1, -1) because range function
    #goes to the next greatest integer)
    for maxElement in range(arraySize - 1, -1, -1) :
        #incrementing inner for loop
        for index in range(0, maxElement) :
            #compare current with next and swap if necessary
            if array[index] > array[index + 1] :
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp

def main() :
    myArray = [30, 10, 20, 40, 50]
    print('Before sorting...', myArray)
    bubbleSort(myArray, len(myArray))
    print('After sorting...', myArray)
