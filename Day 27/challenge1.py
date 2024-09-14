import tkinter as tk

window = tk.Tk()
window.title("Grid Challenge")
window.minsize(width=500, height=500)

# Set Empty Cell
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# window.rowconfigure(2, weight=1)
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)
# window.columnconfigure(3, weight=1)

# Create a label
label = tk.Label(text="Name:")

# Place the label in the first row and first column
label.grid(column=0, row=0)

# Create a button
button = tk.Button(text="New Button")
button.grid(column=2, row=0)

# Create a second button
button2 = tk.Button(text="Button")
button2.grid(column=1, row=1)

# Create an Entry
entry = tk.Entry(text="Entry")
entry.grid(column=3, row=2)

window.mainloop()
