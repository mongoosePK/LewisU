##Author: William Pulkownik
##Date 26 OCT 2015
##Program: reading text from file 10_2.py

def main() :
    #variables to hold data read from file
    name1 = '' ; name2 = '' ; mname3 = '' ; count = int(1)
    #open file philosophers.dat for reading
    infile = open('philosophers.dat', 'r')
    #read names from file .rstrip(***) is a python function which removes
    #the end of string
    #loop to read all lines from file
    for name1 in infile :
        print('Name ', str(count), ' read = ', name1)
        count += 1
    #close file
    infile.close()
    
main()
