import tkinter as tk
from tkinter import ttk
from lib.functions import close_window, open_file


class Soundbuttons(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.heading = ttk.Label(self, text="Soundbuttons Area", font=("Arial", 14))
        self.heading.grid(padx=4, pady=4)  # rowspan=True, sticky="we"

        button_list = []
        button_names = [f"song {i}" for i in range(0, 5)]

        for i, name in enumerate(button_names):
            self.button = ttk.Button(master=self, text=name)
            button_list.append(self.button)
            self.button.grid()
