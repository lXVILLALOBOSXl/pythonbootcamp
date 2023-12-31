from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)

    password = ""
    i = 0
    word_len = 10

    while i < word_len:

        ran = random.randint(0, 2)

        if ran == 0:
            password += random.choice(letters)
        elif ran == 1:
            password += random.choice(numbers)
        elif ran == 2:
            password += random.choice(symbols)

        i += 1

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    if len(password) < 1 or len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} '
                                                          f'\nPassword: {password} \nIs it ok to save?')

    if is_ok:
        with open("data.txt", mode="a") as file:
            file.write(f'{website} | {email} | {password}\n')

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.insert(0, "person@email.com")
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "person@email.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", highlightthickness=0, width=36, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
