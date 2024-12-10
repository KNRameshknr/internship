import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import random
import time

# Initialize the recognizer and the pyttsx3 engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service.")
        return None

# Function to greet based on time of day
def greet():
    current_hour = int(datetime.datetime.now().hour)
    if current_hour < 12:
        speak("Good morning!")
    elif current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

# Function to tell the time
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Function to tell the date
def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

# Function to open a website
def open_website(command):
    if 'youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'github' in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    else:
        speak("Sorry, I can only open YouTube, Google, or GitHub.")

# Function to play music
def play_music():
    music_folder = "C:\\Users\\YourUsername\\Music"  # Change to your music folder path
    songs = [song for song in os.listdir(music_folder) if song.endswith('.mp3')]
    if songs:
        song_to_play = random.choice(songs)
        song_path = os.path.join(music_folder, song_to_play)
        os.startfile(song_path)
        speak(f"Playing {song_to_play}")
    else:
        speak("No music found in your folder.")

# Function to perform a task based on voice command
def perform_task(command):
    if 'time' in command:
        tell_time()
    elif 'date' in command:
        tell_date()
    elif 'open' in command:
        open_website(command)
    elif 'play music' in command:
        play_music()
    elif 'stop' in command or 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand the command.")

# Main function
def main():
    greet()
    while True:
        command = listen()
        if command:
            perform_task(command)

if __name__ == "__main__":
    main()
