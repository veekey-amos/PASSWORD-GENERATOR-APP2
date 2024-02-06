from tkinter import *
from random import randint

root = Tk()
root.configure(bg='midnight blue')
root.geometry("600x400")
root.title('Password Generator")


welcome_label = Label(root, text="Welcome! Click the Generate button to generate your unique password.", font=("Arial bold", 12, "bold"), bg="black", fg="white")
welcome_label.pack(pady=10)
def new_rand() :
    pw_entry.delete(0, END)
    pw_length = int(ny_entry.get())
    ny_password = ''

    for _ in range(pw_length):
        ny_password += chr(randint(33, 126))

    pw_entry.insert(0, ny_password)

lf = LabelFrame(root, text="How Many Characters?", bg="midnightblue", padx=10, pady=10, fg="white")
lf.pack(pady=20)

ny_entry = Entry(lf, font=("Arial bold", 44), bg="white", fg="midnightblue")
ny_entry.pack(pady=20)

pw_entry = Entry(root, text='', font=('Arial bold', 24), bd=0, bg="white", fg="midnight blue")
pw_entry.pack(pady=20)

ny_frame = Frame(roo, bg="midnightblue")
ny_frame.pack(pady=20)

ny_button = Button(ny_frame, text="Generate unique password", command=new_rand, bg="black", fg= "white" )
ny_button.grid(row=0, column=0, padx=10)

root.mainloop()
