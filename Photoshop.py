import tkinter as tk
import customtkinter as ctk
from window import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1280x720")
app.resizable(False, False)


def init_menu():
    menubar = tk.Menu(app)
    app.config(menu=menubar)
    # ####### FILE MENU ############

    file_menu = tk.Menu(menubar, tearoff=False)

    file_menu.add_command(label='New', command=window.load_image)
    file_menu.add_command(label="Open", command=window.load_image)
    file_menu.add_command(label="Close", command=window.close_image)

    save_menu = tk.Menu(file_menu, tearoff=0)
    save_menu.add_command(label="PNG", command=window.save_png)
    save_menu.add_command(label="JPG", command=window.save_jpg)

    file_menu.add_cascade(label="Save to", menu=save_menu)

    sub_menu = tk.Menu(file_menu, tearoff=0)
    sub_menu.add_command(label='General...')
    sub_menu.add_command(label='Keyboard Shortcuts')
    sub_menu.add_command(label='Color Themes')
    sub_menu.add_command(label='Toolbar')

    file_menu.add_cascade(label="Preferences", menu=sub_menu)

    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=app.destroy)

    menubar.add_cascade(label="File", menu=file_menu, underline=0)

    # ############ EDIT MENU ##################
    edit_menu = tk.Menu(menubar, tearoff=False)
    edit_menu.add_command(label="Undo", command=window.undo)
    edit_menu.add_command(label="Redo", command=window.redo)
    menubar.add_cascade(label="Edit", menu=edit_menu, underline=0)

    # ############ IMAGE MENU ##################
    image_menu = tk.Menu(menubar, tearoff=False)
    image_menu.add_command(label="Mode")
    image_menu.add_command(label="Filter")
    menubar.add_cascade(label="Image", menu=image_menu, underline=0)

    # ############ WINDOW MENU ##################
    window_menu = tk.Menu(menubar, tearoff=False)
    window_menu.add_command(label="Options")
    menubar.add_cascade(label="Window", menu=window_menu, underline=0)

    # ############ HELP MENU ##################
    help_menu = tk.Menu(menubar, tearoff=False)
    help_menu.add_command(label="Welcome")
    help_menu.add_command(label="About")
    menubar.add_cascade(label="Help", menu=help_menu, underline=0)


if __name__ == '__main__':
    app.title(string="Photoshop")
    app.iconphoto(False, tk.PhotoImage(file='assets/icon.png'))
    window = Window(app)
    init_menu()
    app.mainloop()
