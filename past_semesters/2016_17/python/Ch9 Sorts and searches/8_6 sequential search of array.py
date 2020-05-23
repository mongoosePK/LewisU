##Author: William Pulkownik
##2 Nov 2015
##Python linear or sequential search

def main():
    SIZE = 10
    scores = [87, 75, 98, 100, 82, 72, 88, 92, 60, 78]
    found = False
    index = int(0)
    # linear search algorithim
    while found == False and index <= SIZE - 1 :
        if score [index] == 100 :
            found = True
        else :
            index = index + 1
    #display search results
    if found :
        print('you earned 100 on test number ', index + 1)
    else :
        print('You did not earn 100 on any test.')

#call it to start the program
main()
