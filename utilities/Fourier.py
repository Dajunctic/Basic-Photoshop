from tkinter import StringVar

import numpy as np
import cv2
import customtkinter as ctk

class FourierMode:
    def __init__(self, master, window):
        self.master = master
        self.window = window

        self.img = None

        self.gamma = 1.0

        self.text = ctk.CTkLabel(self.master, text="FOURIER TRANSFORM", text_color="#18e9f0")

        self.apply_button = ctk.CTkButton(self.master, text="Apply", command=self.apply)

    def transform(self):
        self.img = cv2.cvtColor(self.window.img, cv2.COLOR_BGR2GRAY) if len(self.window.img.shape) != 2 else self.img

        dft = cv2.dft(np.float32(self.img), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

        self.img = magnitude_spectrum
        self.window.show_image(self.img)

    def hide(self):
        self.text.pack_forget()
        self.apply_button.pack_forget()

    def pack(self):
        self.text.pack(pady=20)
        self.apply_button.pack(pady=20)

    def apply(self):
        self.window.edit_image.append(self.img)
        self.window.img = self.window.edit_image.back()
        self.window.show_image(self.window.img)
