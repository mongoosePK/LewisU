##William Pulkownik
##21 OCT 2015
##8_13 Function with array parameter.

def main() :
    SIZE = 5
    numbers = [2, 4, 6, 8, 10]
    total = int(0)
    #call function to totoal all array values
    total = getTotal(numbers, SIZE)
    print('The sum of the array elements is ', total)

def getTotal(array, arraySize) :
    index = int(0)
    total = int(0)
    for index in range(0, arraySize) :
        total = total + array[index]
    return total

main()
