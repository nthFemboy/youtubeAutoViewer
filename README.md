# YouTube Video Viewer Automation

This script allows you to automate the viewing of YouTube videos for a specified number of times with configurable viewing duration. The script uses Selenium and Python to control a Chrome browser and simulate user interactions. It's intended for educational purposes and testing. Please ensure that you're using this script in compliance with YouTube's Terms of Service.

## Features
- Automates opening a YouTube video URL.
- Simulates pressing the spacebar to start the video.
- Allows you to customize the number of views and the duration of each view.
- Optionally randomizes the viewing time to mimic more human-like behavior.
- Clears the console between actions for a cleaner user experience.

## Requirements

Before running the script, ensure you have the following libraries installed:

- **Selenium**: For controlling the browser.
- **webdriver_manager**: For automatically managing ChromeDriver.
- **pyautogui**: For simulating key presses.
- **time**: For introducing delays between actions.
- **os**: For clearing the terminal screen.

You can install the required libraries using pip:

```bash
pip install selenium webdriver_manager pyautogui
