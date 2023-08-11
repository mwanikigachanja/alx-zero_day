import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CMG Calculator")

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12, 'bold'))

        self.entry = tk.Entry(root, font=('Helvetica', 20), borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, column) in buttons:
            button = ttk.Button(root, text=text, padding=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, value):
        current = self.entry.get()
        if value == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

