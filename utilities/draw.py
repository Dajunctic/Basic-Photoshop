import io

import customtkinter as ctk
import tkinter as tk
from tkinter import StringVar
import numpy as np
from CTkColorPicker import AskColor
from PIL import ImageGrab, ImageTk
import cv2
from PIL import Image, EpsImagePlugin

EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs10.01.1\bin\gswin64c.exe'

class DrawMode:
    def __init__(self, master, canvas, canvas_frame, window):
        self.canvas_frame = canvas_frame
        self.window = window
        self.canvas = canvas
        self.master = master
        self.size = 2
        self.size_text = StringVar()
        self.size_text.set(f"Size: {self.size} px")
        self.color = "#000000"
        self.text1 = ctk.CTkLabel(self.master, text=f"Size: {self.size} px")

        self.slider = ctk.CTkSlider(self.master, from_=1, to=20, width=120, command=self.change_size)
        self.slider.set(self.size)

        self.text2 = ctk.CTkLabel(self.master, text="Color")
        self.button = ctk.CTkButton(self.master, width=40, height=40, text="", fg_color=self.color,
                                    hover_color=self.color, command=self.ask_color)

        self.lasx = 0
        self.lasy = 0

        self.apply_button = ctk.CTkButton(self.master, text="Apply", command=self.apply)

    def hide(self):
        self.text1.pack_forget()
        self.slider.pack_forget()
        self.text2.pack_forget()
        self.button.pack_forget()
        self.apply_button.pack_forget()

        self.canvas.bind("<B1-Motion>")

    def pack(self):
        self.text1.pack(pady=20)
        self.slider.pack()
        self.text2.pack(pady=10)
        self.button.pack()
        self.apply_button.pack(pady=20)

    def change_size(self, e):
        self.size = self.slider.get()
        self.text1.configure(text=f"Size: {int(self.size)} px")

    def ask_color(self):
        pick_color = AskColor()  # open the color picker
        self.color = pick_color.get()  # get the color string
        self.button.configure(fg_color=self.color)

    def get_x_and_y(self, e):
        self.lasx, self.lasy = e.x, e.y

    def draw_sth(self, e):
        self.canvas.create_line((self.lasx, self.lasy, e.x, e.y), fill=self.color, width=self.size)
        self.lasx, self.lasy = e.x, e.y

    def can_draw(self):
        self.canvas.bind("<Button-1>", self.get_x_and_y)
        self.canvas.bind("<B1-Motion>", self.draw_sth)

    def apply(self):

        img = ImageGrab.grab(bbox=(
            self.canvas.winfo_rootx() + self.window.app.winfo_rootx(),
            self.canvas.winfo_rooty() + self.window.app.winfo_rooty(),
            self.canvas.winfo_rootx() + self.canvas.winfo_width(),
            self.canvas.winfo_rooty() + self.canvas.winfo_height()
        ))

        self.window.edit_image.append(np.array(img.convert("RGB")))
        self.window.img = self.window.edit_image.back()
        self.window.show_image(self.window.img)

