import customtkinter
import time

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Time keeping TODO app")
        self.geometry(f"{800}x{400}") 
        self.resizable(width=False, height=False)

        #Create frame for time
        self.clock_frame = customtkinter.CTkFrame(self, corner_radius=1, width=800, fg_color="transparent")
        self.clock_frame.pack(side="top",expand=True, fill="both")

        self.line_between_frames = customtkinter.CTkFrame(self, corner_radius=0, height=2, width=800,fg_color="light grey", bg_color="transparent")
        self.line_between_frames.pack(side="top", expand=True)

        self.test_row = customtkinter.CTkFrame(self, corner_radius=0, width=800, fg_color="transparent")
        self.test_row.pack(side="top",expand=True, fill="both")

        self.clock_label = customtkinter.CTkLabel(self.clock_frame, text="", font=customtkinter.CTkFont(size=70, weight="bold"))
        self.clock_label.pack(pady=10, padx=10, expand=True)

        self.expand_menu_checkbox = customtkinter.CTkCheckBox(self.test_row, text="Expand Menu")
        self.expand_menu_checkbox.pack(pady=10, padx=10, expand=True)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.configure(text=current_time)
        self.after(1000, self.update_time)

    def expand_(self):
        pass

app = App()
app.update_time()
app.mainloop()