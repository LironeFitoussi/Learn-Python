import tkinter as tk

# Create a window
window = tk.Tk()

# Add a title to the window
window.title("My First GUI Program")

# Set the size of the window
window.minsize(width=500, height=300)

# Create a label
label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
# label.pack(side="right")
# label.pack(expand=True)
label.pack()


window.mainloop()
