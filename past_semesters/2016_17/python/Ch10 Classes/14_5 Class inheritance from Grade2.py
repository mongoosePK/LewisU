##William Pulkownik
##23 NOV 2015
##14_5.py  exercise to use inherited classes for creating final exam problem

## import makes FinalExam and GradedActivity classes available
import Grade2

def main():
    #get number of questions and number missed on exam
    questions = int(input('Enter the number of questions on the exam: '))
    missed = int(input('How many questions were missed? '))
    #use these values to create final exam object
    exam = Grade2.FinalExam(questions, missed)
    #display the results
    print('Each question is worth: ', exam.getPointsEach())
    print('Exam score is: ', exam.getScore())
    print('The exam grade is: ', exam.getGrade())

main()
