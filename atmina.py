from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("vienādie attēli")

btn0=Button(width=20, height=10, image=bgImg)
btn1=Button(width=20, height=10, image=bgImg)
btn2=Button(width=20, height=10, image=bgImg)
btn3=Button(width=20, height=10, image=bgImg)
btn4=Button(width=20, height=10, image=bgImg)
btn5=Button(width=20, height=10, image=bgImg)
btn6=Button(width=20, height=10, image=bgImg)
btn7=Button(width=20, height=10, image=bgImg)
btn8=Button(width=20, height=10, image=bgImg)
btn9=Button(width=20, height=10, image=bgImg)
btn10=Button(width=20, height=10, image=bgImg)
btn11=Button(width=20, height=10, image=bgImg)

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=0, column=4)
btn5.grid(row=0, column=5)
btn6.grid(row=1, column=0)
btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)
btn10.grid(row=1, column=4)
btn11.grid(row=1, column=5)

myImg1=Image.Tk.PhotoImage(Image.open("1.jpg"))
myImg2=Image.Tk.PhotoImage(Image.open("2.jpg"))
myImg3=Image.Tk.PhotoImage(Image.open("3.jpg"))
myImg4=Image.Tk.PhotoImage(Image.open("4.jpg"))
myImg5=Image.Tk.PhotoImage(Image.open("5.jpg"))
myImg6=Image.Tk.PhotoImage(Image.open("6.jpg"))

bgImg=ImageTk.PhotoImage(Image.open("00"))

gameWindow.mainloop()