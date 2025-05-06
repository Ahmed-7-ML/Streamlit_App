# Tkinter = Tk Interface
# Tkinter is Python’s standard GUI framework
# Window(Frame) : Foundational Element of Tkinter GUI
# Window : Containers in which all other GUI Elements Live
# GUI Elements inside the Windom : Text Box, Label, Button,.. -> Widget

# Widgets are the bread and butter of the Python GUI framework Tkinter.
# They ’re the elements through which users interact with your program.
# Each widget in Tkinter is defined by a class. 
# Some Widgets : Label, Button, Entry, Text, Frame

# Label : Widget to Display Text/ Images on Screen (For Display-Purpose Only)
# Button : Widget that Contains Text and Can Perform an Action When Clicked On.
# Entry : Text Entry Widget that allows only single line of Text
# Text : Text Entry Widget that allows multiple lines of Text
# Frame : Rectangular region used to group related widgets or provide padding between widgets

# Widget Types : classic vs. themed

import tkinter as tk
import webbrowser

# Main Frame
frame = tk.Tk(className="Ahmed Akram") # Instance of Tkinter's Tk Class
frame.title("My Beautiful App")
frame.geometry("500x300")

def Exit():
    exit

def say_hello(name="Ahmed"):
    print(f"Hello {name}")

def open_web():
    link = text1.get()
    webbrowser.open(link)

label1 = tk.Label(text="Welcome !", font="Tahoma 30 italic", fg="purple", bg="orange", width=20, height=5)
label1.pack(padx=10, pady=30) # Must Written to Actually Display the Widget

text1= tk.Entry(frame, width=50)
text1.pack(padx=10, pady=30)

# Create a Button
# Hexadecimal RGB values are more cryptic than named colors
button1 = tk.Button(frame, text="Submit", fg="#88cfa9", bg="green", font="Serif 20 bold italic", padx=10, pady=3, command=say_hello) # width=10, height=10
button1.pack(side="top") # side = "left" | "right" | "top" | "bottom"

# The Widget in the window isn’t square even though the width and height are both set to 10. 
# This is because the width and height are measured in text units. 
# One horizontal text unit is determined by the width of the character 0, or the number zero, 
# Similarly, one vertical text unit is determined by the height of the character 0.

button2 = tk.Button(frame, text="Go to Link", fg="#88cfa9", bg="green", font="Serif 20 bold italic", padx=10, pady=3, command=open_web)

button2.pack(side="bottom")

# Run the Tkinter Event Loop
# In computing, a process that is blocked is waiting for some event, 
# such as a resource becoming available or the completion of an I/O operation.
# Once the event occurs for which the process is waiting ("is blocked on"), 
# the process is advanced from blocked state to an imminent one, such as runnable.
frame.mainloop()

# ======================================================================================


# from tkinter import messagebox
# window.title("Simple GUI Example")
# window.geometry("300x200")  # Set window size (width x height)

# # Function to handle button click
# def on_button_click():
#     user_input = entry.get()  # Get text from entry field
#     if user_input:
#         output_label.config(text=f"Hello, {user_input}!")
#     else:
#         messagebox.showwarning("Input Error", "Please enter your name!")

# # Create and place widgets
# # Label
# label = tk.Label(window, text="Enter your name:", font=("Arial", 12), fg="blue")
# label.pack(pady=10)

# # Entry (text input)
# entry = tk.Entry(window, width=20)
# entry.pack(pady=10)

# # Button
# button = tk.Button(window, text="Submit", command=on_button_click,bg="green", fg="white")
# button.pack(pady=10)

# # Output Label
# output_label = tk.Label(window, text="")
# output_label.pack(pady=10)