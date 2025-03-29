"""
Single Password Generator / Einzel-Passwort-Generator - GUI Tool for Secure Passwords

Description/Beschreibung:
Generate and copy individual passwords with customizable complexity.
Erstellt und kopiert individuelle Passwörter mit anpassbarer Komplexität.

Features/Funktionen:
- Copy-to-clipboard functionality / Kopieren in Zwischenablage
- Custom character sets / Eigene Zeichensets
- Lightweight Tkinter interface / Leichte Tkinter-Oberfläche

Keywords/Schlüsselwörter:
python password generator, secure passwords / Python Passwortgenerator, Sichere Passwörter
"""

from tkinter import *
from tkinter import messagebox, filedialog
import random
import string

overall_font = "Righteous"
overall_font_size = "14"
overall_background_button = "#00008B"

passgenerator = Tk()
passgenerator.title("Password Generator")
passgenerator.config(width=600, height=400)  # Adjusted width for the frame and other content


# Create another frame for the password generator interface
frame_02 = Frame(passgenerator, width=400, height=200)
frame_02.grid(row=0, column=1)

def generate_password():
    length = int(length_entry.get())
    use_numbers = password_numbers_var.get()
    use_special_chars = special_chars_var.get()
    special_chars_list = special_chars_entry.get()

    if use_special_chars:
        char_pool = string.ascii_letters
        if use_numbers:
            char_pool += string.digits
        char_pool += special_chars_list
    else:
        char_pool = string.ascii_letters + string.digits if use_numbers else string.ascii_letters

    generated_password = ''.join(random.choice(char_pool) for _ in range(length))
    created_pass.delete(0, END)
    created_pass.insert(0, generated_password)

def copy_password():
    generated_password = created_pass.get()

    if not generated_password:
        generate_password()

    passgenerator.clipboard_clear()
    passgenerator.clipboard_append(generated_password)
    passgenerator.update()

    messagebox.showinfo("Password Copied", "Password copied to clipboard!")
    passgenerator.after(2000, lambda: passgenerator.update_idletasks())

# Interface elements inside frame_02
password_lenghts = Label(frame_02, text="LENGTH", font=("Righteous", overall_font_size), fg=overall_background_button)
password_lenghts.place(x=10, y=10)

length_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
length_entry.insert(0, "9")
length_entry.place(x=140, y=10)

password_numbers_var = BooleanVar()
password_numbers = Checkbutton(frame_02,
                               text="NUMBERS",
                               font=("Righteous", int(overall_font_size) - 5),
                               variable=password_numbers_var,
                               borderwidth=0,
                               highlightthickness=0,
                               relief="groove",
                               fg=overall_background_button)
password_numbers.place(x=10, y=40)

special_chars_var = BooleanVar()
special_chars = Checkbutton(frame_02, text="SPECIAL CHARS", font=("Righteous", int(overall_font_size) - 5),
    variable=special_chars_var, borderwidth=0, highlightthickness=0, relief="groove",
    fg=overall_background_button)
special_chars.place(x=10, y=60)

special_chars_entry = Entry(frame_02, font=("Righteous", int(overall_font_size) - 2), fg=overall_background_button, justify='center', width=24)
special_chars_entry.insert(0, r"!§$%&/()=?+*#-_.:,;<>+-")
special_chars_entry.place(x=140, y=50)

generate_password_button = Button(frame_02,
                                  text="GENERATE PASSWORD",
                                  font=("Righteous", overall_font_size),
                                  relief="groove",
                                  command=generate_password,
                                  width=32)
generate_password_button.place(x=10, y=80)

created_pass = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center', width=32)
created_pass.place(x=11, y=120)

copy_button = Button(frame_02, text="COPY PASS", font=("Righteous", overall_font_size), relief="groove", command=copy_password,
                                  width=32)
copy_button.place(x=10, y=150)

passgenerator.mainloop()
