##Author: William Pulkownik
##Lab 10 .dat output
##CIS 1400  30NOV2015
def main() :
 
    data = [] ; count = int(0)
    
    infile = open('song_inventory.dat', 'r')
    #read names from file .rstrip(***) is a python function which removes
    #the end of string
    #loop to read all lines from file
    for aline in infile :
        data.append(aline.rstrip('\n'))
        count += 1

    infile.close()

    print(data)
main()

##>>> 
##['Led Zepplin Stairway to Heaven 7.5 1979', 'Lynard Skynard Free Bird 10.0 1977']
##>>> 
