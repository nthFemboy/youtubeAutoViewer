from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from os import system, name
import pyautogui

def cls():
    system('cls' if name == 'nt' else 'clear')

def menu():
    print("1 - Enter url")
    print("2 - Exit")
    userInput = input(">>> ")
    return userInput

def view_video(url, count, time):
    # Setup Chrome options to disable GPU
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    
    # Create a driver instance with the specified options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    i = 0
    while i < count:
        driver.get(url)  # Make sure URL is valid
        sleep(4)
        pyautogui.press('space')  # Start the video
        sleep(time)  # Wait before next view
        i += 1
    
    driver.quit()  # Close the driver after all iterations
    cls()
    print("Views have finished.\nThank you!")

if __name__ == "__main__": 
    while True:
        cls()
        userInput = menu() 
        cls()
        if userInput == "1":
            print("Enter the URL")
            url = input("? ").strip()
            
            # Ensure the URL is complete (starts with "https://")
            if not url.startswith("https://"):
                print("Invalid URL format. Please start the URL with 'https://'.")
                continue
            
            cls()
            print("Enter the amount of times you want to view the YouTube video")
            count = int(input("? "))

            cls()
            print("How long would you like to view the video (minimum is 30s)?")
            time = int(input("? "))

            if (time < 30):
                time = 30

            view_video(url, count, time)

        elif userInput == "2":
            print("Goodbye :3")
            exit(0)

        else:
            print("Invalid input, please try again.")
