##Author: William Pulkownik
##19 OCT 2015
##Array Assign.py
##Descr: in class exercise to create a list of numbers

def main():
    #named constant represents size
    SIZE = 5
    #Array/List of five integer numbers
    numbers = [0, 0, 0, 0, 0]
    #declare loop variables
    index = int() ; value = int(20)
    #set all array value in loop
    for index in range(0, SIZE) :
        numbers[index] = value
        value = value + 10
    #display values
    for index in range(0, SIZE) :
        print('value at index ', index, ' is ', numbers[index])

### PYTHON ONLY
    print('PYTHON SPECIFIC')
    print(numbers)
    for i in numbers :
        print('Numbers list element = ', i)
        
main()
    
