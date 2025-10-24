import speech_recognition as sr
import webbrowser
import pyttsx3
import music_llibrary

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
    elif "google" in command.lower():
        webbrowser.open("https://google.com")
    elif 'youtube' in command.lower():
        webbrowser.open('https://youtube.com')
    elif "quora" in command.lower():
        webbrowser.open("https://quora.com")
    elif "leetcode" in command.lower() or "dsa" in command.lower():
        webbrowser.open("https://leetcode.com")
    elif "portfolio" in command.lower() or "codolio" in command.lower():
        webbrowser.open("https://codolio.com/profile/iamKSR")
    elif "github" in command.lower():
        webbrowser.open("https://github.com")
    elif "anime" in command.lower():
        webbrowser.open("https://anikai.to/")
    elif command.lower().startswith('play'):
        song = command.lower().split(" ")[1]
        link = music_llibrary.music[song]
        webbrowser.open(link)
    


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
