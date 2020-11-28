import pyautogui
import cv2
import random
import time
import datetime


def locateAndClick(image_name, cooldown):
    button_location = pyautogui.locateOnScreen(image_name, confidence=0.9)
    if button_location:
        button_x, button_y  = pyautogui.center(button_location)
        pyautogui.click(button_x, button_y)
        time.sleep(2)
        return 0
    return cooldown


random.seed(datetime.datetime.now())
print("5 Seconds to click on the Amazon Page you want to watch")
time.sleep(5)
while True:
    cooldown = random.randint(10,30)

    # Buying Logic
    locateAndClick('Buy_Now.png', cooldown)
    locateAndClick('No_Warranty.png', cooldown)
    locateAndClick('Place_Your_Order.png', cooldown)

    # Yay we bought the item 
    if pyautogui.locateOnScreen('Check.png', confidence=0.9):
        print("Order Placed!")
        break

    # Time to try again
    if cooldown==0 :
        print(f"RIP. Was in stock around {datetime.datetime.now(datetime.timezone.utc)}")
    print(f"Refreshing page in {cooldown} seconds")
    time.sleep(cooldown)
    pyautogui.press('f5')
    time.sleep(2)
    pyautogui.press('home')
