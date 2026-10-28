
import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x650")

fields = ["First Name", "Middle Name", "Last Name",
          "Mobile Number", "Gmail"]

entries = []

for field in fields:
    tk.Label(root, text=field).pack()
    e = tk.Entry(root)
    e.pack()
    entries.append(e)

tk.Label(root, text="State").pack()
state = tk.StringVar(value="Maharashtra")
tk.OptionMenu(root, state, "Maharashtra", "Karnataka",
              "Goa").pack()

tk.Label(root, text="District").pack()
district = tk.StringVar(value="Solapur")
tk.OptionMenu(root, district, "solapur","Kolhapur", "Pune",
              "Sangli",).pack()

tk.Label(root, text="Tahasil").pack()
tahasil = tk.StringVar(value="Akluj")
tk.OptionMenu(root, tahasil,"Akluj","Karveer", "Panhala",
              "Haveli").pack()

tk.Label(root, text="Address").pack()
address = tk.Entry(root)
address.pack()

def submit():
    f, m, l, mob, mail = [e.get().strip() for e in entries]
    addr = address.get().strip()

    if not f or not m or not l:
        messagebox.showerror("Error", "Enter all names")

    elif not re.fullmatch(r"[6-9][0-9]{9}", mob):
        messagebox.showerror("Error", "Enter valid 10-digit mobile number")

    elif not re.fullmatch(r"[A-Za-z0-9._%+-]+@gmail\.com", mail):
        messagebox.showerror("Error", "Enter valid Gmail address")

    elif len(addr) < 5:
        messagebox.showerror("Error", "Address must have at least 5 characters")

    else:
        messagebox.showinfo("Success", "Registration Successful!")

tk.Button(root, text="Submit", command=submit).pack(pady=15)

root.mainloop()
