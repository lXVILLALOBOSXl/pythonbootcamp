from tkinter import *
from tkinter import filedialog, DISABLED
import tkinter.ttk as ttk
import time
import random

completed_words = []
words = []
word = ""
initialized = False

with open('best_score.txt', 'r') as file:
    first_line = file.readline()
    score = int(first_line)

def restart():
    global words, word, initialized, completed_words
    init()
    set_txt()
    initialized = False
    words = []
    word = ""
    completed_words = []
    txt_input.delete(0, END)
    lbl_timer.config(text=f"Timer: ")
    lbl_WPM.config(text=f"WPM: ")
    txt_input.config(state=NORMAL)


def set_txt():
    txt_words.config(state=NORMAL)
    txt_words.delete('1.0', END)
    txt_words.insert(INSERT, ' '.join(random_words))
    txt_words.config(state=DISABLED)

def delete_word():
    global completed_words
    completed_words.append(random_words.pop(0))
    set_txt()


def on_key_press(event):
    global word, words, initialized

    if not initialized:
        initialized = True
        lbl_best_score.config(text=f"Best Score: {score}")
        countdown(60)

    key = event.char
    if key == " ":
        if word != "":
            words.append(word)
            word = ""
            txt_input.delete(0, END)
            delete_word()
    elif key.isalpha():
        key = key.lower()
        word += key
    


def init():
    global random_words
    with open("random_words.txt", "r") as file:
        random_words = file.readlines()
    random_words = [word.strip() for word in random_words]
    random.shuffle(random_words)
    txt_words.config(state=NORMAL)
    txt_words.insert(INSERT, ' '.join(random_words))
    txt_words.config(state=DISABLED)

def calculate_score():
    global words, completed_words
    correct = 0
    for i in range(len(words)):
        if words[i] == completed_words[i]:
            correct += 1
    return correct
    
def countdown(time):
    if time > 0:
        lbl_timer.config(text=f"Timer: {time}")
        window.after(1000, countdown, time-1)
    else:
        lbl_timer.config(text=f"Timer: {time}")
        txt_input.config(state=DISABLED)
        wpm = calculate_score()
        lbl_WPM.config(text=f"WPM: {wpm}")
        if wpm > score:
            with open('best_score.txt', 'w') as file:
                file.write(str(wpm))
            lbl_best_score.config(text=f"Best Score: {wpm}")

window = Tk()
window.title("Typing Speed Test")
window.geometry('400x600')
window.config(padx=10, pady=10)
style = ttk.Style()
style.configure("TButton", padding=1, relief="flat", background="#ccc")
style.configure("TEntry", padding=1, relief="flat", background="#ccc")
style.configure("TLabel", padding=1, relief="flat", background="#ccc")

# Make the app responsive
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

# Best Score Label
lbl_best_score = ttk.Label(style="TLabel", text="Best Score: ")
lbl_best_score.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# WPM Label
lbl_WPM = ttk.Label(style="TLabel", text="WPM: ")
lbl_WPM.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Timer Label
lbl_timer = ttk.Label(style="TLabel", text="Timer: ")
lbl_timer.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Restart Button
btn_restart = ttk.Button(style="TButton", text="Restart", command=restart)
btn_restart.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Show words to type
txt_words = Text(window, height=10, width=30)
txt_words.config(state=DISABLED)
txt_words.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Textbox for typing
txt_input = ttk.Entry(style="TEntry")
txt_input.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
txt_input.bind("<Key>", on_key_press)


init()


window.mainloop()


