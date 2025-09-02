import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")

        # Display variable
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        # Create display
        display = tk.Entry(root, textvariable=self.display_var,
                           font=("Arial", 16), justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        # Button layout
        buttons = [
            ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            if text == '0':
                btn = tk.Button(root, text=text, font=("Arial", 14),
                                command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, columnspan=2, padx=2, pady=2, sticky="ew")
            else:
                btn = tk.Button(root, text=text, font=("Arial", 14),
                                command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="ew")


        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def button_click(self, char):
        current = self.display_var.get()

        if char == 'C':
            self.display_var.set("0")
        elif char == '=':
            try:

                expression = current.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.display_var.set(result)
            except:
                messagebox.showerror("Error", "Invalid calculation")
                self.display_var.set("0")
        elif char in '+-×÷':
            if current[-1] not in '+-×÷':
                self.display_var.set(current + char)
        else:
            if current == "0":
                self.display_var.set(char)
            else:
                self.display_var.set(current + char)


# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
