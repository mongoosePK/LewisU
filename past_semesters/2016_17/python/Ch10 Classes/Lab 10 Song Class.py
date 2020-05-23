##William Pulkownik
##CIS 1400 LAB 10
##24 NOV 2015
##Lab10.py

class Song :
    def __init__(inst, art, name, run, release) :
        inst.__artist = art
        inst.__title = name
        inst.__time = run
        inst.__year = release

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
    song2 = Song(artist2, title2, time2, year2)
    songFile = open('song_inventory.dat', 'w')
    songFile.write(artist1 + ' ' + title1 + ' ' + str(time1) +
                   ' ' + str(year1) + '\n')
    songFile.write(artist2 + ' ' + title2 + ' ' + str(time2) +
                   ' ' + str(year2) + '\n')
    songFile.close()
    print('The first song is ', song1.getTime(), ' minutes long.')
    print('The second song is ', song2.getTime(), ' minutes long.')
    print('Together, the songs run for ', song1.getTime() + song2.getTime(),
          ' minutes.')
    
    
main()

##>>> 
##Enter the name of a song: Stairway to Heaven
##Please enter that song's artist: Led Zepplin
##In minutes, how long is the song? 7.5
##What year was the song released? 1979
##Enter the name of another song: Free Bird
##Please enter that song's artist: Lynard Skynard
##In minutes, how long is the song? 10
##What year was the song released? 1977
##The first song is  7.5  minutes long.
##The second song is  10.0  minutes long.
##Together, the songs run for  17.5  minutes.
##>>> 
