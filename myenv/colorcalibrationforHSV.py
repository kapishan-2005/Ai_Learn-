import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Sliders")
root.geometry("900x500")

# HSV variables
lh = tk.IntVar(value=0)
uh = tk.IntVar(value=179)
ls = tk.IntVar(value=100)
us = tk.IntVar(value=255)
lv = tk.IntVar(value=100)
uv = tk.IntVar(value=255)

# Frames
left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=10)

right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=10)

video_label = tk.Label(right_frame)
video_label.pack()

mask_label = tk.Label(left_frame)
mask_label.pack()

# Slider creator
def slider(text, var, frm, maxv):
    tk.Label(frm, text=text).pack()
    tk.Scale(frm, from_=0, to=maxv, orient="horizontal", variable=var, length=300).pack()

slider("Hue Low", lh, left_frame, 179)
slider("Hue High", uh, left_frame, 179)
slider("Saturation Low", ls, left_frame, 255)
slider("Saturation High", us, left_frame, 255)
slider("Value Low", lv, left_frame, 255)
slider("Value High", uv, left_frame, 255)

# Preset buttons
def set_red():
    lh.set(0); uh.set(10)
    ls.set(120); us.set(255)
    lv.set(70); uv.set(255)

def set_green():
    lh.set(35); uh.set(85)
    ls.set(80); us.set(255)
    lv.set(60); uv.set(255)

def set_blue():
    lh.set(90); uh.set(130)
    ls.set(80); us.set(255)
    lv.set(60); uv.set(255)

ttk.Button(right_frame, text="Reds", command=set_red).pack(fill="x")
ttk.Button(right_frame, text="Greens", command=set_green).pack(fill="x")
ttk.Button(right_frame, text="Blues", command=set_blue).pack(fill="x")

def update():
    ret, frame = cap.read()
    if not ret:
        root.after(10, update)
        return

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([lh.get(), ls.get(), lv.get()])
    upper = np.array([uh.get(), us.get(), uv.get()])

    mask = cv2.inRange(hsv, lower, upper)
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    img1 = ImageTk.PhotoImage(Image.fromarray(mask_rgb).resize((320, 240)))
    img2 = ImageTk.PhotoImage(Image.fromarray(frame_rgb).resize((320, 240)))

    mask_label.imgtk = img1
    mask_label.configure(image=img1)

    video_label.imgtk = img2
    video_label.configure(image=img2)

    root.after(10, update)

update()
root.mainloop()
cap.release()
