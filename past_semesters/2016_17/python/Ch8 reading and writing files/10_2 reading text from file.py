##Author: William Pulkownik
##Date 26 OCT 2015
##Program: reading text from file 10_2.py

def main() :
    #variables to hold data read from file
    name1 = '' ; name2 = '' ; mname3 = ''
    #open file philosophers.dat for reading
    infile = open('philosophers.dat', 'r')
    #read names from file .rstrip(***) is a python function which removes
    #the end of string
    name1 = infile.readline().rstrip('\n')
    name2 = infile.readline().rstrip('\n') 
    name3 = infile.readline().rstrip('\n')
    #close file
    infile.close()
    #display names
    print('Here are the names read from file: ')
    print(name1)
    print(name2)
    print(name3)

main()
