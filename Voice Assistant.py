#! /usr/bin/python3

print("content-type: text/html")
print()

import speech_recognition as sr
import subprocess as sp
import pyttsx3 as p

print("Welcome! I am Ron!")
p.speak("Welcome! I am Ron!")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Well! Who are you?")
    p.speak("Well! Who are you?")
    name = r.record(source, 5)
    myname = r.recognize_google(name)
    p.speak("Hello!" + myname)

print("How can i help you ?")
p.speak("How can i help you ?")
response = True
while response:
    with sr.Microphone() as source:
        print("---Speak Now---")
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, 10)
        print("---Audio Recorded---")

    try:
        data = r.recognize_google(audio)
        print("Your request: ", data)

        if ("what is your name" in data) or ("what's your name" in data) or ("who are you" in data):
            p.speak("This is Ron your voice assistant")
        elif ("bye" in data) or ("thank" in data):
            print("bye")
            p.speak("It's my pleasure! Have a great day!")
            response = False
        elif ("how are you" in data):
            p.speak("I am doing well!")
        elif ("cal" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("cal")
            print(res)
        elif ("date" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date")
            print(res)
        elif ("clock" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("while true; do echo -en `date +%T``sleep 1`\"\\b\\b\\b\\b\\b\\b\\b\\b\" ; done &")
            print(res)
        elif ("day" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date +%A")
            print(res)
        elif ("month" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date +%B")
            print(res)
        elif ("time" in data) and (("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("date +%T")
            print(res)
        elif ("cal" in data) and ("this year") and (
                ("show" in data) or ("open" in data) or ("run" in data) or ("execute" in data)):
            res = sp.getoutput("cal -y")
            print(res)
        else:
            print("Invalid")
            p.speak("Sorry! I couldn't figure out what you said!")
    except Exception:
        print("Sorry! I can't get you")
        p.speak("Sorry! I can't get you")