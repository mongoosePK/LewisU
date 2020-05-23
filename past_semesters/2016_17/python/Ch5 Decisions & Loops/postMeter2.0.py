##Author: William Pulkownik
##CIS 1400
##Date: 18 Sep 2015
##File: postMeter.py
##Description: Program designed to determine
##shipping rates based on package weight.

def main():
    weight = 0.0
    #I will get the weight
    weight = float(input('Enter your package\'s weight:'))
    rateCalc(weight)
    #Now for the calculation module
def rateCalc(weight):
#define variables and set decision structure. then display
    mini = float(1.1); reg = float(2.2); large = float(3.7) ;
    jumbo = float(3.8)
    if weight <= 2.0 :
        rate = weight * mini
    elif 2.0 < weight <= 6.0 :
        rate = weight * reg
    elif 6.0 < weight <= 10.0 :
        rate = weight * large
    else :
        rate = weight * jumbo
    print('The shipping cost is $', rate)


#Call it.
main()

##=============== RESTART: C:\Users\William\Desktop\postMeter.py ===============
##Enter your package's weight:4.5
##The shipping cost is $ 9.9
##>>> main()
##Enter your package's weight:10
##The shipping cost is $ 37.0
##>>> main()
##Enter your package's weight:11
##The shipping cost is $ 41.8
