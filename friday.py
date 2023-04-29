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
import subprocess as sp


engine = pyttsx3.init()

paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe",
}


# Reminder class
class Reminder:    
    #Reminder
    def set_reminder(engine, command):
        speak(engine, "What should I remind you about?")
        reminder = listen()
        speak(engine, "When do you want to be reminded? Please say the time in hours and minutes.")
        reminder_time = listen()
        try:
            hour, minute = map(int, reminder_time.split())
            now = datetime.datetime.now()
            reminder_datetime = now.replace(hour=hour, minute=minute)
            if now > reminder_datetime:
                reminder_datetime += datetime.timedelta(days=1)
            speak(engine, f"Alright, I will remind you about '{reminder}' at {hour:02d}:{minute:02d}.")
            while True:
                if datetime.datetime.now() >= reminder_datetime:
                    speak(engine, f"Reminder: {reminder}")
                    break
        except ValueError:
            speak(engine, "Sorry, I couldn't understand the time you provided. Please try again.")
        
        # To DO List
    def create_todo_list(engine, command):
        todo_list = []
        speak(engine, "Let's create a to-do list. Please say the tasks one by one. Say 'done' when you're finished.")
        while True:
            task = listen()
            if task == "done":
                break
            todo_list.append(task)
            speak(engine, f"Added: {task}")
        speak(engine, "Here's your to-do list:")
        for task in todo_list:
            speak(engine, task)


# derived class
class TimeDate(Reminder): 
        #Current Time
    def time():
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        speak("the current time is")
        speak(Time)

    #Current Date
    def date():
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        speak("the current date is")
        speak(date)
        speak(month)
        speak(year) 


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()

def calculator():
    os.startfile(paths['calculator'])

# Greetings
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


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
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
        reminder_obj = TimeDate()    
        if 'remind me' in query:
            reminder_obj.set_reminder()
        elif 'to do' in query:
            reminder_obj.create_todo_list()
        elif 'time' in query or 'date' in query:
            reminder_obj.time()
            reminder_obj.date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
        
        elif 'weather' in query:
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'search in chrome' in query:
            speak("What should I search,sir?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
            speak("Here you go sir!")

        elif 'remember that' in query:
            speak("what should i remeber?")
            data = takeCommand()
            speak("you said to me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        
        elif "reminder" in command:
            set_reminder(engine, command)
            
        elif "to-do" in command or "todo" in command:
            create_todo_list(engine, command)

        elif 'have anything friday' in query:
            remember = open('data.txt', 'r')
            speak('here you go!'+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("done boss!")
         
        elif 'camera' in query:
            camera()
            speak("done boss!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("ok sir!going offline")
            quit()
