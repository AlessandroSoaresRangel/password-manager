from tkinter import *
from tkinter import messagebox
# PASSWORD GENERATOR

# SAVE PASSWORD


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showinfo(title="Erro", message="Não pode haver campos vazios")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Esses são os dados detalhados: \n"
                                                              f"Email: {username} \n"
                                                              f"Password: {password}\n"
                                                              f"salvar?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"site: {website} | email/Nome de usuario: {username}"
                           f" | Senha: {password} \n")

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

generate_button = Button(text="Gerar Senha")
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Adicionar", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
