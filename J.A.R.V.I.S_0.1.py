import pyttsx3 # pip install pyttsx3 == text data to speech
import datetime # pip install datetime == date and time
engine = pyttsx3.init() # initialize the engine


# speak function
def speak(audio):
    engine.say(audio) # text to speechs
    engine.runAndWait() # run and wait for the command

def chooseVoice(voice):
    voices = engine.getProperty('voices') # get the voices
    print(voices[1].id) # print the voices
    if voice == 1:
        engine.setProperty('voice', voices[1].id) # set the male voice
    if voice == 2:
        engine.setProperty('voice', voices[-2].id) # set the female voice

    speak ("hello, how can i help you") # call the function and pass the text to it

def getCurrentTime():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # get the time
    speak("The current time is: ") 
    speak(Time)

def getCurrentDate():
    year = datetime.datetime.now().year # get the year
    month = datetime.datetime.now().month # get the month
    day = datetime.datetime.now().day # get the day
    speak("The current date is: ")
    speak(day)
    speak(month)
    speak(year)

while True:
    voice = int(input("Press 1 for male voice\nPress 2 for female voice\n")) # input the text
    #speak(audio) # call the function and pass the text to it
    chooseVoice(voice) # call the function
    getCurrentTime()
    getCurrentDate()
    
