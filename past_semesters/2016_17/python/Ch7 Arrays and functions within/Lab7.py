##Author: William Pulkownik
##Date: 21 OCT 2015
##File: Lab_7.py


def main() :
    #constant for array size
    SIZE = 12
    
    monthRain = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    #the index attachment to monthRain creates a memory space for each input and
    #increments MonthName
    for index in range(SIZE) :
        monthRain[index] = float(input('Enter rainfall for month ' +
                                       str(monthName[index]) +' in inches:' ))

    
    largeRain = getLargestRainfall(monthRain, SIZE)
    smallRain = getSmallestRainfall(monthRain, SIZE)
    total = totalRain(monthRain, SIZE)
    print('The total rainfall for the year was ', format(total, '.2f'),
          ' inches.')
    print('The greatest rainfall was ', monthRain[largeRain], ' inches, in ',
          monthName[largeRain])
    print('The least rainfall was ', monthRain[smallRain], 'inches, in ',
          monthName[smallRain])
    print('The monthly average rainfall for the year was ',
          format(total / 12, '.2f'), ' inches.')
def getLargestRainfall(rain, SIZE) :
    #set large rain to a list value to ensure valid output (same for small)
    largeRain = rain[0]
    monthIndexL = int(0)
    for index in range(SIZE) :
        if rain[index] > largeRain :
            largeRain = rain[index]
            monthIndexL = index     
    return monthIndexL

def getSmallestRainfall(rain, SIZE) :
    smallRain = rain[0]
    monthIndexS = int(0)
    for index in range(SIZE) :
        if rain[index] < smallRain :
            smallRain = rain[index]
            monthIndexS = index
    return monthIndexS

def totalRain(rain, SIZE) :
    total = float(0)
    index = int(0)
    for index in range(SIZE) :
          total = total + rain[index]
    return total


main()

##Enter rainfall for month Jan in inches:1.1
##Enter rainfall for month Feb in inches:2.2
##Enter rainfall for month Mar in inches:3.3
##Enter rainfall for month Apr in inches:4.4
##Enter rainfall for month May in inches:5.5
##Enter rainfall for month Jun in inches:6
##Enter rainfall for month Jul in inches:5
##Enter rainfall for month Aug in inches:4
##Enter rainfall for month Sep in inches:3
##Enter rainfall for month Oct in inches:2
##Enter rainfall for month Nov in inches:3.68
##Enter rainfall for month Dec in inches:1
##The total rainfall for the year was  41.18  inches.
##The greatest rainfall was  6.0  inches, in  Jun
##The least rainfall was  1.0 inches, in  Dec
##The monthly average rainfall for the year was  3.43  inches.
