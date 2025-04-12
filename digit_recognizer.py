import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageDraw, ImageOps
import cv2
from tensorflow.keras.models import load_model

# Load model
model = load_model("model/digit_cnn.h5")

# Create main window
root = tk.Tk()
root.title("Digit Recognizer")
root.geometry("300x400")
root.resizable(False, False)

# Create canvas
canvas_width, canvas_height = 280, 280
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Image for drawing (PIL)
image = Image.new("L", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(image)

# Drawing logic
def draw_line(event):
    x, y = event.x, event.y
    r = 8
    canvas.create_oval(x - r, y - r, x + r, y + r, fill='black', outline='black')
    draw.ellipse((x - r, y - r, x + r, y + r), fill='black')

canvas.bind("<B1-Motion>", draw_line)

# Clear canvas
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_width, canvas_height], fill="white")

# Predict digit
def predict_digit():
    # Convert PIL image to OpenCV format
    img = image.copy()
    img = ImageOps.invert(img)  # MNIST is white digits on black
    img = img.resize((28, 28))
    img = np.array(img).astype("float32") / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img)
    digit = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    messagebox.showinfo("Prediction", f"Predicted Digit: {digit}\nConfidence: {confidence:.2f}%")

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Predict", command=predict_digit, width=10).pack(side="left", padx=10)
tk.Button(btn_frame, text="Clear", command=clear_canvas, width=10).pack(side="right", padx=10)

# Start GUI loop
root.mainloop()
