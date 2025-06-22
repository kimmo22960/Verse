import tkinter as tk
from tkinter import *
import requests
import textwrap
import os
from threading import Thread
from time import sleep

def update():
    global frame1, my_message

    if not window.winfo_exists():  # Check if the window is closed before updating
        return

    response = requests.get('https://bible-api.com/data/web/random/NT')
    data = response.json()
    book = data["random_verse"]["book"]
    chapter = data["random_verse"]["chapter"]
    verse = data["random_verse"]["verse"]
    longText = data["random_verse"]["text"]

    window.title(f"Verse of the Day - {book} {chapter}:{verse}")
    window.after(400000, update)  # Schedule the next update.

    frame1.pack_forget()  # Remove the old frame
    frame1 = LabelFrame(window, text=f"Verse from {book} {chapter}:{verse}",
                        font=("freesans", 12),
                        background=("#C2C2C2"))
    frame1.pack(pady=20)

    my_message.pack_forget()  # Remove the old message
    my_message = Message(frame1, text=f"{longText}",
                        font=("freesans", 18),
                        aspect=200,
                        justify=tk.CENTER,
                        background=("#7D7D7D"))
    my_message.pack(pady=10, padx=10)

window = tk.Tk()
window.configure(background="#C2C2C2")
window.minsize(300, 200)
window.maxsize(800, 600)
window.geometry("440x240+10+20")

frame1 = LabelFrame(window, text="Verse from Book Chapter:Verse",
                    font=("freesans", 12),
                    background=("#C2C2C2"))
frame1.pack(pady=20)

my_message = Message(frame1, text="",
                    font=("freesans", 18),
                    aspect=200,
                    justify=tk.CENTER,
                    background=("#7D7D7D"))
my_message.pack(pady=10, padx=10)

Thread(target=update).start()
window.mainloop()
