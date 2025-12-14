import webbrowser
import os
import requests
import pyttsx3
from gtts import gTTS
import speech_recognition as sr
import pygame
import google.generativeai as genai
import pyaudio

engine=pyttsx3.init()
genai.configure(api_key="AIzaSyDsdiMRIyu6ZC4XVT1S91vVbKmwtbrE058")
model=genai.GenerativeModel("gemini-1.5-flash")

music = {
    "stealth": "https://www.youtube.com/watch?v=JiAlZIW7hsQ&list=RDJiAlZIW7hsQ&start_radio=1",
    "tonight": "https://www.youtube.com/watch?v=8ZIOkbrX_uU&list=RD8ZIOkbrX_uU&start_radio=1",
    "wolf": "https://www.youtube.com/watch?v=lX44CAz-JhU&list=RDlX44CAz-JhU&start_radio=1",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI&list=RDDeumyOzKqgI&start_radio=1",
    "respect": "https://www.youtube.com/watch?v=A134hShx_gw&list=RDA134hShx_gw&start_radio=1",
    "march": "https://www.youtube.com/watch?v=dDiMaUFBvq4&list=RDdDiMaUFBvq4&start_radio=1",
    "golden": "https://www.youtube.com/watch?v=yebNIHKAC4A&list=RDyebNIHKAC4A&start_radio=1",
    "ordinary": "https://www.youtube.com/watch?v=u2ah9tWTkmk&list=RDu2ah9tWTkmk&start_radio=1",
    "tears": "https://www.youtube.com/watch?v=V9vuCByb6js&list=RDV9vuCByb6js&start_radio=1",
    "manchild": "https://www.youtube.com/watch?v=aSugSGCC12I&list=RDaSugSGCC12I&start_radio=1",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=RDJGwWNGJdvx8&start_radio=1",
    "hello": "https://www.youtube.com/watch?v=YQHsXMglC9A&list=RDYQHsXMglC9A&start_radio=1",
    "uptown": "https://www.youtube.com/watch?v=OPf0YbXqDm0&list=RDOPf0YbXqDm0&start_radio=1",
    "thick of it": "https://www.youtube.com/watch?v=At8v_Yc044Y&list=RDAt8v_Yc044Y&start_radio=1",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc&list=RD7wtfhZwyrcc&start_radio=1",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA&list=RD60ItHLz5WEA&start_radio=1",
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk&list=RDkJQP7kiw5Fk&start_radio=1",
    "let her go": "https://www.youtube.com/watch?v=RBumgq5yVrA&list=RDRBumgq5yVrA&start_radio=1",
    "counting stars": "https://www.youtube.com/watch?v=hT_nvWreIhg&list=RDhT_nvWreIhg&start_radio=1",
    "cheap thrills": "https://www.youtube.com/watch?v=nYh-n7EOtMA&list=RDnYh-n7EOtMA&start_radio=1",
    "love yourself": "https://www.youtube.com/watch?v=oyEuk8j8imI&list=RDoyEuk8j8imI&start_radio=1",
    "rockstar": "https://www.youtube.com/watch?v=UceaB4D0jpo&list=RDUceaB4D0jpo&start_radio=1",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=RD2Vv-BfVoq4g&start_radio=1",
    "see you again": "https://www.youtube.com/watch?v=RgKAFK5djSk&list=RDRgKAFK5djSk&start_radio=1",
    "rolling in the deep": "https://www.youtube.com/watch?v=rYEDA3JcQqw&list=RDrYEDA3JcQqw&start_radio=1",
    "havana": "https://www.youtube.com/watch?v=HCjNJDNzw8Y&list=RDHCjNJDNzw8Y&start_radio=1"
}


def robot_speak(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts=gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def AIProcess(command):
    try:
        response=model.generate_content(f"You are Friday, an AI assistant who helps in day to day simple tasks and who always gives a short clear answer\nUSER : {command}")
        return response.text or "Sorry, Didnt understand"
    except Exception as e:
        print(f"[DEBUG] AI Process failed: {e}")

def CommandProcess(c):
    c=c.lower()
    print(f"USER SAID: {c}")

    if "open google" in c:
        webbrowser.open("https://www.google.com/")
    elif "open flipkart" in c:
        webbrowser.open("https://www.flipkart.com/")
    elif "open spotify" in c:
        webbrowser.open("https://open.spotify.com/")
    elif "open jiomart" in c:
        webbrowser.open("https://www.jiomart.com/")
    elif "open shopify" in c:
        webbrowser.open("https://www.shopify.com/in")
    elif "open myntra" in c:
        webbrowser.open("https://www.myntra.com/")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com/")
    elif "open twitter" in c:
        webbrowser.open("https://x.com/")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com/")
    elif "open snapchat" in c:
        webbrowser.open("https://www.snapchat.com/")

    elif "weather" in c:
        r = sr.Recognizer()
        speak("Tell me your city name")
        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=8, phrase_time_limit=8)
                city = r.recognize_google(audio)
                city = city.strip().lower()
                print(f"[DEBUG] City requested: {city}")

                # Step 1: Get coordinates
                geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
                geo_response = requests.get(geo_url).json()
                if "results" not in geo_response or len(geo_response["results"]) == 0:
                    speak(f"Sorry, I couldn't find {city}.")
                    return
                lat = geo_response["results"][0]["latitude"]
                lon = geo_response["results"][0]["longitude"]

                # Step 2: Get weather
                url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                response = requests.get(url).json()
                

                if "current_weather" in response:
                    temp = response["current_weather"]["temperature"]
                    wind = response["current_weather"]["windspeed"]
                    print(f"The current temperature in {city} is {temp}Â°C with wind speed {wind} km/h")
                    speak(f"The current temperature in {city} is {temp}Â°C with wind speed {wind} km/h")
                else:
                    speak("Sorry, I couldn't fetch the weather right now.")

            except Exception as e:
                print(f"[DEBUG] Weather error: {e}")
                speak("Sorry, I couldn't recognize the city name.")

    elif "search" in c:
        que=c.replace("search","").strip()
        if que:
            speak(f"Searching {que}")
            webbrowser.open(f"https://www.google.com/search?q={que}")
        else:
            speak("Please tell me what to search")
    elif c.startswith("play"):
        words=c.split(" ",1)
        if len(words)>1:
            song=words[1].lower()
            if song in music:
                link=music[song]
                webbrowser.open(link)
            else:
                speak("Cant find your song")
        else:
            print("No song found")
    else:
        output=AIProcess(c)
        print(f"AI Response: {output}")
        speak(output)

if __name__=="__main__":
    speak("Initializing.......")

    while True:
        r=sr.Recognizer()
        print("Recognizing your request.....")


        try:
            with sr.Microphone() as source:
                print("I am Listning.......")
                audio=r.listen(source,timeout=8,phrase_time_limit=8)

                word=r.recognize_google(audio)
                print(f"Heard you say my name : {word}")

                if word.lower() == 'friday':
                    print("Heard my name: Friday")
                    speak("Ask your query")

                    with sr.Microphone() as source:
                        print("Friday Activated: Listning for command")
                        audio=r.listen(source,timeout=8,phrase_time_limit=8)
                        command=r.recognize_google(audio)
                        print(f"Command Analyzed: {command}")

                    if command.lower() in ["exit", "quit", "stop", "shutdown"]:
                        speak("Shutting down, Goodbye")
                        break
                    
                    CommandProcess(command)

        except sr.WaitTimeoutError:
            print("Timeout: no speech detected")

        except sr.UnknownValueError:
            print("Cant understand what you are saying")

        except sr.RequestError as e:
            print(f"Could not request results : {e}")       