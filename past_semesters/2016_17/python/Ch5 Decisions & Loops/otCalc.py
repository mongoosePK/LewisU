##Author: William Pulkownik
##21Sep2015
##CIS 1400
##File: otCalc.py
##Description: a boolean exercise used to simulate overtime pay calculation.

BASE_HOURS = 40

def main():
    #local var
    overTime = False; hoursWorked = float() ; payRate = float()
    #user input
    hoursWorked = float(input("Enter the number of hours worked: "))
    payRate = float(input("Enter the hourly pay rate: "))
    if hoursWorked > BASE_HOURS :
        overTime = True
    # call appropriate calculation and display module based on overtime
    if overTime:
        calcOTPay(hoursWorked, payRate)
    else:
        calcPay(hoursWorked, payRate)

def calcOTPay(hours, rate):
    #LOCAL CONSTANT
    OT_MULTIPLIER = 1.5
    otHours = float(); otPay = float(); grossPay = float();
    otHours = hours - BASE_HOURS
    otPay = otHours * rate * OT_MULTIPLIER
    grossPay = BASE_HOURS * rate + otPay
    print('The gross pay is $', grossPay)
    return

def calcPay(hours, rate):
    grossPay = float()
    grossPay = hours * rate
    print('The gross pay is $', grossPay)
    return

main()

##Enter the number of hours worked: 60
##Enter the hourly pay rate: 10
##The gross pay is $ 700.0
##>>> main()
##Enter the number of hours worked: 10
##Enter the hourly pay rate: 10
##The gross pay is $ 100.0
##>>> 
