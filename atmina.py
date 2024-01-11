from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gameWindow=Tk()
gameWindow.title("vienādie attēli")

bgImg=ImageTk.PhotoImage(Image.open("00.png"))
#Button(bg="black")

#myImg1=ImageTk.PhotoImage(Image.open("1.png").resize((200,300)))
#myImg2=ImageTk.PhotoImage(Image.open("2.png").resize((200,300)))
#myImg3=ImageTk.PhotoImage(Image.open("3.png").resize((200,300)))
#myImg4=ImageTk.PhotoImage(Image.open("4.png").resize((200,300)))
#myImg5=ImageTk.PhotoImage(Image.open("5.png").resize((200,300)))
#myImg6=ImageTk.PhotoImage(Image.open("6.png").resize((200,300)))

count=0
correctAns=0
answers=[]
answer_dict={} #kas pies[iests salidzina ar atnildem nosaraksta]


def btnClick(btn,number):
    global count, correctAns, answers,answer_dict
    if btn["image"]=="pyimage1"and count<2:
        btn["image"]=imageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=imageList[number]
    if len(answers)==2:
        if imageList[answers[0]]==imageList[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
            correctAns+=2
            if correctAns==2:
                messagebox.showinfo("uzmineji", "uzmineji")
                correctAns=0
        else:
            messagebox.showinfo("neuzmineji","neuzmineji")
            for key in answer_dict:
                key["image"]="pyimage1"
        count=0
        answers=[]
        answer_dict={}
    return 0

if correctAns==6:
    messagebox.showinfo("tu uzvareji")

def reset():
    global count, correctAns, answers,answer_dict

    btn0.config(state=NORMAL)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn10.config(state=NORMAL)
    btn11.config(state=NORMAL)

    btn0["image"]="pyimage1"
    btn1["image"]="pyimage1"
    btn2["image"]="pyimage1"
    btn3["image"]="pyimage1"
    btn4["image"]="pyimage1"
    btn5["image"]="pyimage1"
    btn6["image"]="pyimage1"
    btn7["image"]="pyimage1"
    btn8["image"]="pyimage1"
    btn9["image"]="pyimage1"
    btn10["image"]="pyimage1"
    btn11["image"]="pyimage1"
    random.shuffle(imageList)
    return 0

btn0=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn0,0))
btn1=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn9,9))
btn10=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn10,10))
btn11=Button(width=200, height=300, image=bgImg, command=lambda:btnClick(btn11,11))

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

myImg1=ImageTk.PhotoImage(Image.open("1.png").resize((200,300)))
myImg2=ImageTk.PhotoImage(Image.open("2.png").resize((200,300)))
myImg3=ImageTk.PhotoImage(Image.open("3.png").resize((200,300)))
myImg4=ImageTk.PhotoImage(Image.open("4.png").resize((200,300)))
myImg5=ImageTk.PhotoImage(Image.open("5.png").resize((200,300)))
myImg6=ImageTk.PhotoImage(Image.open("6.png").resize((200,300)))

imageList=[myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,
           myImg4,myImg4,myImg5,myImg5,myImg6,myImg6]

random.shuffle(imageList)


galvenaizvelne=Menu(gameWindow)
gameWindow.config(menu=galvenaizvelne)

opcijas=(Menu)(galvenaizvelne, tearoff=False)
galvenaizvelne.add_cascade(label="Opcijas", menu=opcijas)

opcijas.add_command(label="jauna spēle", command=reset)
opcijas.add_cascade(label="iziet", command=gameWindow.quit)

galvenaizvelne.add_command(label="Par programmu")





gameWindow.mainloop()