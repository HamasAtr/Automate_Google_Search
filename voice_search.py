import speech_recognition as sr
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):

    engine.say(audio) 

    engine.runAndWait()
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing")

        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

query = takeCommand().lower()
driver = webdriver.Chrome()

driver.get("https://www.google.com")

element = driver.find_element(By.CLASS_NAME, "gLFyf")

element.send_keys(query)
element.send_keys(Keys.ENTER)

# elements = driver.find_elements(By.CLASS_NAME, 'MjjYud')

# texts = [el.text for el in elements]
# pprint(texts)





