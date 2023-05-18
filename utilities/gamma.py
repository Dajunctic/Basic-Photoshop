from tkinter import StringVar

import numpy as np
import cv2
import customtkinter as ctk

class GammaMode:
    def __init__(self, master, window):
        self.master = master
        self.window = window

        self.img = None

        self.gamma = 1.0

        self.text = ctk.CTkLabel(self.master, text=f"γ = {self.gamma}")

        self.slider = ctk.CTkSlider(self.master, from_=1, to=50, width=120, command=self.adjust_gamma)
        self.slider.set(self.gamma * 10)

        self.apply_button = ctk.CTkButton(self.master, text="Apply", command=self.apply)

    def adjust_gamma(self, e):
        image = self.window.img
        self.gamma = int(self.slider.get()) / 10
        self.text.configure(text=f"γ = {self.gamma}")

        invGamma = 1.0 / self.gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")

        self.img = cv2.LUT(image, table)
        self.window.show_image(self.img)

    def hide(self):
        self.text.pack_forget()
        self.slider.pack_forget()
        self.apply_button.pack_forget()

    def pack(self):
        self.text.pack(pady=20)
        self.slider.pack()
        self.apply_button.pack(pady=20)

    def apply(self):
        self.window.edit_image.append(self.img)
        self.window.img = self.window.edit_image.back()
        self.window.show_image(self.window.img)
