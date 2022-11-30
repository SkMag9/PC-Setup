import customtkinter as ctk
import subprocess as sp


def run_powershell(self, cmd):
    completed = sp.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    WIDTH = 800
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("PC Setup App")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ====== create two frames ======

        # ===== configure grid layout (2x1) =====
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = ctk.CTkFrame(master=self,
                                       width=180)
        self.left_frame.grid(row=0,
                             column=0,
                             sticky="nswe",
                             padx=10,
                             pady=10)

        self.right_frame = ctk.CTkFrame(master=self)
        self.right_frame.grid(row=0,
                              column=1,
                              sticky="nswe",
                              padx=10,
                              pady=10)

        # ===== left frames - tabs =====
        # ==== Main Label ====
        self.left_lbl_title = ctk.CTkLabel(master=self.left_frame,
                                           text="PC Setup",
                                           text_font=("Roboto Medium", -16))
        self.left_lbl_title.grid(row=0,
                                 column=0,
                                 padx=10,
                                 pady=10)

        # ==== Tab Buttons ====
        # === Change PC name ===
        self.left_btn_change_pc_name = ctk.CTkButton(master=self.left_frame,
                                                     text="Change PC name",
                                                     command=self.tab_change_pc_name())
        self.left_btn_change_pc_name.grid(row=1,
                                          column=0,
                                          padx=10,
                                          pady=5)

        # === Change Windows Key ===
        self.left_btn_change_windows_key = ctk.CTkButton(master=self.left_frame,
                                                         text="Change Windows key",
                                                         command=self.tab_change_windows_key())
        self.left_btn_change_windows_key.grid(row=2,
                                              column=0,
                                              padx=10,
                                              pady=5)

    def tab_change_pc_name(self):
        pass

    def tab_change_windows_key(self):
        pass

    def event_change_pc_name(self):
        powershell_command = ""
        powershell_return = run_powershell(powershell_command)
        if powershell_return.returncode != 0:
            print("An error ovvured: %s", powershell_return.stderr)
        else:
            print("Changed PC name successfully")

    def event_change_windows_key(self):
        pass

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
