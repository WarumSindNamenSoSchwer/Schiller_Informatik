import tkinter as tk
import time

class myApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.button_state = False

        #Window
        self.title("clock app")
        self.geometry(f"{800}x{500}")
        self.resizable(width=False, height=False)

        #Frames
        self.main_frame = tk.Frame(self, background="grey")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.sidebar_btn = tk.Button(self.main_frame, width=2, height=1, command=self.activate)
        self.sidebar_btn.place(x=20, y=20)

        self.clock_label = tk.Label(self.main_frame, text="", font=("Arial", 60))
        self.clock_label.pack(expand=True)

        self.todo_frame = tk.Frame(self.main_frame, background="red")
        self.
        
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
        self.clock_label.config(text=current_time)
        self.after(1000, self.update_time)


if __name__ == "__main__":
    app = myApp()
    app.update_time()
    app.mainloop()