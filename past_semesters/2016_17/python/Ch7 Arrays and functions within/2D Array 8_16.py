# Author:  Your Name Here
# Date:    MM/DD/YYYY
# Program: Prog8_16.py
# Descr:
# In-class exercise to create the Python implementation
# of Program 8-16 on page 322 and discussed on slides
# 25 and 26.  This program uses a two-dimensional array.

def main():
    # named constant to represent array size
    ROWS = 3
    COLS = 4
    # 2-D array/list initialized with numbers
    #    3 rows, 4 columns
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    # local variables
    row = 0
    col = 0
    # nested loops to prompt user for input
    for row in range(0, ROWS):
        for col in range(0, COLS):
            values[row][col] = int(input('Enter an integer number: '))

    # nested loop to display values
    print('Here are the values you entered.')
    for row in range(0, ROWS):
        for col in range(0, COLS):
            print('row = ' + str(row) + ' col = ' + str(col) + \
              ' value = ' + str(values[row][col]))


main()
