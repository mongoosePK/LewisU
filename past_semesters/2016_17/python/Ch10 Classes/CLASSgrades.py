##William Pulkownik
##18 NOV 2015
##grade classes

## self. , here, refers to the object itself

class GradedActivity :
    def __init__(self) :
        self.__score = 0.0
    def setScore(self, s) :
        self.__score = s
    def getScore(self) :
        return self.__score
    def getGrade(self) :
        if self.__score >= 90 :
            grade = 'A'
        elif self.__score >= 80 :
            grade = 'B'
        elif self.__score >= 70 :
            grade = 'C'
        elif self.__score >= 60 :
            grade = 'D'
        else :
            grade = 'F'
        return grade
        
