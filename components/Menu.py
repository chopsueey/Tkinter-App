import tkinter as tk
from tkinter import ttk
from .Button import Button
from lib.functions import close_window, open_file


class Menu(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Buttons

        self.open_button = Button(master=self, text="Open a File", command=open_file)
        self.open_button.pack(fill="both", expand=True)

        self.play_button = Button(master=self, text="Play")
        self.play_button.pack(fill="both", expand=True)

        self.end_button = Button(
            master=self,
            text="Quit",
            command=lambda: close_window(self),
        )
        self.end_button.pack(fill="both", expand=True)
