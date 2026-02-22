#add 9 buttons for numbers 0-9 and buttons for +,-,*,/ and = and a clear button to clear the entry field
import tkinter as tk
def on_button_click(value):
    if value == "C":
        entry_field.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry_field.get())
            entry_field.delete(0, tk.END)
            entry_field.insert(0, str(result))
        except Exception as e:
            entry_field.delete(0, tk.END)
            entry_field.insert(0, "Error")
    else:
        entry_field.insert(tk.END, value)
root = tk.Tk()
root.title("Simple Calculator")
entry_field = tk.Entry(root, width=35, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button_values = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]
row = 1
col = 0
for value in button_values:
    button = tk.Button(root, text=value, width=9, height=3, command=lambda v=value: on_button_click(v))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
root.mainloop()