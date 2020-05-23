""" Author: William Pulkownik
    Date: 2Sep15
    Program: PayCalc.py
    Descr:
    In class exercise of python pay calculator
"""
# Python does not have data type keywords; use numbers to represent data 
payRate = 0.0; grossPay = 0.0; numHours = 0; taxes = 0.0; netPay = 0.0
# python does not support named constants; use a non-changing variable
TAX_RATE = 0.25
# Get the input data
numHours = int(input('Enter the number of hours (as a whole number) :'))
payRate = float(input('Enter the hourly pay rate:'))
#calculate and display gross pay
grossPay = numHours * payRate
print('The gross pay is $', grossPay)
# calculate and display taxes
taxes = grossPay * TAX_RATE
print ('The taxes are $', taxes)
# calc and display netPay
netPay = grossPay - taxes
print ('The net pay is $', netPay)
    
