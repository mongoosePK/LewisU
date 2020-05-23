def main() :
    #get test score
    score = input('Enter a test score: ' )
    #validate
    while isInvalidNumCheck(score) :
        print('Error! The score cannot be less than 0 or gresater than 100 and must be a number.')
        score = input('Enter the correct score: ')
    print('The score is', score)




##Function: isInvalidNumCheck
##return true if score is not a number or not in valid range

def isInvalidNumCheck(score) :
    status = True
    #check if score is invalid with replace AND isdigit functions on the string 'score'
    if not score.replace('.', '', 1).isdigit() or float(score) < 0 or float(score) > 100 :
        status = True
    else :
        status = False
    return status


main()
