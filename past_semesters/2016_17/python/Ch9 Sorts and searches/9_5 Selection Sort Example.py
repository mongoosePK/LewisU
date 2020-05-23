##File: Selection Sort Example

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

def main() :
    numArray = [40, 30, 20]
    print('before sort ', numArray)
    selectionSort(numArray, len(numArray))
    print('After sort', numArray)

main()
