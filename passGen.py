import random, string
import pyperclip
from tkinter import *
import tkinter as tk

window=tk.Tk()
window.geometry("500x400")
window.title("Password Generator")

output_pass=StringVar()
all_combi=[string.punctuation,string.ascii_lowercase, string.ascii_uppercase,string.digits]

def randPassGen():
    password=""
    for y in range(Pass_len.get()):
        char_type=random.choice(all_combi)
        password=password+random.choice(char_type)
    output_pass.set(password)

def copyPass():
    pyperclip.copy(output_pass.get())

head=Label(window, text="Password Generator", font=('Algerian', 20, 'underline'), foreground="darkblue")
head.pack(pady="0 20")

Pass_head=Label(window, text="Password length")
Pass_head.pack(pady=10)

Pass_len=IntVar()
length=Spinbox(window, from_=8, to_=32, textvariable=Pass_len, width=10, font=3)
length.pack(pady=10)

Button(window, text="GENERATE PASSWORD", command= randPassGen, bg='lavender', fg='darkblue', padx=5, pady=5,font='Arial 10').pack(pady=20)

Pass_label=Label(window, text='Random Generated Password')
Pass_label.pack(pady="30 10")
Entry(window, textvariable= output_pass, width=20, font=5).pack()

Button(window, text='copy to clioboard', command=copyPass, bg='lightgrey',fg='black', padx=5, pady=5).pack(pady=20)

window.mainloop()