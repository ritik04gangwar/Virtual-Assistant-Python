import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Kindly start speaking.....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognising audio......")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Unable to listen....")

def speechtxt(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',100)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':
    if 'hey gordon' in speechtxt().lower():
        
        while True:
            data1=speechtxt.lower()
            if 'your name' in data1:
                name='my name is gordon'
                speechtxt(name)
            elif 'old are you' in data1:
                age='i am 3  years old'
                speechtxt(age)
            elif 'time now' in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                speechtxt(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'joke' in data1:
                joke1=pyjokes.get_joke(language="en",category="neutral")
                speechtxt(joke1)
            elif 'play song' in data1:
                add="C:\Users\Ritik Gangwar\Music"
                listsong=os.listdir(add)
                os.startfile(os.path.join(add,listsong[0]))
            elif 'exit' in data1:
                speechtxt("thank you have a nice day")
                break

            time.sleep(10)

    else:
        print("Say the given words: yo bro....")