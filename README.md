# Digit Recognizer Application
# Overview
This application is a simple digit recognizer built using Python's Tkinter library for the graphical user interface (GUI) and a Convolutional Neural Network (CNN) model trained to recognize handwritten digits (0-9). Users can draw digits on a canvas, and the application will predict the digit using the trained model.

# Features
Draw digits on a canvas using the mouse.
Predict the drawn digit using a pre-trained CNN model.
Display the predicted digit and the confidence level in a message box.
Clear the canvas to draw a new digit.
Requirements
Python 3.x
TensorFlow
NumPy
OpenCV
Pillow (PIL)
Tkinter (comes pre-installed with Python)
Installation
Clone the repository:


git clone https://github.com/yourusername/digit-recognizer.git
cd digit-recognizer
Install required packages: You can install the required packages using pip:

pip install tensorflow numpy opencv-python pillow
Download the pre-trained model: Ensure you have the trained model file digit_cnn.h5 in the model directory. If you do not have the model, you will need to train a CNN model on the MNIST dataset and save it as digit_cnn.h5.

Usage
Run the application: Execute the following command in your terminal:

Draw a digit: Use your mouse to draw a digit on the canvas.

Predict the digit: Click the "Predict" button to see the predicted digit and its confidence level.

Clear the canvas: Click the "Clear" button to reset the canvas for a new drawing.

Code Structure
app.py: The main application file containing the GUI and digit recognition logic.
model/digit_cnn.h5: The pre-trained CNN model file for digit recognition.
Key Functions
draw_line(event): Handles the drawing of the digit on the canvas when the mouse is moved while the left button is pressed.
clear_canvas(): Clears the canvas and resets the drawing area.
predict_digit(): Processes the drawn image, predicts the digit using the CNN model, and displays the prediction and confidence in a message box.
Example Code Snippet
Here is a brief overview of the main components of the code:

# Load model
model = load_model("model/digit_cnn.h5")

# Create main window
root = tk.Tk()
root.title("Digit Recognizer")
root.geometry("300x400")
root.resizable(False, False)

# Create canvas
canvas = tk.Canvas(root, width=280, height=280, bg='white')
canvas.pack()

# Drawing logic
def draw_line(event):
    # Drawing logic here

# Predict digit
def predict_digit():
    # Prediction logic here

# Buttons
tk.Button(btn_frame, text="Predict", command=predict_digit, width=10).pack(side="left", padx=10)
tk.Button(btn_frame, text="Clear", command=clear_canvas, width=10).pack(side="right", padx=10)

# Start GUI loop
root.mainloop()
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
