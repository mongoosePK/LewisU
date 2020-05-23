##William Pulkownik
##05 OCT 2015
##SalesCommission.py
##exercise 6-8 uses a function to modularize a sales commission program

def getSalesWithValidation() :
    #define a local variable to store monthlysales - get input - return it.
    monthlySales = float()
    monthlySales = input('Enter the salesperson\'s monthly sales: ')
    #validate input
    while invalidSales(monthlySales) :
        print('error must be greater than 0 and less than 2000')
        monthlySales = input('enter the salesperson\'s monthly sales: ')
    return float(monthlySales)

def invalidSales(sales) :
    status = True
    if not sales.replace('.', '', 1).isdigit() or float(sales) < 0 :
        status = True
    else :
        status = False
    return status

def getAdvancedPay() :
    advanced = float()
    advanced = float(input('Enter the amount of advanced pay, or 0 if no advanced pay was given: '))
    return advanced

# returns pay as float. READ, VALIDATE, AND RETURN VALUE
def getAdvancedPayWithValidation() :
    advanced = float()
    advanced = input('Enter the amount of advanced pay, or 0 if no advanced pay was given: ')
    while invalidAdvanced(advanced) :
        print('error mot be greater than 0 and less than 2000')
        advanced = input('Enter the amt of advanced pay, or 0 if none given')
    #return value of advanced pay as a real number
    return float(advanced)

def invalidAdvanced(advanced) :
    status = True
    #python EXCEPTION HANDLING -- here, a try/except block this is an advanced alternative
    #to our other validation method. it allows us to display customized error messages to user.
    try :
        value = float(advanced) #will raise valueError exception
        if value < 0 or value > 2000 :
            #manually raise an exception
            raise ValueError('value ' + str(value) + ' out of range.')
        status = False
    except ValueError as veErr :
        print('error.', veErr)
        status = True
    return status

def determineCommissionRate(sales) :
    rate = float()
    #you can chain comparisons OR set as an AND/OR/NOT operation
    if sales < 10000 :
        rate = .1
    elif 10000 <= sales <= 14999.99 :
        rate = .12
    elif sales >= 15000 and sales <= 17999.99 :
        rate = .14
    elif sales >= 18000 and sales <= 21999.99 :
        rate = .18
    else :
        rate = .18
    return rate

def main() :
    #the first declaration line of variables is unnecessary
    sales = float() ; commissionRate = float() ; advancedPay = float() ; pay = float() ; 
    sales = getSalesWithValidation()
    advancedPay = getAdvancedPayWithValidation()
    commissionRate = determineCommissionRate(sales)
    pay = sales * commissionRate - advancedPay
    #notice the format of pay, 2 decimal point float
    print('The pay is $', format(pay, '.2f'))
    if pay < 0 :
        print('The salesperson must reimburse the company.')

main()
