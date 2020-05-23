#Pulkownik
#9_7insertionSort
#insertionSort

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

def main() :
    values = [30, 10, 20, 5]
    print(values)
    insertionSort(values, len(values))
    print(values)

main()
