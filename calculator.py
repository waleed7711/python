import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field for displaying calculations
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

# Create and arrange buttons
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(fill=tk.BOTH, expand=True)
    for text in row:
        button = tk.Button(row_frame, text=text, font=("Arial", 18), relief=tk.RIDGE)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
        button.bind("<Button-1>", button_click)

# Run the application
root.mainloop()
