import os
import sys
import time
import PIL.ImageTk
from tkinter import *
from tkinter import messagebox, filedialog
import random
import string

overall_font = "Righteous"
overall_font_size = "14"
overall_background_button = "#00008B"


def resource_path(relative_path):
    """ This function is used to get the correct path for the image file (e.g., 'logo_02.png') """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def make_pass_one():
    root.destroy()
    passgenerator = Tk()
    passgenerator.title("Password Generator")
    passgenerator.config(width=600, height=400)  # Adjusted width for the frame and other content

    # Create a new frame for the image on the left
    frame_01 = Frame(passgenerator, width=120, height=200, bg="#00008B")
    frame_01.grid(row=0, column=0)

    # Load and display the image in the new frame
    photo = PIL.Image.open(resource_path("logo_02.png"))
    photo = photo.resize((100, 75))  # Resize the image to fit the frame
    photo = PIL.ImageTk.PhotoImage(photo)
    label = Button(frame_01, image=photo, bg="#00008B", bd=0, borderwidth=0)
    label.image = photo  # Behalte eine Referenz, um Garbage Collection zu vermeiden
    label.place(x=5, y=70)

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


def make_password_file():
    root.destroy()
    pass_generator_file = Tk()
    pass_generator_file.title("Password Generator")
    pass_generator_file.config(width=600, height=400)  # Adjusted width for the frame and other content

    # Create a new frame for the image on the left
    frame_01 = Frame(pass_generator_file, width=210, height=300, bg="#00008B")
    frame_01.grid(row=0, column=0)

    # Load and display the image in the new frame
    photo = PIL.Image.open(resource_path("logo_02.png"))
    photo = photo.resize((200, 150))
    photo = PIL.ImageTk.PhotoImage(photo)
    label = Label(frame_01, image=photo, bg="#00008B")
    label.image = photo
    label.place(x=0, y=70)

    # Create another frame for the password generator interface
    frame_02 = Frame(pass_generator_file, width=450, height=250)
    frame_02.grid(row=0, column=1)

    # Add the password file generation widgets inside frame_02
    password_lenghts = Label(frame_02, text="LENGTH", font=("Righteous", overall_font_size), fg=overall_background_button)
    password_lenghts.place(x=10, y=10)

    length_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
    length_entry.insert(0, "9")
    length_entry.place(x=200, y=10)

    password_pieces = Label(frame_02, text="PASSES / FILE", font=("Righteous", overall_font_size), fg=overall_background_button)
    password_pieces.place(x=10, y=40)

    length_pieces_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
    length_pieces_entry.insert(0, "10000")
    length_pieces_entry.place(x=200, y=40)

    password_pieces_sum = Label(frame_02, text="PASSES FILES", font=("Righteous", overall_font_size), fg=overall_background_button)
    password_pieces_sum.place(x=10, y=70)

    length_pieces_sum_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
    length_pieces_sum_entry.insert(0, "1")
    length_pieces_sum_entry.place(x=200, y=70)

    special_chars = Label(frame_02, text="SPECIAL CHARS", font=("Righteous", overall_font_size), fg=overall_background_button)
    special_chars.place(x=10, y=100)

    special_chars_entry = Entry(frame_02, font=("Righteous", int(overall_font_size) - 2), fg=overall_background_button, justify='center', width=24)
    special_chars_entry.insert(0, r"!§$%&/()=?+*#-_.:,;<>+-")
    special_chars_entry.place(x=200, y=100)

    file_names = Label(frame_02, text="FILENAMES", font=("Righteous", overall_font_size), fg=overall_background_button)
    file_names.place(x=10, y=130)

    file_names_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
    file_names_entry.insert(0, "passwords")
    file_names_entry.place(x=200, y=130)

    file_names_path = Label(frame_02, text="SAVE PATH", font=("Righteous", overall_font_size), fg=overall_background_button)
    file_names_path.place(x=10, y=160)

    file_names_path_entry = Entry(frame_02, font=("Righteous", overall_font_size), fg=overall_background_button, justify='center')
    file_names_path_entry.insert(0, r"C:/Temp/")
    file_names_path_entry.place(x=200, y=160)

    def generate_password(length, special_chars):
        characters = string.ascii_letters + string.digits + special_chars
        return ''.join(random.choice(characters) for i in range(length))

    def generate_and_save_passwords():
        length = int(length_entry.get())
        passes_per_file = int(length_pieces_entry.get())
        num_files = int(length_pieces_sum_entry.get())
        special_chars = special_chars_entry.get()
        file_name = file_names_entry.get()
        file_path = file_names_path_entry.get()
        passwords = set()  # to ensure uniqueness
        for _ in range(num_files):
            with open(f"{file_path}{file_name}_{_+1}.txt", "w") as f:
                for _ in range(passes_per_file):
                    password = generate_password(length, special_chars)
                    while password in passwords:  # ensure uniqueness
                        password = generate_password(length, special_chars)
                    passwords.add(password)
                    f.write(password + "\n")

    generate_button = Button(frame_02,
                             text="GENERATE FILES",
                             font=("Righteous", overall_font_size),
                             fg=overall_background_button,
                             command=generate_and_save_passwords,
                             width=37)
    generate_button.place(x=10, y=200)

    pass_generator_file.mainloop()


root = Tk()
root.title("Password Generator")
root.config(width=600, height=150)

# Create a frame for the image on the left
frame_01 = Frame(root, width=130, height=100, bg="#00008B")
frame_01.grid(row=0, column=0)

# Load and display the image
photo = PIL.Image.open(resource_path("logo_02.png"))
photo = photo.resize((100, 75))
photo = PIL.ImageTk.PhotoImage(photo)
label = Label(frame_01, image=photo, bg="#00008B")
label.image = photo  # Keep a reference to avoid garbage collection
label.place(x=10, y=10)

# Create another frame for the buttons on the right
frame_02 = Frame(root, width=400, height=100)
frame_02.grid(row=0, column=1)

generate_password_button = Button(frame_02,
                                  text="GENERATE PASSWORD",
                                  font=("Righteous", overall_font_size),
                                  relief="groove",
                                  command=make_pass_one,
                                  width=30)
generate_password_button.place(x=10, y=10)

generate_password_file = Button(frame_02,
                                text="GENERATE PASSWORD FILE",
                                font=("Righteous", overall_font_size),
                                relief="groove",
                                command=make_password_file,
                                width=30)
generate_password_file.place(x=10, y=50)

root.mainloop()
