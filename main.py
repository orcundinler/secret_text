from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pybase64
from tkinter import messagebox

path_image = "image.png"

screen = Tk()
screen.title("Top Secret")
screen.wm_minsize(550, 650)
game = True
save_password = []


def encrypt():
    secret = secret_text.get(1.0, END)
    secret_text.delete(1.0, END)

    if masterkey_entry.get() == f"{masterkey_entry.get()}":
        secret = secret.encode("ascii")
        secret = pybase64.b64encode(secret)
        secret = secret.decode("ascii")
        secret_text.insert(END, secret)
    else:
        pass


def get_password():
    global game
    user_input = masterkey_entry.get()
    value = user_input
    if game is True:
        save_password.append(value)
        game = False
    else:
        pass


def decrypt():
    secret = secret_text.get(1.0, END)
    secret_text.delete(1.0, END)
    try:
        if masterkey_entry.get() == f"{save_password[0]}":
            secret = secret.encode("ascii")
            secret = pybase64.b64decode(secret)
            secret = secret.decode("ascii")
            secret_text.insert(END, secret)
    except IndexError:
        messagebox.showwarning("Error!", "Master Key can not be empty. Try again.")


def delete_text():
    secret_text.delete(1.0, END)
    masterkey_entry.delete(0, END)
    title_entry.delete(0, END)


def save_as_text_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file_content = secret_text.get('1.0', END) + title_entry.get()
                file.write(file_content)
                status_label.config(text=f"File saved to: {file_path}")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")


def check_characters():
    while True:
        if int(len(title_entry.get())) <= 0:
            messagebox.showwarning("Error!", "Put atleast 1 character in Title.")
            break
        else:
            encrypt(), get_password(), save_as_text_file(), delete_text()
            break


img = ImageTk.PhotoImage(Image.open(path_image))
topsecretimage = Label(screen, image=img)
topsecretimage.pack()

title_label = Label(font=("Arial", 15, "bold"), text="Enter Your Title")
title_label.pack()

title_entry = Entry(width=50)
title_entry.focus()
title_entry.pack()

secret_label = Label(font=("Arial", 15, "bold"), text="Enter Your Secret")
secret_label.pack()

secret_text = Text(width=50, height=20)
secret_text.pack()

masterkey_label = Label(font=("Arial", 15, "bold"), text="Enter Master Key")
masterkey_label.pack()

masterkey_entry = Entry(width=50)
masterkey_entry.pack()

save_button = Button(text="Save & Encrypt", font=("Arial", 15, "normal"), command=check_characters)
save_button.pack(pady=10)

decrypt_button = Button(text="Decrypt the text.", font=("Arial", 10, "bold"), command=decrypt)
decrypt_button.config(pady=10, padx=10)
decrypt_button.pack(pady=10)

status_label = Label(screen, text="", padx=20, pady=10)
status_label.pack()

mainloop()
