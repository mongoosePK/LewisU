## William P.
## 16 SEP 15
## CIS 1400
## File: Grade.py
## Using python and if statements to calculate grade

def main():
    score = 0.0
    #in python declaring a variable ahead of its use is superfluous
    #without declaring score a float var the cpu automatically considers it a
    #string, and can't compare string and var
    score = float(input('Enter test score: '))
    if score < 60:
        print('Your grade is F')
# "elif" is python's elseif ...  colon at the end of statement is good syntax
    elif score < 70:
        print('your grade is D')
    elif score < 80:
        print('your grade is C')
    elif score < 90:
        print('your grade is B')
    else:
        print('your grade is A')

#call the module
main()
