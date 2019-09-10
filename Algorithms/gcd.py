# gcd.py
# by: william pulkownik
# 5SEP19

#here we will loop until we get good data
print ('this is the GreatestCommonDivisor calculator')
while True:
    try:
        m = int(input ('enter your first positive integer:'))
        n = int(input ('enter another positive integer:'))
    except ValueError:
        print('Sorry, at least one of your entries is not an integer')
        continue
    # if not isinstance(m, int) or not isinstance(n, int):
    #     print('Sorry, at least one of your entries is not an integer')
    #     continue
    if (m < 0) or (n < 0):
        print('Sorry, at least one of your entries was negative.')
        continue
    else:
        #good input data
        break



def gcdTool(m,n):
    if (n==0):
        return m
    else:
        return (gcdTool(n, m%n))

print ('the GCD of your integers is: ', gcdTool(m,n))