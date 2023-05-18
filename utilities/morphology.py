import cv2
import numpy as np
import customtkinter as ctk


class MorphMode:
    def __init__(self, master, window):
        self.master = master
        self.window = window

        self.img = None

        self.gamma = 1.0

        self.erode_button = ctk.CTkButton(self.master, text="Erode", command=self.erode, fg_color="#fca326")
        self.dilate_button = ctk.CTkButton(self.master, text="Dilate", command=self.dilate, fg_color="#fca326")
        self.opening_button = ctk.CTkButton(self.master, text="Opening", command=self.opening, fg_color="#fca326")
        self.closing_button = ctk.CTkButton(self.master, text="closing", command=self.closing, fg_color="#fca326")

        self.apply_button = ctk.CTkButton(self.master, text="Apply", command=self.apply)
        self.frames = [self.erode_button, self.dilate_button, self.opening_button, self.closing_button,
                       self.apply_button]

    def hide(self):
        for x in self.frames:
            x.pack_forget()

    def pack(self):
        for x in self.frames:
            x.pack(pady=20)

    def apply(self):
        self.window.edit_image.append(self.img)
        self.window.img = self.window.edit_image.back()
        self.window.show_image(self.window.img)

    def erode(self):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        self.img = cv2.erode(self.window.img, kernel, iterations=2)
        self.window.show_image(self.img)

    def dilate(self):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        self.img = cv2.dilate(self.window.img, kernel, iterations=2)
        self.window.show_image(self.img)

    def opening(self):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        self.img = cv2.morphologyEx(self.window.img, cv2.MORPH_OPEN, kernel)
        self.window.show_image(self.img)

    def closing(self):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        self.img = cv2.morphologyEx(self.window.img, cv2.MORPH_CLOSE, kernel)
        self.window.show_image(self.img)


def erode(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    return cv2.erode(img, kernel, iterations=2)


def dilate(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    return cv2.dilate(img, kernel, iterations=2)


def opening(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


def closing(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
