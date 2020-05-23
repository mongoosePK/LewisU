# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Prog9_2.py
# Descr:
# In-class exercise to create the Python implementation
# of Bubble Sort Program 9-2 in Gaddis.

def main():
    # Constant for the array size
    SIZE = 6
    # Array to hold test scores
    testScores = [0, 0, 0, 0, 0, 0]
    # Get the test scores
    getTestScores(testScores, SIZE)
    #sort score array
    bubbleSort(testScores, SIZE)
    # Display the test scores
    print('Here are the test scores sorted from lowest to highest.')
    showTestScores(testScores, SIZE)

# The getTestScores module prompts the user
# to enter test scores into the array that is
# passed as an argument.
def getTestScores(array, arraySize):
    # Counter variables
    index = 0
    # Get the test scores
    for index in range (0, arraySize):
        array[index] = int(input('Enter score number ' + str(index + 1) + ' '))

# The showTestScores module displays the contents
# of the array that is passed as an argument.
def showTestScores(array, arraySize):
    # Counter variables
    index = 0
    # Display the test scores
    for index in range (0, arraySize):
        print(array[index])

def bubbleSort(array, arraySize) :
    maxElement = int(0)
    index = int(0)
    #decrementing outer For Loop (goes from (size-1, -1) because range function
    #goes to the next greatest integer)
    for maxElement in range(arraySize - 1, -1, -1) :
        #incrementing inner for loop
        for index in range(0, maxElement) :
            #compare current with next and swap if necessary
            if array[index] < array[index + 1] :
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp

# start program
main()
