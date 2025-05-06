import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

button1 = tk.Button(root, text="My Button")
button1.pack(side="left", anchor="nw", padx=10, pady=10) # nw = north west


entry1 = tk.Entry(root, width=20)
entry1.pack(padx=10, pady=10, anchor="nw", side="left",
            ipady=5, fill="both", expand=True) # fill = "x" | "y" | "both" | "none"

root.mainloop()