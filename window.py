import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My Window")

# Set the window size
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Hello, World!")
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="Click Me", command=lambda: print("Button Clicked"))
button.pack(pady=20)

# Run the application
root.mainloop()