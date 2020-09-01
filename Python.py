import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("JARVIS: ", audio)
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning mam!")
    else:
        speak("Hey Hello Welcome mam!")
        speak("How may I help you!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
       
    except Exception as e:
        print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https:\\web.whatsapp.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir = 'G:\\Songs\\Hindi'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[6]))

        elif 'exit execution' in query:
           sys.exit(0)    
        