import  speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif "open facebook" in c.lower():
          webbrowser.open("https://google.com")
     elif "open youtube" in c.lower():
          webbrowser.open("https://google.com")
     elif "open linkedin" in c.lower():
          webbrowser.open("https://google.com")
     print(c)
     pass
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #listen for the word jarvis
        #obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            audio = r.litsen(source, timeout=2)
        #recognize speech using Sphinx
        print('recognizing')
        try:
            with sr.Microphone() as source:
                 print("listening...")
                 audio = r.listen(source , timeout = 2 , phase_time_limit = 1)
            word = r.recognize_googlee_cloud(audio)
            if word.lower() == "jarvis" :
                 speak("ya")
                 #litsen foe command
                 with sr.Microphone() as source:
                    print("Jarvis active")
                    audio = r.listen(source) 
                    commsnd = r.recognize_google(audio)
                    
                    processCommand(command)
        except sr.UnknownValueError:
                print("sphinx could not understand audio")
        except sr.RequestError as e:
                print("sphinx error; {0}".format(e))        



