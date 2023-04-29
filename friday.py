import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import subprocess as sp

engine = pyttsx3.init()

paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe",
}

def calculator():
    os.startfile(paths['calculator'])

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date =  int(datetime.datetime.now().day)
    speak("the currect date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Boss!")
        speak("Lets Start the Work")
    if hour >= 12 and hour < 18:
        speak("Good afternoon Boss")
        speak("Make it Happen!")
    if hour >= 18 and hour < 24:
        speak("Good evening Boss")
        speak("The Day is not over yet!")
    else:
        speak("Good Night Boss")
    speak("Friday at your service , Please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening your voice.....................")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing Voice......")
        query = r.recognize_google(audio,language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("unable to recognize! Say Again!!")
        return None
    return  query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com','1234')
    server.sendmail('email@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)
        elif 'send mail' in query:
            try:
                speak("what should i say sir!")
                content = takeCommand()
                to = 'otheraddress@yahoo.com'
                sendEmail(to,content)
                speak("ok sir!, the mail has been sent")
            except Exception as e:
                print(e)
                speak("unable to send mail hard luck , sir!")
        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said to me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'have anything friday' in query:
            remember = open('data.txt','r')
            speak('here you go!'+remember.read())
        elif 'cpu' in query:
            cpu()
        elif 'offline' in query:
            speak("ok sir! going offline")
            quit()
