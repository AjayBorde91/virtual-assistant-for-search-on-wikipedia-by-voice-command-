#print('ajay')
import pyttsx3
import datetime
import pyaudio
import wikipedia 
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
#print(voices) #testing
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning sir .")
    elif hour>=12 and hour <18:
        speak("good afternoon sir .")
    else:
        speak("Good evening sir .")
    speak("I am scam  , your private voice based virtual assistant , sir ,  tell me hoe cam i help you ?")    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


 

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' or 'who' in query:  #if wikipedia found in the query then this block will be executed
            speak('got it sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to my knowledge")
            #print(results)
            speak(results)

    
