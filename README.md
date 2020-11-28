# The Crappy Amazon Bot

This repo uses the [pyautogui](https://github.com/asweigart/pyautogui) library, which is distributed under the BSD 3-Clause "New" or "Revised" License
This repo uses the [opencv-python](https://github.com/asweigart/pyautogui) library, which is distributed under the MIT License

## Motivation

I'm tired of scalpers buying up in demand parts (like the latest processors and graphics cards) and upselling them. I wanted to create a way to help regular people get the parts they wanted without building something that could be scaled to be used for high volume purposes, and thus the Crappy Amazon Bot was created. Please distribute this bot.

## Summary
A bot that uses the OpenCV vision libraries to locate buttons on your screen and attempt to buy things on Amazon. 

## Features

### Highly unscalable

The bot identifies elements on the web browser and moves the mouse to click them. It can only interact with the focused window so it can only try and buy 1 item at a time. In most cases an individual person wouldn't be able to deploy several instances of this bot, but many people deploying one or two instances of this bot will be very disruptive to scalpers.

### Human speed at best

The bot takes time to identify elements on the screen and to click them. It is not interacting with APIs and is held back by Amazon's refresh rate limits.

### Easy to setup

Requires python and a few open source python packages. Easy to setup, easy to distribute. 

## Setup

1. [Install python](https://wiki.python.org/moin/BeginnersGuide/Download) on your machine
2. If needed [Install pip]
3. Open a python shell/command line/terminal in this folder and run `pip install -r requirements.txt`

## Using the Bot

1. Open Amazon on a web browser
2. Login to your Amazon account 
3. [Enable One Click Ordering](https://www.amazon.com/gp/help/customer/display.html?nodeId=201889620) in your account
4. Navigate to the listing of the item you want to buy
5. Use the python shell/command line/terminal to start the bot `python crappy_amazon_bot.py` or double click the `crappy_amazon_bot.py` script to start it
6. Within the next 5 seconds, Click on the browser window with the open listing visible
7. Leave your computer alone and let the bot do its thing