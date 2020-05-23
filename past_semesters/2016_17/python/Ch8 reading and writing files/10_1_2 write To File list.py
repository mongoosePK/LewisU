##Author: William Pulkownik
##Date 26 OCT 2015
##Program: Writing to file 10_1.py

def main() :
    names = ['Jann Ibay', 'Brendan La', 'Cesar Lazcano']
    #open a file named philosophers.dat for writing 1&3 use file var outfile 2
    #'w' = write 'r' = read 'a' = append
    outfile = open('philosophers2.dat', 'a')
    #process file with writing statements **for spacing \n (4)
    for n in names:
        outfile.write(n + '\n')
    #close file (step5)
    outfile.close()

main()
