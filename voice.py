import pyttsx3 as p
import speech_recognition as sr 
from selenium_web import *
from Yt_audio import *
from news import *
import pyjokes
from weather import *
import datetime
import pywhatkit


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty("rate", 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices)
print(rate)

contacts = {
    "manali": "+918097056991",
    "preksha": "+918879655956",
    "sampada didi": "+919137759503",
    "mummy": "+919076151337"
}


def speak(Text):
    engine.say(Text)
    engine.runAndWait()

today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("hello i am your voice assistant vedant") 
speak("Today is " + today_date.strftime("%A, %d %B %Y"))
speak("Temprature in mumbai is "+str(temp())+"degree celcius and with"+str(des()))
speak(" how are u ?") 


with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening....")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if all(word in text.lower() for word in ["what", "about", "you"]):
    speak("I am also having a good day.")

if "i am not well" in text.lower() or "i'm not well" in text.lower():
    speak("Oh no, what happened? Do you want to talk about it?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening....")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic ?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    speak("searching {} in wikipidia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video ?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)
        vid = r.recognize_google(audio)

    speak("playing {} in youtube".format(vid))
    assist=music()
    assist.play(vid)

elif "news" in text2:
    print("Sure,now i will read news for u")
    speak("Sure,now i will read news for u")
    arr = news()
    for i in range(len(arr)):
        speak(arr[i])
        print(arr[i])

elif "joke" and "jokes" in text2:
    joke = pyjokes.get_joke()
    speak("sure gey ready for chukles... ")
    print("sure Here is a joke for you...")
    print(joke)
    speak(joke)


elif "whatsapp" in text2.lower():
    speak("Whom should I send the message to?")
    name = listen().lower()

    if name in contacts:
        number = contacts[name]
        speak(f"Okay, sending message to {name}. What should I say?")
        message = listen()
        speak("At what hour should I send it?")
        hour = int(listen())
        speak("And minutes?")
        minute = int(listen())
        send_whatsapp_message(number, message, hour, minute)
    else:
        speak(f"Sorry, I don't have a contact saved as {name}.")

        
