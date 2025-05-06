import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

frame = tk.Tk()
frame.title("Eng/Ahmed Akram Amer 's Portofolio")
frame.geometry("500x400")

# 1) PhotoImage (Only for .png, .gif)
# my_img = tk.PhotoImage(file="example.png")

# 2) PIL.ImageTk (For .jpg, .png, .jpeg, etc.)
image = Image.open("MySelf.jpg")
photo = ImageTk.PhotoImage(image)
# Create Label To Hold The Image
label1 = tk.Label(frame, image=photo, width=300, height=300)
label1.pack(expand=True, fill="both")

info = """I am Student at Faculty of Electronics Engineering.
I am Interested in Machine Learning, Deep Learning, Computer Vision and Natural Language Processing.
See My Links Below...
"""

label2 = tk.Label(frame, text=info, bg="Black", fg="White", 
                  font=("Arial", 20, "bold"))
label2.pack()

def open_linkedin():
    webbrowser.open("www.linkedin.com/in/ahmed-akram-kamel-amer")

def open_github():
    webbrowser.open("https://github.com/Ahmed-7-ML")

def open_hackerrank():
    webbrowser.open("https://www.hackerrank.com/profile/a7m7da7e3")

# button1 = tk.Button(frame, text="Linkedin", fg="White", bg="#3480eb", command=open_linkedin, font="Serif 30 bold")
# button1.pack()

image1 = Image.open("Linkedin.png")
image1 = image1.resize((200, 200), Image.Resampling.LANCZOS) # Resize the image
tk_image1 = ImageTk.PhotoImage(image1) # Convert to Tkinter format
label3 = tk.Button(frame, image=tk_image1, command=open_linkedin) # Display image in a Label
label3.pack(pady=20, side="left")

# button2 = tk.Button(frame, text="Hackerrank", fg="White", bg="#3480eb", command=open_hackerrank, font="Serif 30 bold")
# button2.pack()

image2 = Image.open("Github.jpg")
image2 = image2.resize((200, 200), Image.Resampling.LANCZOS)
tk_image2 = ImageTk.PhotoImage(image2)
label4 = tk.Button(frame, image=tk_image2, command=open_github)
label4.pack(pady=20, side="right")

# button3 = tk.Button(frame, text="Github", fg="White", bg="#3480eb", command=open_github, font="Serif 30 bold")
# button3.pack()

image3 = Image.open("Hackerrank.png")
image3 = image3.resize((200, 200), Image.Resampling.LANCZOS)
tk_image3 = ImageTk.PhotoImage(image3)
label5 = tk.Button(frame, image=tk_image3, command=open_hackerrank)
label5.pack(pady=20)

frame.mainloop()