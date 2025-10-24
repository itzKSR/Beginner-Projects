import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def process_command(command):
    print(command)
    if "gpt" in command.lower():
        webbrowser.open("https://chatgpt.com")
    if "google" in command.lower():
        webbrowser.open("https://google.com")
    if 'youtube' in command.lower():
        webbrowser.open('https://youtube.com')
    if "quora" in command.lower():
        webbrowser.open("https://quora.com")
    if "leetcode" in command.lower() or "dsa" in command.lower():
        webbrowser.open("https://leetcode.com")
    if "portfolio" in command.lower() or "codolio" in command.lower():
        webbrowser.open("https://codolio.com/profile/iamKSR")
    if "github" in command.lower():
        webbrowser.open("https://github.com")
    
    if "anime" in command.lower():
        webbrowser.open("https://anikai.to/")

if __name__ == "__main__":
    speak("initialising jarvis..")
    # Listen for audio
    speak("testing voice output")
    while True:
        r = sr.Recognizer()
        # recognize speech using Sphinx                             
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.8)
                print("Listening...")
                audio = r.listen(source, timeout= 8, phrase_time_limit=5)
                print("Recognizing...")
            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("hello master")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.8)
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process_command(command)
        except Exception as e:
            print("Error; {0}".format(e))
