import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == "__main__":
    while True:
        query =takeCommand().lower()
        if "wake up "in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query =takeCommand().lower()
                
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                

                if "go to sleep " in query:
                    speak("Ok sir ,You can call me anytime")
                    break
                
                elif "hello" in query:
                    speak("Hello sir. How are you ?")
                elif "i am fine " in query:
                    speak("That's great sir")
                elif "How are you " in query:
                    speak("Perfect sir")
                elif "Thank you" in query:
                    speak("You welcome sir")
                    
                elif "google" in query:
                    from SearchNow import searchgoogle
                    searchgoogle()
                
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube()
                elif "wkipedia" in query:
                    from SearchNow import searchWikipeadia
                    searchWikipeadia(query)
            