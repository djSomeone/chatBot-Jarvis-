import speech_recognition as sr
import pyttsx3
import test

# Initialize recognizer
recognizer = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Speed (default: 200)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
print("Wait I am Starting my self...")
# Use the microphone as the input source
with sr.Microphone() as source:
    while True:
        print("Say something...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You: "+text)
            response=test.myChatBot(text)
            print("Jarvis: "+response)
            engine.say(response)
            engine.runAndWait()    
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")