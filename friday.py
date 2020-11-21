import pyttsx3  # pip install pyttx3
import datetime
# pip install SpeechRecognition,for speech recognition
import speech_recognition as sr
import wikipedia  # pip install wikipedia
import smtplib  # for sending mails
import webbrowser as wb  # for chrome search
import os
import pyautogui  # pip install pyautogui ,for screenshot
import psutil  # pip install psutil ,for battery and cpu usage
import pyjokes  # pip install pyjokes,for jokes


engine = pyttsx3.init()


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
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning boss!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon boss!")
    elif hour >= 18 and hour < 24:
        speak("Good evening boss")
    else:
        speak("Good night boss")
    speak("Friday at your service Please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("unable to recogninize!Say again please!")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', '1234')
    server.sendmail('email@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/kumar/OneDrive/Pictures/Screenshots/ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def jokes():
    speak("ok boss")
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send mail' in query:
            try:
                speak('what should I say,sir!')
                content = takeCommand()
                to = 'otheraddress@yahoo.com'
                sendEmail(to, content)
                speak("ok sir,the mail has been sent")
            except Exception as e:
                print(e)
                speak("unable to send mail,sir")

        elif 'search in chrome' in query:
            speak("What should I search,sir?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
            speak("Here you go sir!")

        elif 'play songs' in query:
            songs_dir = 'C:/Users/kumar/OneDrive/Desktop/Music'
            songs = os.listdir(songs_dir)
            speak("ok sir,playing song")
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("what should i remeber?")
            data = takeCommand()
            speak("you said to me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'have anything friday' in query:
            remember = open('data.txt', 'r')
            speak('here you go!'+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("done boss!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("ok sir!going offline")
            quit()
