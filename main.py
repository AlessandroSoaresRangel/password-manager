from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
from json.decoder import JSONDecodeError

# PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# SAVE PASSWORD


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email/username": username,
        "password": password
    }}

    if not website or not username or not password:
        messagebox.showinfo(title="Erro", message="Não pode haver campos vazios")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError or JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# UI SETUP
window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

username_label = Label(text="Email/Nome de usuario:")
username_label.grid(column=0, row=2)

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Senha:")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Gerar Senha", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Adicionar", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
