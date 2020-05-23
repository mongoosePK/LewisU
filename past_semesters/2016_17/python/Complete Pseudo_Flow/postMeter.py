##Author: William Pulkownik
##CIS 1400
##Date: 18 Sep 2015
##File: postMeter.py
##Description: Program designed to determine
##shipping rates based on package weight.

def main():
    weight = 0.0; rate = 0.0
    #I will get the weight
    weight = float(input('Enter your package\'s weight:'))

    #Now for the calculation module
    def rateCalc(weight):
        if weight <= 2.0 :
            rate = weight * 1.1
        elif 2.0 < weight <= 6.0 :
            rate = weight * 2.2
        elif 6.0 < weight <= 10.0 :
            rate = weight * 3.7
        else :
            rate = weight * 3.8
        print('The shipping cost is $', rate)
    rateCalc(weight)
#calling the rateCalc module must be done indented in main() def
#Call it.
main()

##=============== RESTART: C:\Users\William\Desktop\postMeter.py ===============
##Enter your package's weight:4.5
##The shipping cost is $ 9.9
##>>> 
