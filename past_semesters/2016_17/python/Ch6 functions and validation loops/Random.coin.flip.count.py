##Author: William Pulkownik
##Date: 30 Sep 2015
##File: Random num  count.py
##Description: text implementation of 6-5. Random # generator and counter

# to use the random number generator, we import it from the library, else "random" is undefined.
import random

def main() :
    #local counter variable and simulated named constant for count. count must be N+
    counter = int(0)
    NUM_FLIPS = int(10)
    #this flips the coin a set number of times THIRD ARGUMENT OPTIONAL IN PYTHON
    for counter in range(1, NUM_FLIPS + 1, 1) :
        if random.randint(1, 2) == 1 :
            print('HEADS')
        else :
            print('TAILS')

#CALL IT CALL IT CALL IT
main()
