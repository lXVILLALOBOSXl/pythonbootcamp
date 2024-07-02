import os
import time
import pyautogui
from PIL import ImageGrab, Image

filename = './dinosaur.png'

# Automate the Chrome Dinosaur Game
URL = 'https://elgoog.im/dinosaur-game/'

# Open a new tab in Chrome using AppleScript
os.system("""
osascript -e 'tell application "Google Chrome" to activate'
osascript -e 'tell application "System Events" to keystroke "t" using {command down}'
""")

time.sleep(2)

# Type the URL and start the game
pyautogui.typewrite(URL)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('space')
time.sleep(1)

def check_pixel_color(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    width, height = img.size
    
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if r in range(70, 90) and g in range(70, 90) and b in range(70, 90):
                return True  
                
    return False

# Loop to play the game
while True:
    # Take a screenshot of the game
    screenshot = ImageGrab.grab(bbox=(980, 590, 1110, 650))
    screenshot.save(filename)

    if check_pixel_color(filename):
        pyautogui.press('space')

    time.sleep(0.1)  # Add a small delay to control the loop speed
