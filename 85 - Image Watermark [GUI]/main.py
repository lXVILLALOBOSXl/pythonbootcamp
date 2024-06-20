from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os
import platform
import tkinter.ttk as ttk
import pandas
import random

username = os.environ.get('USER')
operating_system = platform.system()



def upload_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    txt_image_path.config(text=filename)

def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def generate_image():
    path = txt_image_path.cget("text")
    if path == "No Image Selected":
        return
    
    file_name = path.split("/")[-1]
    file_name = file_name.split(".")[0]

    text = txt_watermark.get()
    if text == "":
        return
    
    image = Image.open(path)

    watermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(watermark)
    font_size = 100 
    if operating_system == "Windows":
        font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", font_size)
    else:
        font = ImageFont.truetype("Keyboard.ttf", font_size)

    text_width, text_height = get_text_dimensions(text, font)

    text_x = (image.width - text_width) / 2
    text_y = (image.height - text_height) / 2

    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255, 128)) 


    watermarked = Image.alpha_composite(image.convert('RGBA'), watermark)

    watermarked = watermarked.convert('RGB')

    #save in downloads
    if operating_system == "Windows":
        watermarked.save(f"C:/Users/{username}/Downloads/{file_name}-WM.jpg")
    else:
        watermarked.save(f"/Users/{username}/Downloads/{file_name}-WM.jpg")




window = Tk()
window.title("WaterMark App")
window.geometry('400x200')
window.config(padx=20, pady=20)
style = ttk.Style()
style.configure("TButton", padding=1, relief="flat", background="#ccc")
style.configure("TEntry", padding=1, relief="flat", background="#ccc")
style.configure("TLabel", padding=1, relief="flat", background="#ccc")

# Make the app responsive
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

# Upload Image Button
btn_upload = ttk.Button(style="TButton", text="Upload Image", command=upload_image)
btn_upload.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Image Path
txt_image_path = ttk.Label(style="TLabel", text="No Image Selected")
txt_image_path.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Watermark Text
txt_watermark = ttk.Entry(style="TEntry")
txt_watermark.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Generate Button
btn_ok = ttk.Button(style="TButton",text="Generate", command=generate_image)
btn_ok.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


window.mainloop()


