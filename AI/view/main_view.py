import customtkinter
import config.config as cfg
from controller.controller import Controller
from view.input_view import IntputFrame
from view.output_view import OutputFrame
from tkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("TFT-AI")
        self.geometry("1100x500")
        self.iconbitmap(cfg.icon_logo_ulpgc)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.output_frame.configure(fg_color="transparent")

        self.input_frame = IntputFrame(self)
        self.input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def predict_button_action(self):
        prediction = Controller.run_ai(self.output_frame.get_image())
        self.output_frame.set_image_label(prediction)

    @staticmethod
    def change_theme():
        if customtkinter.get_appearance_mode() == "Dark":
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")

    def browse_file(self):
        file = filedialog.askopenfile()
        if file is not None:
            self.output_frame.set_image_label("indeterminada.")
            self.output_frame.display_image(file.name)


if __name__ == "__main__":
    app = App()
    app.mainloop()
