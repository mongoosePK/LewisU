##Author: William Pulkownik
##Date 26 OCT 2015
##Program: reading text from file 10_2.py

def main() :
    #variables to hold data read from file
    names = [] ; count = int(0)
    #open file philosophers.dat for reading
    infile = open('philosophers2.dat', 'r')
    #read names from file .rstrip(***) is a python function which removes
    #the end of string
    #loop to read all lines from file
    for aline in infile :
        names.append(aline.rstrip('\n'))
        count += 1
    #close file
    infile.close()

    print('number read = ', count)
    print('Names: ', names)
    for index in range(0, len(names)) :
        print(names[index])
main()
