import time
from datetime import datetime
from pynput.keyboard import Controller,Key
from data import data
import webbrowser
keyboard = Controller()
isStarted = False
for i in data:
    while True:
        if isStarted==False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                if i[0][8] == 'z':
                    webbrowser.open(i[0])
                    isStarted = True
                elif i[0][8] == 't':
                    webbrowser.open(i[0])
                    time.sleep(7)           
                    for i in range(0,7):
                        keyboard.press(Key.tab)
                        time.sleep(1)
                    time.sleep(2)
                    keyboard.press(Key.enter)
                    time.sleep(6)
                    keyboard = Controller()
                    keyboard.press (Key.ctrl )
                    keyboard.press (Key.left )
                    keyboard.press ('m')
                    time.sleep(3)
                    keyboard.release (Key.ctrl )
                    keyboard.release (Key.shift )
                    keyboard.release ('m')
                    isStarted = True

            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                if i[0][8] == 'z':
                    keyboard.press(Key.alt)
                    keyboard.press('q')
                    time.sleep(1)
                    keyboard.press(Key.enter)
                    isStarted = False
                    break
                elif i[0][8] == 't':
                    keyboard.press(Key.ctrl)
                    keyboard.press(Key.shift)
                    keyboard.press('b')
                    time.sleep(0.5)
                    keyboard.release('b')
                    keyboard.release(Key.ctrl)
                    keyboard.release(Key.shift)
                    break
                


