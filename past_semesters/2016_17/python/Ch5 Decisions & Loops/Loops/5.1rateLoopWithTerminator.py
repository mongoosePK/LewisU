##Author: William Pulkownik
##23 SEP 2015
##File: textBookProgram5_1.py
##Description: Python implementation of textbook exercise 5.1

def main():
    #make variables
    sales = float(); commision = float()
    keepGoing = 'y'
    COMMISSION_RATE = 0.1
    #set loop while calculating commissions //the while loop has an OR condition for both cases of 'y' (ASCII values different)
    while keepGoing == 'y' or keepGoing == 'Y' :
        sales = float(input('Enter the amount of sales: '))
        commission = sales * COMMISSION_RATE
        print('The commission is $', commission)
        #since program will run indefinitely, we must end the loop.
        keepGoing = input('Do you wish to calculate another commission? (enter \'y\' for yes)')
        
main()
