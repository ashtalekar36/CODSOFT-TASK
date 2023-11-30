import tkinter as tk
from tkinter import ttk

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Calculate the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Set the width and height of the window
        window_width = 400
        window_height = 500

        # Calculate the x and y coordinates to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Configure a brighter color scheme
        self.root.configure(bg='#E6E6E6')
        ttk.Style().configure('TButton', background='#99CCFF', font=('Arial', 12))
        ttk.Style().configure('TLabel', background='#E6E6E6', font=('Arial', 12))
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for numbers
        self.entry_num1 = ttk.Entry(self.root, width=15, font=('Arial', 14))
        self.entry_num1.grid(row=0, column=0, columnspan=4, pady=10, padx=5, sticky='ew')

        # Display for the current operation
        self.operation_display = ttk.Label(self.root, text="", style='TLabel')
        self.operation_display.grid(row=1, column=0, columnspan=4, pady=5)

        # Buttons for digits and operations
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 1), ('.', 5, 2), ('=', 5, 3), ('+', 5, 0),
        ]

        for (text, row, column) in buttons:
            ttk.Button(self.root, text=text, command=lambda t=text: self.button_click(t),
                       width=5, style='TButton').grid(row=row, column=column, padx=5, pady=5)

        # History log
        self.history_label = ttk.Label(self.root, text="History:", style='TLabel')
        self.history_label.grid(row=6, column=0, columnspan=4, pady=5)

        self.history_text = tk.Text(self.root, height=5, width=30, font=('Arial', 10))
        self.history_text.grid(row=7, column=0, columnspan=4, pady=5)

    def button_click(self, value):
        current_num = self.entry_num1.get()

        if value == '=':
            try:
                result = eval(current_num)
                self.history_text.insert(tk.END, f"{current_num} = {result}\n")
                self.entry_num1.delete(0, tk.END)
                self.entry_num1.insert(tk.END, str(result))
                self.operation_display.config(text="")
            except Exception as e:
                self.entry_num1.delete(0, tk.END)
                self.entry_num1.insert(tk.END, "Error")
                self.operation_display.config(text="")
                print(e)
        else:
            new_num = current_num + str(value)
            self.entry_num1.delete(0, tk.END)
            self.entry_num1.insert(tk.END, new_num)

            if value in ('+', '-', '*', '/'):
                self.operation_display.config(text=f"{current_num} {value}")

# Create the main window
root = tk.Tk()
app = AdvancedCalculator(root)

# Run the main loop
root.mainloop()
