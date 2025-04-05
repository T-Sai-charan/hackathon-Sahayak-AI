import requests
import tkinter as tk
from tkinter import messagebox

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        ip = data.get("ip", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country", "N/A")
        loc = data.get("loc", "N/A")
        org = data.get("org", "N/A")
        timezone = data.get("timezone", "N/A")

        result = f"""
IP: {ip}
City: {city}
Region: {region}
Country: {country}
Coordinates: {loc}
Organization: {org}
"""
        output_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch location:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Auto Location Detector")
root.geometry("1000x1000")
root.config(padx=20, pady=20)

title_label = tk.Label(root, text="Click to Detect Your Location", font=("Arial", 14))
title_label.pack(pady=100)

detect_button = tk.Button(root, text="Detect Location", command=get_location, font=("Arial", 12))
detect_button.pack(pady=100)

output_label = tk.Label(root, text="", justify="left", font=("Courier", 10))
output_label.pack(pady=10)

root.mainloop()
