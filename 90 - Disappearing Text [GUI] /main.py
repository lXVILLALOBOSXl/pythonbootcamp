from tkinter import *
import tkinter.ttk as ttk

job = None

def count_down():
    global timer, job
    lbl_timer.config(text=f"Timer: {timer}")
    if timer > 0:
        timer -= 1
        window.after_cancel(job)  
        job = window.after(1000, count_down)  
    else:
        txt_input.delete('1.0', 'end')
        lbl_timer.config(text="")

def reset_timer():
    global timer, job
    timer = 5  
    if job:
        window.after_cancel(job)  
    job = window.after(0, count_down)  

def on_key_press(event):
    key = event.char
    if key.isalnum() or key in [",", ".", "!", "?", ";", ":", "-", "_", "+", "=", "*", "/", "&", "%", "$", "#", "@", "^", "(", ")", "[", "]", "{", "}", "<", ">", "|", "\\", "`", "~"]:
        reset_timer()


window = Tk()
window.title("Disappearing Text")
window.geometry('600x600')
window.config(padx=10, pady=10)

txt_input = Text(window, height=30, width=30, padx=10, pady=20, relief="flat", bg="#000", wrap="word")
txt_input.grid(row=1, column=0, padx=10, pady=1, sticky="nsew")
txt_input.bind("<Key>", on_key_press)

lbl_timer = Label(window)
lbl_timer.grid(row=0, column=0, padx=10, pady=20, sticky="nw")

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()


