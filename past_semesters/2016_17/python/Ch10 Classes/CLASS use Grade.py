##William Pulkownik
##18 NOV 2015
##use grade classes

import CLASSgrades

def main() :
    testScore = float(0)
    test = CLASSgrades.GradedActivity()
    testScore = float(input('Enter a numeric test score: '))
    test.setScore(testScore)
    print('The grade for that test is ', test.getGrade())

main()
