from tkinter import *
from random import randint

root = Tk()
root.geometry("600x400")


welcome_label = Label(root, text="Welcome! Click the Generate button to generate your unique password.", font=("Arial bold", 12, "bold"), bg="black", fg="white")
welcome_label.pack(pady=10)
def new_rand() :
    pw_entry.delete(0, END)
    pw_length = int(ny_entry.get())
    ny_password = ''

    for _ in range(pw_length):
        ny_password += chr(randint(33, 126))

    pw_entry.insert(0, ny_password)


lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

ny_entry = Entry(lf, font=("Arial bold", 44))
ny_entry.pack(pady=20)


root.mainloop()
