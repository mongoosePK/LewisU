##Author: William Pulkownik
##6 OCT 2015
## CIS 1400
##File: Lab6.py

def getValidScore() :
    ## A FOR LOOP WILL WORK IF YOU CALL THE DETERMINE  GRADE FUNCTION WITHIN
    ##GETVALIDSCORE -------TRY IT. THIS WILL MAKE HARDCALLING THE LOOP IN MAIN()
    ## UNNECESSARY
    #get test score as a string and return it as a real number
    score = input('Enter a test score: ' )
    #validate
    while isInvalidScore(score) :
        print('Error! the score cannot be less than 0 or greater than 100.')
        score = input('Enter the correct score: ')
    return float(score)

def isInvalidScore(score) :
    status = True
    #check if score is invalid with replace AND isdigit functions on the string 'score'
    #this ensures float validity
    if not score.replace('.', '', 1).isdigit() or float(score) < 0 or float(score) > 100 :
        status = True
    else :
        status = False
    return status

def determineGrade(score) :
    #This function accepts the grade as a real number then returns a string output to the 'gradeX' variable
    if float(score) < 60 :
        return str('grade is an F')
    elif float(score) < 70 :
        return str('grade is a D')
    elif float(score) < 80 :
        return str('grade is a C')
    elif float(score) < 90 :
        return str('grade is a B')
    else :
        return str('grade is an A')

def calcAverage(score1, score2, score3, score4, score5) :
    #to make this work
    average = float(score1 + score2 + score3 + score4 + score5) / 5
    return float(average)

def main() :
    print('Please enter 5 test scores to receive letter grades and test average.')
    score1 = getValidScore()
    grade1 = determineGrade(score1)
    print('The test ', grade1)
    score2 = getValidScore()
    grade2 = determineGrade(score2)
    print('The test ', grade2)
    score3 = getValidScore()
    grade3 = determineGrade(score3)
    print('The test ', grade3)
    score4 = getValidScore()
    grade4 = determineGrade(score4)
    print('The test ', grade4)
    score5 = getValidScore()
    grade5 = determineGrade(score5)
    print('The test ', grade5)
    average = calcAverage(score1, score2, score3, score4, score5)
    averageGrade = determineGrade(average)
    print('The test average is: ', format(average, '.2f'))
    print('The test average letter ', averageGrade)

main()

##Please enter 5 test scores to receive letter grades and test average.
##Enter a test score: 105
##Error! the score cannot be less than 0 or greater than 100.
##Enter the correct score: Great Job!
##Error! the score cannot be less than 0 or greater than 100.
##Enter the correct score: 100
##The test  grade is an A
##Enter a test score: 89.9
##The test  grade is a B
##Enter a test score: 79
##The test  grade is a C
##Enter a test score: 69
##The test  grade is a D
##Enter a test score: 59.99
##The test  grade is an F
##The test average is:  79.58
##The test average letter  grade is a C
##>>> 


