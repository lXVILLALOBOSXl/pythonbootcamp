from tkinter import *
import requests

quote = "" 
def get_quote():
    try:
        response = requests.get(url="https://api.kanye.rest")
        response.raise_for_status()
        data = response.json()
    except:
        print(f"Error has occured")
    else:
        quote = data["quote"]
        canvas.itemconfig(quote_text, text=quote)
    

    



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="/Users/luisvillalobos/Documents/Programacion/Self Study/Udemy/Python Bootcamp/33 - API Endpoints & API Parameters - ISS Overhead Notifier/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=f"{quote}", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="/Users/luisvillalobos/Documents/Programacion/Self Study/Udemy/Python Bootcamp/33 - API Endpoints & API Parameters - ISS Overhead Notifier/kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()