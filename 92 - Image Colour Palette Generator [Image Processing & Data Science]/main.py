from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from sklearn.cluster import KMeans
import tkinter.ttk as ttk
import numpy as np
import threading



def get_file_name():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if filename:
        txt_image_path.config(text=filename)

def generate_palette_thread():
    threading.Thread(target=generate_palette).start()

def generate_palette():
    global btn_ok  # Asegúrate de tener acceso a btn_ok
    if filename:
        btn_ok.config(text="Generating...", state="disabled")
        window.update_idletasks()  # Actualiza la interfaz de usuario
        my_img = Image.open(filename)
        img_array = np.array(my_img)
        pixels = img_array.reshape(-1, 3)
        kmeans = KMeans(n_clusters=10)
        kmeans.fit(pixels)
        colors = kmeans.cluster_centers_
        colors = colors.round(0).astype(int)
        
        for color in colors:
            color_hex = rgb_to_hex(tuple(color))
            color_container_frame = Frame(color_container, width=100, height=20)
            color_container_frame.pack(pady=1)
            color_container_frame.pack_propagate(False)

            color_frame = Frame(color_container_frame, bg=color_hex, width=30, height=15)
            color_frame.pack(side='left', padx=1)
            color_frame.pack_propagate(False)

            color_label = Label(color_container_frame, text=color_hex)
            color_label.pack(side='right', padx=1)

        btn_ok.config(state='normal', text="Generate")
    
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


window = Tk()
window.title("Coulor Palette Generator")
window.geometry('450x600')
window.config(padx=10, pady=10)
style = ttk.Style()
style.configure("TButton", padding=1, relief="flat", background="#ccc")
style.configure("TLabel", padding=1, relief="flat", background="#ccc")

# Make the app responsive
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

# Upload Image Button
btn_upload = ttk.Button(style="TButton", text="Upload Image", command=get_file_name)
btn_upload.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")

# Image Path
txt_image_path = ttk.Label(style="TLabel", text="No Image Selected")
txt_image_path.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")

# Generate Button
btn_ok = ttk.Button(style="TButton",text="Generate", command=generate_palette_thread)
btn_ok.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")

# Color Container
color_container = ttk.Frame(window)
color_container.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")

color_container.grid_columnconfigure(0, weight=1)
color_container.grid_rowconfigure(0, weight=1)


window.mainloop()


