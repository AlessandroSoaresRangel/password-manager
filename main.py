from tkinter import *
# PASSWORD GENERATOR

# SAVE PASSWORD

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

username_label = Label(text="Email/Nome de usuario:")
username_label.grid(column=0, row=2)

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Senha:")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Gerar Senha")
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Adicionar")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
