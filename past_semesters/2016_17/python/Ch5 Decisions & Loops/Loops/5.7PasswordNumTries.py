##Author: William Pulkownik
##23 SEP 2015
##File: textBookProgram5_7.PY
##description: Python implementation of book exercis 5.7
## NOTE python does not support posttest DO-UNTIL loop.
##      create pretest WHILE loop with break statement.

def main() :
    password = '' ; numTries = int(0)

    #loop until password correct
    while True:
        #get the password
        password = input('Enter the password: ')
        #set numtries increment -- check password and limit counts 
        numTries = numTries + 1
        if password == 'prospero' and numTries <= 4:
            break
        elif numTries > 4 :
            break
##The print stat
    if numTries <= 4 :
        print('Password confirmed')
    else :
        print('Please wait for your special prize!') 

main()
