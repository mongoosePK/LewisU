#pulkownik
#Binary search function
#9_8
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

def main() :
    values = [10, 20, 30, 40, 50, 60, 70, 80]
    index = binarySearch(values, 40, len(values))
    if index > -1 :
        print('Value in array!')

main()
