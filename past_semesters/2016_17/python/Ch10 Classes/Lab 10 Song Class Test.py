##William Pulkownik
##CIS 1400 LAB 10
##24 NOV 2015
##Lab10.py

class Song :
    def __init__(inst, art, name, run, release, write) :
        inst.__artist = art
        inst.__title = name
        inst.__time = run
        inst.__year = release
        inst.__outFile = write

    ##mutators
    def setArtist(inst, art) :
        inst.__artist = art
    def setTitle(inst, name) :
        inst.__title = name
    def setTime(inst, run) :
        inst.__time = run
    def setYear(inst, release) :
        inst.__year = release


    ##accessors
    def getArtist(inst) :
        return inst.__artist
    def getTitle(inst) :
        return inst.__title
    def getTime(inst) :
        return inst.__time
    def getYear(inst) :
        return inst.__year

##method
    def writeFile(inst, art, name, run, release) :
        outFile = open('song_inventory.dat', 'a')
        inst.__outFile.write(art + ' ' + name + ' ' + str(run) + ' ' + str(release))
        putFile.close()
        
def main() :
    
    title1 = input('Enter the name of a song: ')
    artist1 = input('Please enter that song\'s artist: ')
    time1 = float(input('In minutes, how long is the song? '))
    year1 = int(input('What year was the song released? '))
    title2 = input('Enter the name of another song: ')
    artist2 = input('Please enter that song\'s artist: ')
    time2 = float(input('In minutes, how long is the song? '))
    year2 = int(input('What year was the song released? '))
    song1 = Song(artist1, title1, time1, year1)
    song1.writeFile(artist1, title1, time1, year1)
    song2 = Song(artist2, title2, time2, year2)
    song2.writeFile(artist2, title2, time2, year2)
    print('The first song is ', song1.getTime(), ' minutes long.')
    print('The second song is ', song2.getTime(), ' minutes long.')
    print('Together, the songs run for ', song1.getTime() + song2.getTime(),
          ' minutes.')
    
    
main()
