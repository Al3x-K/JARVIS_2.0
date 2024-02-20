import pyttsx3 # pip install pyttsx3 == text data to speech

engine = pyttsx3.init() # initialize the engine


# speak function
def speak(audio):
    engine.say(audio) # text to speechs
    engine.runAndWait() # run and wait for the command

def getVoices(voice):
    voices = engine.getProperty('voices') # get the voices
    print(voices[1].id) # print the voices
    if voice == 1:
        engine.setProperty('voice', voices[1].id) # set the male voice
    if voice == 2:
        engine.setProperty('voice', voices[-2].id) # set the female voice

    speak ("hello, how can i help you") # call the function and pass the text to it

while True:
    voice = int(input("Press 1 for male voice\nPress 2 for female voice\n")) # input the text
    #speak(audio) # call the function and pass the text to it
    getVoices(voice) # call the function