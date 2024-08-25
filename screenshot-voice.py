import pyttsx3
import speech_recognition as sr
import pyautogui
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Sorry ,there was a request error."

def take_screenshot():
    screenshot = pyautogui.screenshot()
    file_name = f"screenshot_{int(time.time())}.png"
    screenshot.save(file_name)
    speak("Screenshot taken")
    print(f"Screenshot saved as {file_name}")

if __name__ == "__main__":
    speak("Say 'take screenshot' to capture the screen.")

    while True:
        command = listen_command()
        if "take screenshot" in command:
            take_screenshot()
        elif 'exit' in command:
            speak("Exiting")
            break
        else:
            speak("waiting for the 'take screenshot' command")