import tkinter as tk
from tkinter import ttk
from lib.functions import close_window, open_file


class Menu(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        style = ttk.Style()
        style.configure("Menu.TButton", font=("Helvetica", 14, "italic"), foreground='purple', background="orange")
        style.map('Menu.TButton', background=[('active', 'darkorange'), ('pressed', 'red')], foreground=[('active', 'white')])

        self.open_button = ttk.Button(
            master=self, text="Open a File", command=open_file
        )
        self.open_button.pack(fill="both", expand=True)
        self.open_button.config(style='Menu.TButton')

        self.play_button = ttk.Button(master=self, text="Play")
        self.play_button.pack(fill="both", expand=True)

        self.end_button = ttk.Button(
            master=self,
            text="Quit",
            command=lambda: close_window(self),
        )
        self.end_button.pack(fill="both", expand=True)
