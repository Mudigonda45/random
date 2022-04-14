import random
import pyautogui as pg
import time
name = ("","rom,sampath,mohan,sriram")
time.sleep(10)
for i in range (1000):
    a = random.choice(name)
    pg.write('how are you' + a)
    pg.press('enter')
