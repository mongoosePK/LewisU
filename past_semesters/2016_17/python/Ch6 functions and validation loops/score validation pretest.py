def main() :
    #get test score
    score = int(input('Enter a test score: ' ))
    #validate
    while isInvalid(score) :
        print('Error! the score cannot be less than 0 or gresater than 100.')
        score = int(input('Enter the correct score: '))
    print('The score is', score)

def isInvalid(score) :
    status = True
    #see if passed score is invalid
    if score < 0 or score > 100 :
        status = True
    else :
        status = False
    return status

main()
