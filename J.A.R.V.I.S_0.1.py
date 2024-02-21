import pyttsx3 # pip install pyttsx3 == text data to speech
import datetime # pip install datetime == date and time
import speech_recognition as sr # pip install speechRecognition == speech recognition

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

    #speak ("hello, how can i help you") # call the function and pass the text to it

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

def welcomeBack():
    greeting()
    getCurrentTime()
    getCurrentDate()
    speak("How can i help you?")

def greeting():
    hour = datetime.datetime.now().hour # get the hour
    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening!")
    else:
        speak("Good Night!")

# main function
#while True:
 #   voice = int(input("Press 1 for male voice\nPress 2 for female voice\n")) # input the text
    #speak(audio) # call the function and pass the text to it
  #  chooseVoice(voice) # call the function
   # getCurrentTime()
    #getCurrentDate()
        

def takeCommandCMD(): 
    query = input("Please tell me how can i help you: \n") # input the text
    return query # return the text

def takeCommandMic():
    r = sr.Recognizer() # recognize the speech
    with sr.Microphone() as source: # get the microphone
        print("Listening...") 
        r.pause_threshold = 1 # pause the threshold
        audio = r.listen(source) # listen to the audio
    try: 
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in') # recognize the audio
        print(f"User said: {query}\n") # print the audio
    except Exception as e: 
        print("Say that again please...") 
        return "None" 
    return query # return the audio


if __name__ == "__main__":
    welcomeBack()
    while True:
        query = takeCommandMic().lower() # input the text and convert it to lower case
        if "time" in query:
            getCurrentTime()
        elif "date" in query:
            getCurrentDate()