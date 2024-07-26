import tkinter as tk
import time

imtext = "#07100e"
background ="#fafdfd"
primary = "#35d3b4"
secondary = "#8df1dd"
accent = "#3df8d3"
sidebar = "#dbf0f0"


class myApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.button_state = False

        #Window
        self.title("clock app")
        self.geometry(f"{800}x{500}")
        #self.resizable(width=False, height=False)

        #Grid
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)

        #Frames
        self.sidebar_frame = tk.Frame(self, background=sidebar)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=0,column=1, rowspan=4, sticky="nsew")

        #Labels
        self.logo_label = tk.Label(self.sidebar_frame, text="Swift\nTasks", padx=10, pady=10, font=("Arial", 13, "bold"), background=sidebar)
        self.logo_label.grid(column=0, row=0)

        self.clock_label = tk.Label(self.main_frame, text="")


    def activate(self):
        if not self.button_state:
            self.Platzhalter.pack(expand=True)
            self.Platzhalter.pack(expand=True)
            self.button_state = True
        else:
            self.Platzhalter.pack_forget()
            self.platzhalter.pack_forget()

            self.button_state = False
        

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        #self.clock_label.config(text=current_time)
        self.after(1000, self.update_time)


if __name__ == "__main__":
    app = myApp()
    app.update_time()
    app.mainloop()

