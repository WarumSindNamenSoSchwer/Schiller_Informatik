import tkinter as tk
from tkinter import ttk, messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window", font=("Arial", 16))
    label.pack(padx=20, pady=20)

def show_message():
    messagebox.showinfo("Info", "This is an information message.")

# Initialize the main window
root = tk.Tk()
root.title("Tkinter Widgets Example")
root.geometry("800x800")

# Frame for organizing the layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Adding a Label
label = tk.Label(frame, text="Label: Hello, Tkinter!", font=("Arial", 16), bg="lightblue")
label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Button
button = tk.Button(frame, text="Button: Click Me", command=on_button_click, font=("Arial", 14))
button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding an Entry
entry = tk.Entry(frame, font=("Arial", 14))
entry.insert(0, "Entry: Type here")
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Text widget
text = tk.Text(frame, height=5, width=30, font=("Arial", 14))
text.insert(tk.END, "Text: Multi-line input\n")
text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(frame, text="Checkbutton: Check me", variable=check_var, font=("Arial", 14))
checkbutton.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding Radiobuttons
radio_var = tk.StringVar(value="Option 1")
radiobutton1 = tk.Radiobutton(frame, text="Radiobutton: Option 1", variable=radio_var, value="Option 1", font=("Arial", 14))
radiobutton2 = tk.Radiobutton(frame, text="Radiobutton: Option 2", variable=radio_var, value="Option 2", font=("Arial", 14))
radiobutton1.grid(row=5, column=0, padx=5, pady=5, sticky="w")
radiobutton2.grid(row=5, column=1, padx=5, pady=5, sticky="w")

# Adding a Scale
scale = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, font=("Arial", 14), label="Scale")
scale.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Listbox
listbox = tk.Listbox(frame, font=("Arial", 14), height=4)
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)
listbox.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Combobox
combobox = ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"], font=("Arial", 14))
combobox.set("Combobox: Select an option")
combobox.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Canvas
canvas = tk.Canvas(frame, width=200, height=100, bg="white")
canvas.create_rectangle(50, 25, 150, 75, fill="blue")
canvas.create_oval(75, 25, 125, 75, fill="red")
canvas.create_line(0, 0, 200, 100, fill="green", width=3)
canvas.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Progressbar
progressbar = ttk.Progressbar(frame, length=200, mode='determinate')
progressbar['value'] = 50  # Sets the progress to 50%
progressbar.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=on_button_click)
file_menu.add_command(label="Open", command=on_button_click)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_message)

# Adding a PanedWindow
paned_window = tk.PanedWindow(frame, orient=tk.HORIZONTAL)
paned_window.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="we")

left_pane = tk.Label(paned_window, text="PanedWindow: Left Pane", bg="lightblue")
right_pane = tk.Label(paned_window, text="PanedWindow: Right Pane", bg="lightgreen")
paned_window.add(left_pane)
paned_window.add(right_pane)

# Adding a Notebook
notebook = ttk.Notebook(frame)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Notebook: Tab 1")
notebook.add(tab2, text="Notebook: Tab 2")
label_tab1 = ttk.Label(tab1, text="Content of Tab 1", font=("Arial", 14))
label_tab2 = ttk.Label(tab2, text="Content of Tab 2", font=("Arial", 14))
label_tab1.pack(padx=10, pady=10)
label_tab2.pack(padx=10, pady=10)
notebook.grid(row=12, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Treeview
treeview = ttk.Treeview(frame, columns=("size", "modified"), show="headings")
treeview.heading("size", text="Size")
treeview.heading("modified", text="Modified")
treeview.insert("", "end", values=("10KB", "2023-07-03"))
treeview.insert("", "end", values=("20KB", "2023-07-04"))
treeview.grid(row=13, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Adding a Scrollbar to a Text widget
scroll_text = tk.Text(frame, height=5, width=30, font=("Arial", 14))
scroll_text.grid(row=14, column=0, padx=5, pady=5, sticky="w")

scrollbar = tk.Scrollbar(frame, command=scroll_text.yview)
scrollbar.grid(row=14, column=1, sticky="nsew")
scroll_text.config(yscrollcommand=scrollbar.set)

# Adding a button to open a new window
new_window_button = tk.Button(frame, text="Open New Window", command=open_new_window, font=("Arial", 14))
new_window_button.grid(row=15, column=0, columnspan=2, padx=5, pady=5, sticky="w")

root.mainloop()
