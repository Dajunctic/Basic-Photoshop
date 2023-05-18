import cv2
import numpy as np
import customtkinter as ctk


class HistogramMode:
    def __init__(self, master, window):
        self.master = master
        self.window = window

        self.img = None

        self.gamma = 1.0
        self.t1 = ctk.CTkButton(self.master, text="HISTOGRAM", text_color="#18e9f0")

        self.b1 = ctk.CTkButton(self.master, text="Equalize", command=self.equalize, fg_color="#fca326")
        self.b2 = ctk.CTkButton(self.master, text="Equalize (CV2-colored)", command=self.equalize_cv2_colored, fg_color="#fca326")
        self.b3 = ctk.CTkButton(self.master, text="Equalize (CV2-grayscale)", command=self.equalize_cv2_grayscale, fg_color="#fca326")
        self.b4 = ctk.CTkButton(self.master, text="Adaptive EQ", command=self.adaptive_equalize, fg_color="#fca326")

        self.apply_button = ctk.CTkButton(self.master, text="Apply", command=self.apply)
        self.frames = [self.t1, self.b1, self.b2, self.b3, self.b4,
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

    def equalize(self):
        s_k = compute_sk(self.window.img)
        self.img = cv2.LUT(self.window.img, s_k)
        self.window.show_image(self.img)

    def equalize_cv2_colored(self):
        # equalized_img_cv2 = cv2.equalizeHist(img)
        R, G, B = cv2.split(self.window.img)

        output1_R = cv2.equalizeHist(R)
        output1_G = cv2.equalizeHist(G)
        output1_B = cv2.equalizeHist(B)

        self.img = cv2.merge((output1_R, output1_G, output1_B))
        self.window.show_image(self.img)

    def equalize_cv2_grayscale(self):
        self.img = cv2.equalizeHist(self.window.img)
        self.window.show_image(self.img)

    def adaptive_equalize(self):
        clahe = cv2.createCLAHE(clipLimit=40, tileGridSize=(8, 8))
        self.img = clahe.apply(self.window.img)
        self.window.show_image(self.img)


def compute_sk(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    h, w = img.shape[:2]
    hist = hist / (h * w)

    cdf = np.cumsum(hist)
    s_k = (255 * cdf - 0.5).astype("uint8")
    return s_k


def equalize(img):
    s_k = compute_sk(img)
    equalized_img = cv2.LUT(img, s_k)
    return equalized_img


def equalize_cv2_colored(img):
    # equalized_img_cv2 = cv2.equalizeHist(img)
    R, G, B = cv2.split(img)

    output1_R = cv2.equalizeHist(R)
    output1_G = cv2.equalizeHist(G)
    output1_B = cv2.equalizeHist(B)

    equ = cv2.merge((output1_R, output1_G, output1_B))
    return equ


def equalize_cv2_grayscale(img):
    equ = cv2.equalizeHist(img)
    return equ


def adaptive_equalize(img):
    clahe = cv2.createCLAHE(clipLimit=40, tileGridSize=(8, 8))
    clahe_high = clahe.apply(img)
    return clahe_high


def is_gray_scale(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            if r != g != b:
                return False
    return True
