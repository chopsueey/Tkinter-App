from tkinter import ttk

class Button(ttk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Styling
        self.style = ttk.Style()
        self.style.configure("Menu.TButton", font=("Helvetica", 14, "italic"), foreground='purple', background="orange")
        self.style.map('Menu.TButton', background=[('active', 'darkorange'), ('pressed', 'red')], foreground=[('active', 'white')])
        
        self.config(style='Menu.TButton')
