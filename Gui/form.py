
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x350")

tk.Label(root, text="Student Registration").pack()

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Roll No").pack()
roll = tk.Entry(root)
roll.pack()

tk.Label(root, text="Class").pack()
cls = tk.StringVar(value="FY")
tk.OptionMenu(root, cls, "FY", "SY", "TY").pack()

tk.Label(root, text="subject").pack()
sub = tk.StringVar(value="Python")
tk.OptionMenu(root,sub,"Python","Java","c++").pack()

def register():
    messagebox.showinfo(
        "Registration",
        "Name: " + name.get() +
        "\nRoll No: " + roll.get() +
        "\nClass: " + cls.get() +
        "\nSubject: " + sub.get()
    )

tk.Button(root, text="Register", command=register).pack(pady=15)

root.mainloop()
