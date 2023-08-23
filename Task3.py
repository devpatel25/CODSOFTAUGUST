# Task 3- Password Generator

import tkinter as tk
import random

# function to generate password
def generate_password(length):
    characters=("qwertyuiopasdfghjklzxcvbnm"
        "QWERTYUIOPASDFGHJKLZXCVBNM"
        "!@#$%^&*()_+=\:;,.?/<>")
    password= ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password():
    try:
        pass_length = int(len_entry.get())
        if pass_length<=0:
            pass_lbl.config(text="Invalid Length! It must be greater than 0.",foreground="red")
        else:
            password=generate_password(pass_length)
            pass_lbl.config(text=password,background="white",foreground="black",font=("arial",20,"bold"),width=20)
    except ValueError:
        pass_lbl.config(text="Value Error!", foreground="red")

# Main
root= tk.Tk()
root.geometry("300x200")
root.title("Password Generator")
len_label=tk.Label(root,text="Enter the length of the password: ",font=("arial",15))
len_label.pack()
len_entry=tk.Entry(root,font=("arial",15))
len_entry.pack()
btn=tk.Button(root,text="Generate Password", command=display_password)
btn.pack()
pass_lbl=tk.Label(root,text="")
pass_lbl.pack()
root.mainloop()

