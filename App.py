import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from lib.functions import open_file, close_window
from components.Menu import Menu
from components.Soundbuttons import Soundbuttons


# Subklasse App mit vererbten Daten von Klasse Tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Soundboard")
        self.iconbitmap(r'./favicon.ico')
        # self.geometry("600x300")

        # Maingrid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Frames
        for i in range(0, self.grid_size()[0]):
            self.menu = Menu(master=self, relief="groove")
            self.menu.grid(column=i, row=i, padx=10, pady=10, sticky="nsew")

        # # Menuframe
        # self.main_menu = Menu(master=self, borderwidth=2, relief="groove", padding=10)
        # self.main_menu.grid(column=0, row=0, sticky="nsew", padx=2, pady=2)

        # # Soundbuttonsframe
        # self.soundbutton_frame = Soundbuttons(master=self, borderwidth=2, relief="groove", padding=10)
        # self.soundbutton_frame.grid(column=0, row=1, sticky="nsew", padx=2, pady=2)


    def run(self):
        self.mainloop()
