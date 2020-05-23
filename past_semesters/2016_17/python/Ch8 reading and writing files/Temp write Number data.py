##William Pulkownik
##28 OCT 2015
##tempWriteNumberdata

def main() :
    temp1 = 35.3; temp2 = 65.6 ; temp3 = 88.7
    tempFile = open('temperature.dat', 'w')
    ## temps are in () because we are converting to str, then adding EOF - '/n'
    tempFile.write(str(temp1) + '\n')
    tempFile.write(str(temp2) + '\n')
    tempFile.write(str(temp3) + '\n')
    tempFile.close()

main()
