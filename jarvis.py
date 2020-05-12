import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import requests
import json
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your personal assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":

	wishMe()
	while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
        
        elif 'open sublimetext' in query:
            sublimepath="C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(sublimepath)
        
        elif 'open android studio' in query:
            studiopath=r'''E:\Desktop\New folder (2)\bin\studio64.exe'''
            os.startfile(studiopath)
            
        elif 'open pycharm' in query:
            pycharmpath="C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.3\bin\pycharm64.exe"
            os.startfile(pycharmpath)
            
        elif 'open Matlab' in query:
            matlabpath="C:\Program Files\MATLAB\R2018a\bin\matlab.exe"
            os.startfile(matlabpath)
            
        elif 'weather' in query:
            speak("which city")
            city=takeCommand()
            apikey="yourapikey"
            url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apikey
            response=requests.request("GET",url)
            
            data=json.loads(response.text)
            weatherdata=data['weather'][0]
            print(weatherdata)
            latest=weatherdata['main'],weatherdata['description']
            speak(latest)
        elif 'dictionary' in query:
            app_id="your_id"
            app_key="your_key"
            endpoint = "entries"
            language_code = "en-us"
            word_id = takeCommand()
            url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
            r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
            meanings=gg=json.loads(r.text)
            meaning=(gg['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'])
            print(meaning)
            speak(meaning)
            
            
            


        elif 'play music' in query:
            music_dir = 'E:\Music\Music'
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)

        elif 'email to Rahul' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = takeCommand()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email") 
        elif 'close' in query:
            break