# packages required
import sys
import pyttsx3 as p
import speech_recognition as sr
import  selenium_web
import randfacts
import datetime
import os

# files
from google import *
from yt import *
from news import *

#this is for changes in voice speed and tone. 

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')

# after command , it will wait to listen

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#  will wish the user according to time and date

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour < 12:
        return("Good morning")
    elif(hour>=12) and hour<16:
        return("Good afternoon")
    else:
        return ("Good evening")
    
    

today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("hello sir," + wishme() +  ", i am your voices assistant, how are you?")
speak("Today is "+ today_date.strftime("%d") + " of " + today_date.strftime("%B") +", And is currently " + today_date.strftime("%I") + today_date.strftime("%M") + today_date.strftime("%p"))
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    
    
if "what" and " about" and "you" in text:
    speak("I am also having a good day sir")
    speak("what can i do for you?")


else :
    speak("what can i do for you?")

# to get the input from microphone as source

with sr.Microphone() as source:     
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)
    
#checks whether the input contans the word or not
 
if "information" in text2:
    speak("You need information related to which topic?")
    
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    
    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))
    
    assist = selenium_web.infow()
    assist.get_info(infor)
    
elif "play" and "video" in text2:
    speak("you want me to play which video??")
    
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("Playing {} on youtube".format(vid))
    print("Playing {} on youtube".format(vid))

    assist = music()
    assist.play(vid)
        
elif "news" in text2:
    print("Sure sir, let me read news for you.")
    speak("Sure sir, let me read news for you.")
    
    
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
        
elif "fact" or "facts" in text2:
    speak("sure sir")
    x= randfacts.getFact()
    print(x)
    speak("did you know that, "+x)

elif "open" and "google" in text2:
    speak("what should I search on google?")
    
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        search_key = r.listen(source)
        keyword_ = r.recognize_google(search_key)
    
    speak("searching {} on google".format(keyword_))
    print("searching {} on google".format(keyword_))
    
    assist = google_search()
    assist.google_info(keyword_)

elif "joke" or "jokes" in text2:
    speak("sure sir,")
    arr=joke()
    print(arr[0])
    speak(arr[0]) 
    print(arr[1])
    speak(arr[1])  
    

elif "sleep now" in text2 :
	speak("Thank you sir using Me , Have A Good Day....")
	sys.exit()

    
    
    
    
    
        
            












    