import tkinter as tk 
from tkinter import messagebox 
root= tk.Tk()
root.title("senior buddy app")
root.geometry("300x200")

def open_senior_page():
    senior_window = tk.Toplevel(root)
    senior_window.title("senior citizen")
    senior_window.geometry("300x200")
    tk.Label(senior_window, text="hello 👵👴", font=("Arial",14)).pack(pady=10)
    tk.Button(senior_window, text="check in",  command=lambda:messagebox.showinfo("check in","checked in successfully!")).pack(pady=5)
def open_guardian_page():
    guardian_window= tk.Toplevel(root)
    guardian_window.title("guardian")
    guardian_window.geometry("300x200")
    tk.Label(guardian_window, text="Guardian dashboard", font=("Arial",14)).pack(pady=10)
    tk.Button(guardian_window, text="View Check-In Status",  command=lambda:messagebox.showinfo("Status","senior checked-In today")).pack(pady=5)
tk.Label(root, text="Choose your side", font=("Arial",14)).pack(pady=10)
tk.Button(root, text="I'm a Senior Citizen", command=open_senior_page,width=25).pack(pady=5)
tk.Button(root, text="I'm a Guardian", command=open_guardian_page,width=25).pack(pady=5)
root.mainloop()     
