import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        entry.delete(0, tk.END)

def clear_entry():
    entry.delete(0, tk.END)

def button_click(char):
    entry.insert(tk.END, char)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 14), bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_num = 1
col_num = 0
for button_text in buttons:
    if button_text == '=':
        tk.Button(root, text=button_text, width=5, font=('Arial', 14), bd=5, command=calculate).grid(row=row_num, column=col_num, padx=5, pady=5)
    elif button_text == 'C':
        tk.Button(root, text=button_text, width=5, font=('Arial', 14), bd=5, command=clear_entry).grid(row=row_num, column=col_num, padx=5, pady=5)
    else:
        tk.Button(root, text=button_text, width=5, font=('Arial', 14), bd=5, command=lambda char=button_text: button_click(char)).grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()
