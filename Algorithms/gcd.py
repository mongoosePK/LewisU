# gcd.py
# by: william pulkownik
# 5SEP19

print ('this is the GreatestCommonDivisor calculator')
m = input ('enter an integer:')
n = input ('enter another integer:')

def gcdTool(m,n):
    if (n==0):
        return m
    else:
        return (gcdTool(n, m%n))

print ('the GCD of your integers is: '), gcdTool(m,n)