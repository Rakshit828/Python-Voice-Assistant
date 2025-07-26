import pyautogui
import webbrowser
from datetime import datetime

count = 1

def take_screenshot():
    global count #THis tells python explicitly to allow the function to modify the global variable
    screenshot = pyautogui.screenshot()
    screenshot.save(f'screenshot{count}.png')
    count += 1


import webbrowser
import pyautogui
import time

def search_in_google(command):
    if "about" not in command:
        print("No topic found in command.")
        return

    topic = command.split("about", 1)[1].strip().lower()
    print(f"Searching Google for: {topic}")

    webbrowser.open('https://www.google.com')
    time.sleep(3)  # wait for browser to open and page to load

    pyautogui.hotkey('ctrl', 'l')  # focus address bar
    time.sleep(0.5)  # slight delay before typing

    pyautogui.write(topic, interval=0.1)
    pyautogui.press('enter')


def search_in_youtube(command):
    if "about" not in command:
        print("No topic found in command.")
        return

    topic = command.split("about", 1)[1].strip().lower()
    print(f"Searching YouTube for: {topic}")

    webbrowser.open('https://www.youtube.com')
    time.sleep(3)  # YouTube may take longer to load

    pyautogui.hotkey('ctrl', 'l')  # focus address bar
    time.sleep(0.5)

    pyautogui.write(topic, interval=0.1)
    pyautogui.press('enter')


def tell_current_time():
    now = datetime.now()
    formatted_time = now.strftime("%I:%M %p").lstrip("0")  # Removes leading 0 in hour
    return f"The current time is {formatted_time}."


def tell_current_date():
    today = datetime.now()
    formatted_date = today.strftime("%A, %B %d, %Y")
    # Remove leading zero from the day (e.g., '07' -> '7')
    day = today.strftime("%d").lstrip("0")
    formatted_date = today.strftime(f"%A, %B {day}, %Y")
    return f"Today is {formatted_date}."


