from tkinter import StringVar

import numpy as np
import cv2
import customtkinter as ctk


class BlurMode:
    def __init__(self, master, window):
        self.master = master
        self.window = window

        self.img = None
        self.g_kernel_size = 1
        self.sigmoid = 0

        self.m_kernel_size = 1

        self.text1 = ctk.CTkLabel(self.master, text=f"Gaussian Blur", text_color="#30c9f0")
        self.text2 = ctk.CTkLabel(self.master,
                                  text=f"Kernel size: {self.g_kernel_size}x{self.g_kernel_size} | σ: {self.sigmoid}")

        self.slider = ctk.CTkSlider(self.master, from_=0, to=50, width=120, command=self.gaussian_blur)
        self.slider.set(self.g_kernel_size / 2)
        self.sigmoid_slider = ctk.CTkSlider(self.master, from_=0, to=200, width=120, command=self.gaussian_blur)
        self.sigmoid_slider.set(self.sigmoid * 10)

        self.text3 = ctk.CTkLabel(self.master, text="Median Blur", text_color="#30c9f0")
        self.text4 = ctk.CTkLabel(self.master, text=f"Kernel size: {self.m_kernel_size}x{self.m_kernel_size}")
        self.median_slider = ctk.CTkSlider(self.master, from_=0, to=50, width=120, command=self.median_blur)
        self.median_slider.set(self.m_kernel_size / 2)

        self.apply_button = ctk.CTkButton(self.master, text="Apply", command=self.apply)

    def gaussian_blur(self, e):
        self.g_kernel_size = int(self.slider.get()) * 2 + 1
        self.sigmoid = int(self.sigmoid_slider.get()) / 10

        self.text2.configure(text=f"Kernel size: {self.g_kernel_size}x{self.g_kernel_size} | σ: {self.sigmoid}")

        self.img = cv2.GaussianBlur(self.window.img, (self.g_kernel_size, self.m_kernel_size), self.sigmoid)
        self.window.show_image(self.img)

    def median_blur(self, e):
        self.m_kernel_size = int(self.median_slider.get()) * 2 + 1
        self.text4.configure(text=f"Kernel size: {self.m_kernel_size}x{self.m_kernel_size}")

        self.img = cv2.medianBlur(self.window.img, self.m_kernel_size)
        self.window.show_image(self.img)

    def hide(self):
        self.text1.pack_forget()
        self.text2.pack_forget()
        self.slider.pack_forget()
        self.sigmoid_slider.pack_forget()

        self.text3.pack_forget()
        self.text4.pack_forget()
        self.median_slider.pack_forget()

        self.apply_button.pack_forget()

    def pack(self):
        self.text1.pack()
        self.text2.pack(pady=20)
        self.slider.pack()
        self.sigmoid_slider.pack(pady=20)

        self.text3.pack()
        self.text4.pack(pady=20)
        self.median_slider.pack()

        self.apply_button.pack(pady=20)

    def apply(self):
        self.window.edit_image.append(self.img)
        self.window.img = self.window.edit_image.back()
        self.window.show_image(self.window.img)
