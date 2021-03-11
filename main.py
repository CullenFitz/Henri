from speak import speak
from listen import hear

from getNews import getFox
from getNews import getCNN
from getNews import getMSNBC

from getTime import getTime

#initialize names
namesFile = open('names.txt')
nameInFile = namesFile.readlines()
programName = nameInFile[0]
userName = nameInFile[1]

speak(getTime() + ", What can I do for you?")

name = 'Henry'
keepGoing = True
while keepGoing:

    if hear() == "get me some news":
        speak("Any particular source? I can show you fox news, CNN or MSNBC")
        if hear() == "fox news":
            speak("Ok. pulling up Fox News")
            getFox()
        elif hear() == "CNN":
            speak("Ok. pulling up CNN")
            getCNN()
        elif hear() == "MSNBC":
            speak("Ok. Pulling Up CNN")
            getMSNBC()

    elif hear() == "change name":
        speak("What would like to call me?")
        name = hear()
        speak("From now on, my name is " + name)
        files = open('names.txt')

    elif hear() == "what is your name":
        speak(name)

    else:
        speak("Im having some trouble")

