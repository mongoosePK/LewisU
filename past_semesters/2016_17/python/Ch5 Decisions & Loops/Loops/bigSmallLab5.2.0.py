##Author: William Pulkownik
##25 Sep 2015
##File: bigSmall.py
##Description: Lab 5 assignment, tracking and categorizing user input based on value

def main():
    inputNum = float() ; smallest = inputNum ; largest = inputNum ;
    welcomeMod()
    inputMod()
    ##For Some reason I can't call dispMod() from the main function \
    ## without losing the input values for biggest and smallest. Why?

def welcomeMod():
    print("This program will allow you to enter multiple values, then display the high and low values")
    print("Please enter your values. After you are done, enter \"-99\"")

def inputMod() :
    inputNum = float() ;
    while inputNum != -99 :
        inputNum = float(input("Value:"))
        if inputNum != -99 :
            if inputNum < smallest :
                smallest = inputNum
            elif inputNum > largest :
                largest = inputNum
                    
    dispMod(smallest, largest) 


def dispMod(smallest, largest) :
    print("Your smallest and largest values are, respectively,", smallest, largest)

main()


##>>> 
##This program will allow you to enter multiple values, then display the high and low values
##Please enter your values. After you are done, enter "-99"
##Value:-25
##Value:0
##Value:25
##Value:50
##Value:-99
##Your smallest and largest values are, respectively, -25.0 50.0
##>>> 
