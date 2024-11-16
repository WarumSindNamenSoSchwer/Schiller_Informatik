from tkinter import *
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time) 

root: Tk = Tk()
root.title("Clock App")
root.geometry("800x500")

upper_frame = Frame(root, padx=10, pady=10, bg="red", height=120)
lower_frame = Frame(root, padx=10, pady=10, bg="green")

upper_frame.pack(fill=BOTH, expand=True)
lower_frame.pack(fill=BOTH, expand=True)

clock_label = Label(upper_frame, text="", font=("Arial", 60, "bold"), bg="red", fg="white")
clock_label.pack(expand=True)

checkbox = Button(lower_frame, text="Add tasks")
checkbox.pack(expand=True)

update_time()

root.mainloop()