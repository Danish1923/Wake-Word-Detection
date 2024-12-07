import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Define wake words
wake_words = ["HELP PLEASE", "EMERGENCY"]

# Function to speak the response
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to detect wake words
def detect_wake_word():
    with sr.Microphone() as source:
        print("Listening...")
        
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio).upper()
            print(f"You said: {command}")
            
            # Check if any wake word is in the recognized text
            if any(wake_word in command for wake_word in wake_words):
                print("I will help you")
                speak("I will help you")
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Continuously listen for wake words
while True:
    detect_wake_word()
