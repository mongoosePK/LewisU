## Author: William Pulkownik
## CIS 1400 16SEP2015
## Password Program
def main():
    ## python doesn't need you to declare variable types as strings, so
    ## --- password = input('enter the password') --- is valid
    password = str(input('Please enter your password: '))
    ## 
    if password == 'prospero':
        print('Password accepted.')
    else:
        print('Sorry, that\'s the wrong password.')

##this is how you call the module
main()
