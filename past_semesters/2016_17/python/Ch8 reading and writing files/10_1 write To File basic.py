##Author: William Pulkownik
##Date 26 OCT 2015
##Program: Writing to file 10_1.py

def main() :
    #open a file named philosophers.dat for writing 1&3 use file var outfile 2
    #'w' = write 'r' = read 'a' = append
    outfile = open('philosophers.dat', 'a')
    #process file with writing statements **for spacing \n
    outfile.write('William Pulkownik\n')
    outfile.write('Matt Weiss\n')
    outfile.write('Vladimir Putin\n')
    #close file (step5)
    outfile.close()

main()
