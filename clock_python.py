from tkinter import *
import time

window = Tk()
window.title('Digital Clock')
window.geometry("600x400")


def myTime():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    zone = time.strftime("%Z")
    myText = hour + ":" + minute + ":" + second + am_pm
    myText2 = day + "--" + zone
    myLable2.config(text=myText2)
    myLable.config(text=myText)
    myLable.after(1000, myTime)


myLable = Label(window, text="", font=(
    "Arial", 72), fg='white',  bg='black')
myLable.pack()
myLable2 = Label(window, text="", font=(
    "Arial", 28), fg='black',  bg='white')
myLable2.pack()
myTime()
window.mainloop()
