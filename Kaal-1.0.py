import pyttsx3 #pip install pyttsx3
import datetime #for Date and Time 
import speech_recognition as sr #pip install speechRecognition
import wikipedia # pip install wikipedia
import smtplib # pip install smtplib
import webbrowser as wb #pip install webbrowser
import psutil # pip install psutil
import pyjokes # pip install pyjokes
import pyautogui #pip install pyautogui
import os #pip install os
import random #pip install random
import wolframalpha # pip install wolframalpha
import json # pip instakll json
import time
import numpy as np
import requests # pip install requests
from urllib.request import urlopen

engine = pyttsx3.init()
wolframalpha_app_id = 'WWHELG-57L2GT9UWE'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #24 Hour Time
    speak("the current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme_():

    #Greating
    
    speak("Hello Kaal sir !")

    hour = datetime.datetime.now().hour

    if 4 <= hour <= 12:
        speak("Good Morning sir!")
    elif 12 <= hour <=16:
        speak("Good afternoon sir!")
    elif 16 <= hour <=23:
        speak("Good evening sir!")
    else:
        speak("good night sir!")

    speak("I  am  Chotu   and  HOW can help you ")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say That Again Please.....")
        return "None"
    
    return query
def sendEmail(to,content):
    sever=smtplib.SMTP('smtp.gmail.com',587)
    sever.ehlo()
    sever.starttls()
    # For this function ,You must be enable low security in Gmail which are used to send Email  
    sever.login('shivambhairav@gmail.com','25111900')
    sever.sendmail('shivambhairav@gmamil.com',to,content)
    sever.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at '+usage)

    battery = psutil.sensors_battery()
    speak('battery percentage at ')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/YESVEER SINGH/OneDrive/Pictures/Screenshots/pic.png')

if __name__ == "__main__":
    
    wishme_()

    while True:
        query = TakeCommand().lower()

        #All commmand will be start in lower case in query
        #for easy recognition

        if 'time' in query:  # tell us time when we ask
            time_()
        elif 'date' in query: # tell us date when we ask 
            date_()
        elif 'wikipedia' in query: # wikipedia search any queary
            speak("Searching...")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=4)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'how are you' in query: 
            speak("Thankyou for Asking   I am fine sir!  I hope you are also fine ")
            print("I am fine sir")
        elif 'where are you' in query:
            speak("I live in cloud and only in your coumputer ")
            print("I am in your computer harddisk")
        elif 'papa' in query:
            speak("Thanks")
        elif 'who are you' in query:
            speak("i  am  Chotu  a virtiual assistant of Shivam sir! ")
            print("I am  Chotu  a virtiual assistant look like a JARVIS sir!")
        elif 'developer' in query:
            speak('kaal bhairav sir and also know as Yesveer shivam sir')
            print("Kaal Bhairav")
        elif 'send email' in query:
            try:
                speak("What should I say ?")
                content=TakeCommand()
                #provide reveciver mail adderess
               
                speak("Who is Reciever")
                reciever=input("Enter Reciever's Email:")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent")
                print("Email has been sent")

            except Exception as e:
                print(e)
                speak("unable to sent Email")
        elif 'search in chrome' in query:
            speak("what whould I search")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe  %s'
            # chromepath is location of installation of chrome in your computer 

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #only open .com website extension

        elif 'search in youtube' in query:
            speak('What should I search ?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe  %s'
            search_Term = TakeCommand().lower()
            speak('Here we go to youtube')
            wb.get(chromepath).open_new_tab('https://www.youtube.com/results?search_query= '+search_Term)

        elif 'search in google' in query:
            speak('what should I search ?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe  %s'
            search_Term = TakeCommand().lower()
            speak('Searching.....')
            wb.get(chromepath).open_new_tab('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()    
        
        elif 'jokes' in query:
            jokes()
        
        elif 'go offline' in query:
            speak("going to offline")
            quit()
        
        elif 'android stdio' in query:
            speak("opening android stdio....")
            stdio = r'C:/Program Files/Android/Android Studio/bin/studio64.exe'
            os.startfile(stdio)

        elif 'ardunio' in query:
            speak("opening ardunio app.......")
            ardunio = r'C:/Program Files (x86)/Arduino/arduino.exe'
            os.startfile(ardunio)

        elif 'excel' in query:
            speak("opening ms excel.......")
            excel = r'C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE'
            os.startfile(excel)

        
        elif 'atom' in query:
            speak("opening atom.......")
            atom = r'C:/Users/YESVEER SINGH/AppData/Local/atom/atom.exe'
            os.startfile(atom)

        elif 'chrome' in query:
            speak("opening GOOgle chrome.......")
            chrome = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
            os.startfile(chrome)

        elif 'powerpoint' in query:
            speak("opening ms powerpoint.......")
            powerpoint = r'C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE'
            os.startfile(powerpoint)

        elif 'Visual stdio code' in query:
            speak("opening visual stdio code........")
            visual = r'C:/Users/YESVEER SINGH/AppData/Local/Programs/Microsoft VS Code/Code.exe'
            os.startfile(visual)

        elif 'word' in query:
            speak("opening ms word.......")
            word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(word)

        elif 'virtual box' in query:
            speak("opening virtuial box......")
            box = r'C:/Program Files/Oracle/VirtualBox/VirtualBox.exe'
            os.startfile(box)

        elif 'thankyou' in query:
            speak("your welcome sir!")

        elif 'thanks' in query:
            speak("donot say thanks , its my work and your welcome sir!")

        elif 'write a notes'  in query:
            speak("what should i write sir!")
            notes = TakeCommand()
            file = open('note.txt','w')
            speak("should i include date and time ?")
            ans = TakeCommand()
            if 'yes' in ans or 'Sure' in ans:
                strTime = datetime.datetime.now().strftime("%H %M %S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("done ! take notes from  you sir!")

            else:
                file.write(notes)

        elif 'show notes' in query:
            speak("showing notes...")
            file = open('notes.txt','r')
            print(file.read())
            speak(file())

        elif 'screenshot' in query:
            screenshot()

        elif 'play song' in query:
            song_dir = 'D:/New song'
            music = os.listdir(song_dir)
            speak("what should i play for you ")
            speak("select a number or random..")
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'your choose'):
                speak('I could not understand you. please try again sorry for understanding')
                ans = TakeCommand().lower()

            if 'number' in ans:
               no = int(ans.replace('number',''))

            elif 'random' or 'your choose' in ans:
                no = random.randint(1,100)

            os.startfile(os.path.join(song_dir,music[no]))

        elif 'remember that' in query:
            speak("what should i remember")
            memory = TakeCommand()
            speak("you ask me remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'Do you remember anything' in query:
            remember = open('memory.txt','r')
            speak("you ask me remember that "+remember.read())

        elif 'chhotu' in query:
            speak("yes sir how can i help you")
            TakeCommand()

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User ask the location"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The Answer is : "+answer)
            speak("The Answer is "+answer)

        elif 'mummy' in query:
            speak(" mummy jii         Nameste         mummy    jii  how are you!")

        elif 'fine' in query:
            speak("thankyou for your response mummy jii..")

        elif 'mummy name' in query:
            speak("thanks")

        elif 'what is' and 'who is' in query:
            #use the same  API key that we generated earlier i.e wolframalpha
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No Result")

        elif 'stop listening' in query:
            speak("for how many second you want to stop listening to your command")
            ans = int(TakeCommand())
            speak("I am sleeping for "+ans)
            speak("second")
            time.sleep(ans)
            print(ans)

        elif 'tech news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4c418740147749079469314f27e20260")
                data = json.load(jsonObj)
                i = 1

                speak("here are some top headlines from tech news")
                print("=============TOP HEADLINES================="+"/n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'/n')
                    print(item['description']+'/n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        elif 'enterainment news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?sources=entertainment&apiKey=4c418740147749079469314f27e20260")
                data = json.load(jsonObj)
                i = 1

                speak("here are some top headlines from entertainment news")
                print("=============TOP HEADLINES================="+"/n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'/n')
                    print(item['description']+'/n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))  

        elif 'sport news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?sources=sports&apiKey=4c418740147749079469314f27e20260")
                data = json.load(jsonObj)
                i = 1

                speak("here are some top headlines from sports news")
                print("=============TOP HEADLINES================="+"/n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'/n')
                    print(item['description']+'/n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e)) 


        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("/s /t 1")
