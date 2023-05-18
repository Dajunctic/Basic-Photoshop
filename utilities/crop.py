from tkinter import StringVar

import numpy as np
import cv2
import customtkinter as ctk


class CropMode:
    def __init__(self, master, window):
        self.master = master
        self.window = window

        self.img = None

        self.frames = []

        self.label = ctk.CTkLabel(master, text="Enter starting X:")
        self.frames.append(self.label)

        # Create an Entry widget and grid it on the first row, second column
        self.input_box = ctk.CTkEntry(master)
        self.frames.append(self.input_box)

        # Create a second Label widget and grid it on the second row, first column
        self.label2 = ctk.CTkLabel(master, text="Enter starting Y:")
        self.frames.append(self.label2)

        # Create a second Entry widget and grid it on the second row, second column
        self.input_box2 = ctk.CTkEntry(master)
        self.frames.append(self.input_box2)

        self.label3 = ctk.CTkLabel(master, text="Enter width:")
        self.input_box3 = ctk.CTkEntry(master)
        self.frames.append(self.label3)
        self.frames.append(self.input_box3)

        self.label4 = ctk.CTkLabel(master, text="Enter height:")
        self.input_box4 = ctk.CTkEntry(master)
        self.frames.append(self.label4)
        self.frames.append(self.input_box4)

        self.submit_button = ctk.CTkButton(master, text="Submit",
                                           command=lambda: self.crop_image_callback(self.input_box.get(),
                                                                                    self.input_box2.get(),
                                                                                    self.input_box3.get(),
                                                                                    self.input_box4.get(), window))
        self.frames.append(self.submit_button)

        self.label5 = ctk.CTkLabel(master, text="Image size: " + str(self.window.img.shape[0]) + "x" + str(
            self.window.img.shape[1]))
        self.frames.append(self.label5)

        self.apply_button = ctk.CTkButton(self.master, text="Apply", command=self.apply)
        self.frames.append(self.apply_button)

        self.error = ctk.CTkLabel(master, text="WRONG INPUT.\n PLEASE INSERT AGAIN", text_color="#ff4f42")


    def crop_image_callback(self, x, y, width, height, window):
        new_x = int(x)
        new_y = int(y)
        new_width = int(width)
        new_height = int(height)

        image_width = self.window.img.shape[0]
        image_height = self.window.img.shape[1]

        if new_x + new_width > image_width or new_y + new_height > image_height or new_x < 0 or new_y < 0 or new_width < 0 or new_height < 0:
            self.error.pack()
        else:
            self.error.pack_forget()
            self.img = self.window.img[new_x:new_width, new_y:new_height]

            # self.window.edit_image.append(self.window.img[new_x:new_width, new_y:new_height])
            # self.window.img = self.window.edit_image.back()
            self.window.show_image(self.img)

    def hide(self):
        self.error.pack_forget()
        for x in self.frames:
            x.pack_forget()

    def pack(self):
        for x in self.frames:
            x.pack(pady=5)

    def apply(self):
        self.label5.configure(text="Image size: " + str(self.img.shape[0]) + "x" + str(
            self.img.shape[1]))

        self.window.edit_image.append(self.img)
        self.window.img = self.window.edit_image.back()
        self.window.show_image(self.window.img)
