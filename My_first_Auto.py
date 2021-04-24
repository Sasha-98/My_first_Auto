import pyautogui as pg
import pywinauto.keyboard
from pywinauto.application import Application
from datetime import datetime

web_address = "y8.com"
pywinauto.keyboard.send_keys('{LWIN}')
pywinauto.keyboard.send_keys("chrome", 0.2)
pywinauto.keyboard.send_keys('{ENTER}',3)
pywinauto.keyboard.send_keys("https://www."+web_address+"/",0.2)
pywinauto.keyboard.send_keys('{ENTER}',10)
screen = pg.screenshot("test.png")

now = datetime.now()
d1 = now.strftime("%d.%m.%Y--%H-%M-%S")

screen.save(r"D:\\BE AQ\\Скрипт\\sitey8_com\\"+"y8.com "+d1+".png")
