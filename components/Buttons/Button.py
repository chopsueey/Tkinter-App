from tkinter import ttk

class Button(ttk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, style='Secondary.TButton', **kwargs)

