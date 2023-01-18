from tkinter import *

sifre="abc"

window= Tk()
window.title("ornek uygulama")
window.geometry('500x500')

L1 = Label(window, text="Adınızı Girin")
L1.grid(padx=110, pady=10)

E1 = Entry(window, bd =2)
E1.grid(padx=110, pady=3)

L1=input("şifrenizi giriniz:")

if(sifre==L1):

window.mainloop()

