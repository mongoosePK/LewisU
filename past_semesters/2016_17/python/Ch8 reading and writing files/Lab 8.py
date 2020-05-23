##Author: William Pulkownik
##Date 26 OCT 2015
##Program: Lab_8.py

def main() :
    #declare integers
    number = int() ; counter = int(0) ; total = int(0)
    numFile = open('numbers.dat', 'r')
    #read file line by line, each time accumulating total and
    #incrementing count
    for each in numFile :
        number = int(each)
        total = total + number
        counter += 1
    #close file then print average     
    numFile.close()
    print('The average of the numbers in this file is',
          format(total / number, '.2f'))

#call it.
main()

##================= RESTART: F:\Fall 2015\Programming\Lab 8.py ===============
##The average of the numbers in this file is 59.29
##>>> 
