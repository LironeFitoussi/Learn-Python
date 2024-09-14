import tkinter as tk

# Create a window
window = tk.Tk()

# Add a title to the window
window.title("My First GUI Program")

# Set the size of the window
window.minsize(width=500, height=300)


# Create a Button
button = tk.Button(text="Click Me")
# button.pack()


# Create a label
label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
# label.pack(side="right")
# label.pack(expand=True)
# label.pack()

# Use place to set the position of the label
# label.place(x=100, y=200)

# Change the label's postion using the grid method
label.grid(column=0, row=0)

# Text can be changed using the config method
label["text"] = "New Text"
label.config(text="New Text")


# Creathe Text
text = tk.Text(height=5, width=30)
# text.pack()

window.mainloop()
