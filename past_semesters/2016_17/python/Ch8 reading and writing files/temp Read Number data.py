##William Pulkownik
##28 OCT 2015
##tempReadNumberdata

def main() :
    counter = int(0)
    temp = float(0)
    tempTotal = float(0)
    tempFile = open('temperature.dat', 'r')
    for oneLine in tempFile :
        temp = float(oneLine)
        counter += 1
        tempTotal = tempTotal + temp
    tempFile.close()
    print('number read = ', counter)
    print('total of temperatures is ', format(tempTotal, '.2f'))

main()
