import numpy as np
import cv2
import customtkinter as ctk


class RotateMode:
    def __init__(self, master, window):
        self.master = master
        self.window = window

        self.img = None

        self.gamma = 1.0

        self.t1 = ctk.CTkLabel(self.master, text=f"ROTATE AND FLIP")

        self.b1 = ctk.CTkButton(self.master, text="RIGHT 90", command=self.right_90)
        self.b2 = ctk.CTkButton(self.master, text="LEFT 90", command=self.left_90)
        self.b3 = ctk.CTkButton(self.master, text="HORIZONTAL", command=self.horizontal)
        self.b4 = ctk.CTkButton(self.master, text="VERTICAL", command=self.vertical)

        self.t3 = ctk.CTkLabel(self.master, text=f"Fill the rotated angle value")
        self.b5 = ctk.CTkEntry(self.master)

        self.apply_button = ctk.CTkButton(self.master, text="Submit", command=self.select_angle)

        self.frames = [self.t1, self.b1, self.b2, self.b3, self.b4, self.t3, self.b5, self.apply_button]

    def right_90(self):
        self.img = cv2.rotate(self.window.img, cv2.ROTATE_90_CLOCKWISE)
        self.window.show_image(self.img)
        self.apply()

    def left_90(self):
        self.img = cv2.rotate(self.window.img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.window.show_image(self.img)
        self.apply()

    def horizontal(self):
        self.img = cv2.flip(self.window.img, 1)
        self.apply()

    def vertical(self):
        self.img = cv2.flip(self.window.img, 0)
        self.apply()

    def select_angle(self):
        image = self.window.img
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, -int(self.b5.get()), 1.0)
        self.img = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        self.apply()

    def hide(self):
        for x in self.frames:
            x.pack_forget()

    def pack(self):
        for x in self.frames:
            x.pack(pady=5)

    def apply(self):
        self.window.edit_image.append(self.img)
        self.window.img = self.window.edit_image.back()
        self.window.show_image(self.window.img)
