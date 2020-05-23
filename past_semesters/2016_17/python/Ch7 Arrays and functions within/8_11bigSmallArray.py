##William Pulkownik
##19 OCT 2015
##8_11.py
##takes a list and finds highest value

def main() :
    #named constant for array size
    SIZE = 5
    #INITIALIZED ARRAY/LIST
    numbers = [8, 1, 12, 6, 2]
    # initialize highest to first array value
    highest = numbers[0]
    #local variable to hold the index
    index = int() ; highestIndex = int()
#determinte the highest value in the array
    for index in range(1, SIZE) :
        if numbers[index] > highest :
            highest = numbers[index]
            highestIndex = index

    print('The highest value in the array is ', highest)

    print('The index value of the highest value ', highestIndex)

main()
