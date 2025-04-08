# YouTube Video Viewer Automation

This script automates the viewing of YouTube videos a specified number of times with configurable viewing durations. It utilizes Selenium and Python to control a Chrome browser and simulate user interactions. **Please use this script responsibly and ensure compliance with YouTube's Terms of Service.**

## Features
- Automates opening a YouTube video URL.
- Simulates pressing the spacebar to start the video.
- Allows customization of the number of views and the duration of each view.
- Optionally randomizes the viewing time to mimic human-like behavior.
- Clears the console between actions for a cleaner user experience.

## Bugs
- **Video Playback Interruption**: YouTube may display an error message and stop playback after approximately 19 seconds when using this script. This behavior is likely due to YouTube detecting automated interactions.

## Requirements

Before running the script, ensure you have the following libraries installed:

- **Selenium**: For browser automation.
- **webdriver_manager**: For automatic management of ChromeDriver.
- **pyautogui**: For simulating key presses.
- **time**: For introducing delays between actions.
- **os**: For clearing the terminal screen.

Install the required libraries using pip:

```bash
pip install -r requirements.txt
