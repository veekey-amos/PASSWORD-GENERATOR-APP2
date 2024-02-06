from tkinter import *
from random import randint

root = Tk()
root.geometry("600x400")


welcome_label = Label(root, text="Welcome! Click the Generate button to generate your unique password.", font=("Arial bold", 12, "bold"), bg="black", fg="white")
welcome_label.pack(pady=10)

root.mainloop()