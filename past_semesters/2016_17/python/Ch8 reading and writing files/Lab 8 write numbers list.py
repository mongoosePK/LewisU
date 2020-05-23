##Author: William Pulkownik
##Date 26 OCT 2015
##Program: Writing to file 10_1.py

def main() :
    numbers = [8, 5, 4, 1, 2, 3, 6, 7, 9]
    #open a file named philosophers.dat for writing 1&3 use file var outfile 2
    #'w' = write 'r' = read 'a' = append
    outfile = open('numbers.dat', 'w')
    #process file with writing statements **for spacing, use \n** (4)
    for n in numbers:
        outfile.write(n)
    #close file (step5)
    outfile.close()

main()
