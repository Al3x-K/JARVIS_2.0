import pyttsx3 # pip install pyttsx3 == text data to speech

engine = pyttsx3.init() # initialize the engine


# speak function
def speak(audio):
    engine.say(audio) # text to speechs
    engine.runAndWait() # run and wait for the command

while True:
    audio = input("Enter the text to convert it into speach: \n") # input the text
    speak(audio) # call the function and pass the text to it
  