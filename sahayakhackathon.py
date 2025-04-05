import tkinter as tk 
from tkinter import messagebox, simpledialog
from datetime import datetime, date
import random
from gtts import gTTS
import pygame
import os
from PIL import Image, ImageTk 

tablet_data = {}
last_check_in_time = None
user_data = {
    "last_quote_date": "",
    "shown_quotes": [],
    "checked_in": False
}

language_options = {
    "English": "en",
    "Tamil - தமிழ்": "ta",
    "Hindi - हिंदी": "hi",
    "Kannada - ಕನ್ನಡ": "kn",
    "Telugu - తెలుగు": "te"
}
selected_language = "en"

pygame.mixer.init()

daily_quotes = [
    "Every day is a second chance.",
    "The best time for new beginnings is now.",
    "You are never too old to set another goal or to dream a new dream.",
    "Happiness is not by chance, but by choice.",
    "Keep smiling, because life is a beautiful thing!"
]

translations = {
    "en": {
        "check_in": "Check In",
        "daily_quote": "Daily Quote",
        "view_festivals": "View Festivals",
        "medicine_reminder": "Medicine Reminder",
        "speak_menu": "Speak Menu"
    },
    "ta": {
        "check_in": "சரிபார்க்கவும்",
        "daily_quote": "இன்றைய மீற்கோள்",
        "view_festivals": "திருவிழாக்கள்",
        "medicine_reminder": "மருந்து நினைவூட்டல்",
        "speak_menu": "பட்டியலை பேசு"
    },
    "hi": {
        "check_in": "चेक इन करें",
        "daily_quote": "आज का उद्धरण",
        "view_festivals": "त्योहार देखें",
        "medicine_reminder": "दवा अनुस्मारक",
        "speak_menu": "मेनू बोलें"
    },
    "kn": {
        "check_in": "ಚೆಕ್ ಇನ್",
        "daily_quote": "ಇಂದಿನ ಉಲ್ಲೇಖ",
        "view_festivals": "ಹಬ್ಬಗಳ್ನ್ನು ನೋಡಿ",
        "medicine_reminder": "ಔಷಧಿ ಜ಼್್ಞಾಪನೆ",
        "speak_menu": "ಮೆನು ಉಚ್ಚರಿಸಿ"
    },
    "te": {
        "check_in": "చెక్ ఇన్",
        "daily_quote": "ఈరోజు కోట్",
        "view_festivals": "పండుగలు చూడండి",
        "medicine_reminder": "మందు గుర్తు",
        "speak_menu": "మెనూను చప్పండి"
    }
}

def speak_menu_options():
    options = [
        translations[selected_language]["check_in"],
        translations[selected_language]["daily_quote"],
        translations[selected_language]["view_festivals"],
        translations[selected_language]["medicine_reminder"]
    ]
    text = ", ".join(options)
    tts = gTTS(text=text, lang=selected_language, slow=False)
    temp_path = "menu.mp3"
    tts.save(temp_path)
    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

def show_daily_quote_gui():
    today = str(date.today())
    if user_data["last_quote_date"] == today:
        return
    available = list(set(daily_quotes) - set(user_data["shown_quotes"]))
    if not available:
        user_data["shown_quotes"] = []
        available = daily_quotes.copy()
    quote = random.choice(available)
    user_data["shown_quotes"].append(quote)
    user_data["last_quote_date"] = today
    messagebox.showinfo("Quote of the Day", quote)

def view_festivals_gui():
    general_festivals = [
        {"name": "Diwali", "date": "2025-10-20"},
        {"name": "Holi", "date": "2025-03-14"},
        {"name": "Christmas", "date": "2025-12-25"},
        {"name": "Easter", "date": "2025-04-20"},
        {"name": "Eid al-Fitr", "date": "2025-03-31"},
        {"name": "Eid al-Adha", "date": "2025-06-06"}
    ]
    today = date.today()
    upcoming = [(f["name"], f["date"]) for f in general_festivals if datetime.strptime(f["date"], "%Y-%m-%d").date() >= today]
    if upcoming:
        msg = "upcoming Festivals:\n\n" + "\n".join([f"- {name} on {date}" for name, date in sorted(upcoming)])
        messagebox.showinfo("Festivals", msg)
    else:
        messagebox.showinfo("Festivals", "No upcoming festivals found.")

def medicine_reminder():
    if not tablet_data:
        return
    response = messagebox.askyesno("Medicine Reminder", "Have you taken your medicines today?")
    if response:
        for med in tablet_data:
            if tablet_data[med]["remaining"] > 0:
                tablet_data[med]["remaining"] -= 1

def check_time_for_medicine():
    now = datetime.now()
    if now.hour == 12 and now.minute == 0:
        medicine_reminder()
    root.after(60000, check_time_for_medicine)  

def open_senior_side():
    global selected_language
    show_daily_quote_gui() 
    senior_window = tk.Toplevel(root)
    senior_window.title("Senior Citizen Side")
    senior_window.state('zoomed')  
    
    image_path = r"C:\Users\91827\Downloads\background screen.jpeg"  
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((senior_window.winfo_screenwidth(), senior_window.winfo_screenheight()), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(senior_window, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(senior_window, text="Hello 👵👱", font=("Ubuntu",80)).pack(pady=10)
    lang_var = tk.StringVar(value="English")

    def update_menu_texts():
        t = translations[selected_language]
        btn_check_in.config(text=t["check_in"])
        btn_daily_quote.config(text=t["daily_quote"])
        btn_view_festivals.config(text=t["view_festivals"])
        btn_medicine.config(text=t["medicine_reminder"])
        btn_speak.config(text=t["speak_menu"])

    def update_language_dropdown(choice):
        global selected_language
        selected_language = language_options.get(choice, "en")
        update_menu_texts()

    tk.Label(senior_window, text="Select Language:", font=("Arial", 30)).pack(pady=20)
    tk.OptionMenu(senior_window, lang_var, *language_options.keys(), command=update_language_dropdown).pack(pady=5)

    def check_in_action():
        global last_check_in_time
        last_check_in_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_data["checked_in"] = True
        messagebox.showinfo("Check In", f"Checked in at {last_check_in_time}")

    btn_check_in = tk.Button(senior_window, command=check_in_action)
    btn_daily_quote = tk.Button(senior_window, command=show_daily_quote_gui)
    btn_view_festivals = tk.Button(senior_window, command=view_festivals_gui)
    btn_medicine = tk.Button(senior_window, command=medicine_reminder)
    btn_speak = tk.Button(senior_window, command=speak_menu_options, bg="white")

    btn_check_in.pack(pady=5)
    btn_daily_quote.pack(pady=5)
    btn_view_festivals.pack(pady=5)
    btn_medicine.pack(pady=5)
    btn_speak.pack(pady=10)

    update_menu_texts()

def open_guardian_side():
  guardian_window = tk.Toplevel(root)
  guardian_window.title("Guardian Side")
  guardian_window.state('zoomed')

  image_path = r"C:\Users\91827\Downloads\background screen.jpeg"  
  bg_image = Image.open(image_path)
  bg_image = bg_image.resize((guardian_window.winfo_screenwidth(), guardian_window.winfo_screenheight()), Image.LANCZOS)
  bg_photo = ImageTk.PhotoImage(bg_image)

  bg_label = tk.Label(guardian_window, image=bg_photo)
  bg_label.image = bg_photo 
  bg_label.place(x=0, y=0, relwidth=1, relheight=1)
  tk.Label(guardian_window, text="Guardian Dashboard", font=("Arial", 14)).pack(pady=10)
  
  def view_check_in_status():
        if user_data.get("checked_in"):
            messagebox.showinfo("Check-In", f"Parent has checked in.\nLast check-in: {last_check_in_time}")
        else:
            messagebox.showinfo("Check-In", "Senior has not checked in today.")
  def add_tablet_entry():
        name = simpledialog.askstring("Tablet Name", "Enter tablet name:")
        if not name:
            return
        try:
            total = int(simpledialog.askstring("Total Tablets", f"Total count for {name}:"))
            dosage = int(simpledialog.askstring("Dosage", f"Dosage per day for {name}:"))
        except:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
            return
        tablet_data[name] = {"total": total, "remaining": total, "dosage_per_day": dosage}
        messagebox.showinfo("Saved", f"{name} added with {total} tablets.")

  def mark_tablet_taken():
        meds = list(tablet_data.keys())
        if not meds:
            messagebox.showinfo("No Tablets", "No medication data found.")
            return
        selected = simpledialog.askstring("Mark Tablet", f"Which tablet was taken?\nAvailable: {', '.join(meds)}")
        if selected in tablet_data:
            if tablet_data[selected]["remaining"] > 0:
                tablet_data[selected]["remaining"] -= 1
                messagebox.showinfo("Updated", f"{selected} marked as taken.\n{tablet_data[selected]['remaining']} remaining.")
            else:
                messagebox.showwarning("Out of Stock", f"{selected} is already out of stock.")
        else:
            messagebox.showerror("Not Found", f"{selected} not found.")

  def refresh_tablet_stock():
        meds = list(tablet_data.keys())
        if not meds:
            messagebox.showinfo("No Tablets", "No medication data to refresh.")
            return
        selected = simpledialog.askstring("Refresh Stock", f"Which tablet stock is refreshed?\nAvailable: {', '.join(meds)}")
        if selected in tablet_data:
            try:
                new_total = int(simpledialog.askstring("New Total", f"Enter new total for {selected}:"))
                tablet_data[selected]["total"] = new_total
                tablet_data[selected]["remaining"] = new_total
                messagebox.showinfo("Refreshed", f"{selected} stock reset to {new_total}.")
            except:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")
        else:
            messagebox.showerror("Not Found", f"{selected} not found.")

  tk.Button(guardian_window, text="View Last Check-In", command=view_check_in_status).pack(pady=5)
  tk.Label(guardian_window, text="Tablet Tracker", font=("Arial", 12)).pack(pady=10)
  tk.Button(guardian_window, text="Add New Tablet", command=add_tablet_entry).pack(pady=3)
  tk.Button(guardian_window, text="Mark Tablet Taken", command=mark_tablet_taken).pack(pady=3)
  tk.Button(guardian_window, text="View Tablet Status", command=lambda: messagebox.showinfo("Tablet Status", str(tablet_data))).pack(pady=3)
  tk.Button(guardian_window, text="Refresh Tablet Stock", command=refresh_tablet_stock).pack(pady=3)
  
root = tk.Tk()
root.title("Sahayak")
root.geometry("1500x700")
image_path = r"C:\Users\91827\Downloads\background screen.jpeg" 
bg_image = Image.open(image_path)
bg_image = bg_image.resize((1500, 700), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label =tk.Label(root, image=bg_photo)
bg_label.image = bg_photo 
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(root, text="Welcome to sahayak",font=("Times New Roman", 35)).pack(pady=20)
tk.Label(root, text="Pick Your Role",font=("Times New Roman", 24)).pack(pady=20)
tk.Button(root, text="I'm a Senior Citizen", command=open_senior_side, width=20, height=2).place(x=280, y=400)
tk.Button(root, text="I'm a Guardian", command=open_guardian_side, width=20, height=2).place(x=800, y=400)


check_time_for_medicine()
root.mainloop()
