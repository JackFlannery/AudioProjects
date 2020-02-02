
# This is an audio Python program written by Jack Flannery.

# The purpose of this program as part of a series of programs is to experiment with Python's audio capabilities.
# This specific program, the 8-bit Jukebox, allows the user to choose from a list of songs (like a real jukebox) or
# have the machine choose a song for them out of the four possible options.

# Run the program to try it for yourself! The audio files associated with this simple program are located in the
# same github repository as this file.

# Enjoy!

# import the playsound module, as to allow audio files to be played through Python

from playsound import playsound

# import sleep from time as to allow pauses before songs
from time import sleep

# import randint from random to help with automated song selection
from random import randint

# names of the tracks stored in the digital jukebox
tracks = ['Billie Jean.mp3', 'Wake Me Up Before You Go Go.mp3', 'Take On Me.mp3', 'Reaching.mp3']

# the first method in this program, countDown, is used to play a small audible and printable countdown to come before
# the song that was chosen is played.

def countDown():

    # the calls to sleep are used to make the countdown sound more natural

    sleep(1)

    # the numbers of the countdown, leading up to the playing of the song, are printed out as the noise is heard

    print(3)

    # the countdown sound from Halo Reach was used in this program

    playsound('Count.wav')

    # a small amount of time separates each countdown sound a number print

    sleep(0.75)

    print(2)

    playsound('Count.wav')

    sleep(0.75)

    print(1)

    playsound('Count.wav')

    sleep(0.75)

    print("Play!")

    # a different sound is used to signal the end of the countdown

    playsound('Final.wav')

# the trackSelect method welcomes the user, prints the list of songs to choose from, and asks the user to choose them
# by their track number.

def trackSelect():

    print("Welcome to the Python 8-bit JukeBox!\n")

    print("Song Selection:\n")

    print("1. Billie Jean by Michael Jackson\n")

    print("2. Wake Me Up Before You Go Go\n")

    print("3. Take On Me\n")

    print("4. Reaching by Elastic Blur\n")

    trackNum = int(input("Type in the track number you wish to listen to or type zero to have a track picked for you:"))

    # input control on trackNum

    if isinstance(trackNum, int) and trackNum in range(0, 5):
        return trackNum

    else:
        return "Please enter a valid track number."

# the loadTrack method will tell the user their selection is loading, initiate the countdown function, and play the
# appropriate song per the user's request.

def loadTrack(trackNum):

    print("Loading " + tracks[trackNum-1][:-4] + "...")

    countDown()

    playsound(tracks[trackNum-1])

    quit()

# begin function calls

# the variable jukebox corresponds to a call of the track select function.

jukeBox = trackSelect()

# if the user inputted 0, indicating a shuffle, then the random integer generator titled selector will decide which
# track shall be played out of the four options.

if jukeBox == 0:

    selector = randint(1, 100)

    if selector in range(1, 25):
        loadTrack(1)

    elif selector in range(25, 50):
        loadTrack(2)

    elif selector in range(50, 75):
        loadTrack(3)

    elif selector in range(75, 100):
        loadTrack(4)

# if any other number is chosen, then that number will be sent into the load track function accordingly.

else:

    loadTrack(jukeBox)


