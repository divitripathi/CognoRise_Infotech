from tkinter import *
import tkinter as tk
import random

window=tk.Tk()
window.geometry("800x600")
window.title("Rock Paper Scissor Game")
window.config(bg="#B2BEC3")

computer_options = {
   "0":"Rock",
    "1":"Paper",
   "2":"Scissor"
}

def button_disable():
   b1.config(state= "disabled")
   b2.config(state= "disabled")
   b3.config(state= "disabled")

def isrock():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "Wohoo! You Won✌️"
   else:
      match_result = "Computer Win"
   label.config(text = match_result)
   l_r1.config(text = "Rock")
   l_r3.config(text =value)
   button_disable()

def ispaper():
   value = computer_options[str(random.randint(0, 2))]
   if value == "Paper":
      match_result = "Match Draw"
   elif value=="Scissor":
      match_result = "Computer Win"
   else:
      match_result = "Amazingg..You won💥💥"
   label.config(text = match_result)
   l_r1.config(text = "Paper")
   l_r3.config(text = value)
   button_disable()


def isscissor():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Computer Win"
   elif value == "Scissor":
      match_result = "Match Draw"
   else:
      match_result = "🎉🎉You Win🎉🎉"
   label.config(text = match_result)
   l_r1.config(text = "Scissor")
   l_r3.config(text = value)
   button_disable()


def reset():
   b1.config(state= "active")
   b2.config(state= "active")
   b3.config(state= "active")
   l_r1.config(text = "")
   l_r3.config(text = "")
   label.config(text = "")


head=Label(window, text="Rock Paper Scissor Game", font=('Papyrus 30 bold'), bg="#B2BEC3", fg="#680000")
head.pack(pady="10 20")

l1= Label(window, text="Player", font= ('Helvetica 28 bold underline'), bg="#B2BEC3")
l1.place(relx= .18, rely= .2)

l_r1= Label(window, text="", font= ('Helvetica 18 bold'), fg='white', bg="#B2BEC3")
l_r1.place(relx=.18, rely= .3)

l2= Label(window, text="v/s", font= ('Algerian 40'), bg="#B2BEC3", fg='black')
l2.place(relx= .45, rely= .17)

l3= Label(window, text="Computer", font= ('Helvetica 28 bold underline'), bg="#B2BEC3")
l3.place(relx= .65, rely= .2)

l_r3= Label(window, text="", font= ('Helvetica 18 bold'), fg='white', bg="#B2BEC3")
l_r3.place(relx= .65, rely= .3)

label= Label(window, text="", font=('Coveat', 25,'bold'), bg= "#B2BEC3", fg='#800080')
label.pack(pady=200)

b1= Button(window, text= "Rock", font= 10, width= 7, command= isrock)
b1.place(relx=.2, rely= .8)
b2= Button(window, text= "Paper", font= 10, width= 7 ,command= ispaper)
b2.place(relx= .36,rely= .8)
b3= Button(window, text= "Scissor", font= 10, width= 7, command= isscissor)
b3.place(relx= .53, rely= .8)

reset= Button(window, text= "Reset",bg= "red", fg= "white",width= 10, font= 25, command= reset)
reset.place(relx= .75, rely= .8)
window.mainloop()





























