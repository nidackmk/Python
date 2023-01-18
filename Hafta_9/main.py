"""
pyautoui ile klavye ve mouse işlemleri
"""

import pyautogui

pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInBounce)

screenWidth, screenHeight = pyautogui.size()
print("ekran çözünürlüğü:", screenWidth, screenHeight)

"""
webviev 
Tkinter --- pythonla birlikte gelir (builtin function)
visualTk
Qt
"""
from tkinter import *

window= Tk()
"""
window.title("hello world")

window.geometry('500x500')

btn=Button(window, text="Tıkla")
btn.grid(column=1, row=2)
btn2=Button(window, text="Tıkla Renkli", bg="purple", fg="black", width=10, height=10)


programın biz çarpıya bastıktan sonra kapanması için
window.mainloop()"""

