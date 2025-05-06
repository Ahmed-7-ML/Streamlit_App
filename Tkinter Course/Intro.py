from tkinter import *
# Every Thing is a Widget (Button, Text, Frame,...)

# Root Widget = Window = Frame
root = Tk()

# Label Widget
myLabel = Label(root, text="Hello, World!")

# Pack a widget in the parent widget.
# Shoving it onto Screen
myLabel.pack()

# Creating an Event Loop
root.mainloop()
