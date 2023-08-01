"""
Create a simple calculator program with a GUI interface. 
Make your title of the Calculator programme window with your name
"""

import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    result = eval(expression)
    display.delete(0, tk.END)
    display.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Calculator by Lubembe Colin Wafula")

# Create the display widget
display = tk.Entry(window, width=20, font=("Arial", 12))
display.grid(row=0, column=0, columnspan=4)

# Create number buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
row, col = 1, 0
for button in buttons:
    btn = tk.Button(window, text=button, width=5, height=2,
                    command=lambda num=button: button_click(num))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear button
clear_btn = tk.Button(window, text="C", width=5, height=2, command=button_clear)
clear_btn.grid(row=row, column=col)

# Create the equal button
equal_btn = tk.Button(window, text="=", width=5, height=2, command=button_equal)
equal_btn.grid(row=row+1, column=col)

# Start the main event loop
window.mainloop()
