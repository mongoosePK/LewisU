##Author: William Pulkownik
##28 Sep 2015
##File: prog_5_9.py
##Description: 

def main():
    #local variables
    counter = int() ; square = int()
    # Python does not support constants; use unchanging variable
    MAX_VALUE = 10
    #display table headings
    print('Number\tSquare')
    print('------\t------')
    #display numbers 1 through 10 and their squares
    # in python, the range doesn't include the last value, thus +1
    for counter in range(1, MAX_VALUE + 1 ) :
        #calculate square then display
        square = counter**2
        print(counter, '\t', square)

main()
