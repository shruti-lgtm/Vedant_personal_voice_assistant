from tkinter import *
from PIL import Image, ImageTk
import threading
import pyttsx3 as p
import speech_recognition as sr 
from selenium_web import *
from Yt_audio import *
from news import *
from weather import *
import pyjokes
import datetime
import pywhatkit
from itertools import count


# --- Assistant Setup ---
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty("rate", 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "I couldn't understand."
    except sr.RequestError:
        return "Request error."

# WhatsApp Contacts Dictionary
contacts = {
    
}


def run_assistant():
    today_date = datetime.datetime.now()
    speak("Hello, I am your voice assistant Vedant") 
    speak("Today is " + today_date.strftime("%A, %d %B %Y"))
    speak("Temperature in Mumbai is " + str(temp()) + " degree Celsius with " + str(des()))
    speak("How are you?")

    while True:
        text = listen().lower()
        print("User said:", text)

        if "hey vedant" in text or text.strip() == "vedant":
            speak("Yes princess ?")
            text = listen().lower()  
            print("Command after wake word:", text)

        if "stop" in text or "bye" in text or "exit" in text:
            speak("Okay, talk to you soon. Take care!")
            break

        elif "i am fine" in text or "i'm fine" in text:
            speak("What do you want me to do today?")


        elif all(word in text for word in ["what", "about", "you"]):
            speak("I am also having a good day.")
            speak("What do you want me to do today?")

        elif "not well" in text:
            speak("Oh no, what happened? Do you want to talk about it?")
            response = listen().lower()
            print("User said:", response)

            if "yes" in response:
                speak("I'm here for you. Tell me everything.")
            else:
                speak("Okay, take care. I'm always here if you need me.")

        elif "confused" in text or "help" in text or "what should i do" in text:
            speak("Can you tell me more about the situation?")
            situation = listen().lower()
            print("User said:", situation)

            if "friend" in situation:
                speak("Friendship issues can be tough. Try to talk openly with them and understand their side too.")
            elif "study" in situation or "exam" in situation:
                speak("Make a small study plan and stick to it. Focus on one subject at a time.")
            elif "career" in situation:
                speak("Think about what you're passionate about, and also consider what skills you have. Balance both.")
            else:
                speak("Hmm, that's interesting. I think the best way is to stay calm, list your options, and take one step at a time.")

        elif "information" in text:
            speak("You need information related to which topic?")
            topic = listen().lower()
            speak(f"Searching {topic} in Wikipedia")
            assist = infow()
            assist.get_info(topic)

        elif "play" in text and "video" in text:
            speak("You want me to play which video?")
            vid = listen()
            speak(f"Playing {vid} on YouTube")
            assist = music()
            assist.play(vid)

        elif "news" in text:
            speak("Sure, here are the top news headlines")
            for headline in news():
                print(headline)
                speak(headline)

        elif "joke" in text or "jokes" in text:
            joke = pyjokes.get_joke()
            speak("Sure, get ready for some chuckles!")
            print(joke)
            speak(joke)

        elif "send" in text and "whatsapp" in text and "message" in text:
            speak("To whom should I send the message?")
            name = listen().lower().strip()

            if name in contacts:
                number = contacts[name]
                speak(f"What message should I send to {name}?")
                message = listen()
                speak(f"Sending message to {name}: {message}")

                try:
                    pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
                    speak("Message sent successfully.")
                except Exception as e:
                    speak("Sorry, I couldn’t send the message.")
                    print(e)
            else:
                speak("Sorry, I don't have that contact saved.")
        
        elif "hey vedant" in text or text.strip() == "vedant":
            speak("Yes?")
            text = listen().lower()
            print("Command after wake word:", text)
            continue

        else:
            speak("Sorry, I didn't understand that. Could you please repeat?")

# --- GUI Setup ---
root = Tk()  
root.title("Vedant AI")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="black")

chat_label = Label(root, text="Vedant AI: Hello! Click the orb to talk !",font=("Source Code Pro", 15, "bold"),bg="black", fg="white",wraplength=500, justify="left")
chat_label.pack(side=BOTTOM, pady=(0, 60))

class AnimatedGIF(Label):
    def __init__(self, master, path, delay=100, command=None):
        super().__init__(master, bg="black")
        self.frames = []
        self.delay = delay
        self.command = command

        try:
            img = Image.open(path)
            for frame in count(1):
                self.frames.append(ImageTk.PhotoImage(img.copy()))
                img.seek(frame)
        except EOFError:
            pass

        self.index = 0
        self.configure(image=self.frames[0])
        self.after(self.delay, self.animate)
        self.bind("<Button-1>", self.on_click)

    def animate(self):
        self.index = (self.index + 1) % len(self.frames)
        self.configure(image=self.frames[self.index])
        self.after(self.delay, self.animate)

    def on_click(self, event):
        if self.command:
            threading.Thread(target=self.command).start()

# --- Only the animated GIF in center ---
gif_button = AnimatedGIF(root, "image/Is a ball by Siri.gif", delay=50, command=run_assistant)
gif_button.pack(expand=True)

root.mainloop()