import pyautogui
from time import sleep

text = input("Enter text: ")
number = int(input("Times: "))
sleep(5)
for i in range(number):
    pyautogui.typewrite(text)
    pyautogui.press("enter")
    sleep(0.5)




