from cProfile import run
from datetime import datetime
from distutils import command
from distutils.ccompiler import gen_preprocess_options
from email.mime import audio
from http import server
import imp
from importlib.resources import contents
from logging import exception
from socket import if_nametoindex
from unittest import result

from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Champ sir. Please tell me how may I help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query


def sendEmail(to, contents):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sumitbhadane416@gmail.com', 'sumit@123')
    server.send('rohitbhadane310@gmail.com', to, contents)
    server.close()


if __name__ == "__main__":
    #  speak("Rohit is good boy")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia.....")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'play music' in query:
            music_dr = 'E:\\music'
            song = os.listdir(music_dr)
            print(song)
            os.startfile(os.path.join(music_dr, song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir , the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Rohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to rohit' in query:
            try:
                speak("what should I say?")
                contents = takeCommand()
                to = 'rohitbhadane310@gmail.com'
                sendEmail(to, contents)
                speak("Email has been send!!")
            except exception as e:
                print(e)
                speak("sorry to say ! I am not able to send this email")

        elif 'stop' in query:
            exit()
