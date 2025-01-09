# Cool library to create GUI applications. Tkinter provides a variety of
#   widgets (buttons, labels, text boxes, etc.).
import tkinter as tk
import random
import string

# First window instance
scrollwindow1 = tk.Tk()
scrollwindow1.title("W1")
scrollwindow1.geometry("400x100+100+100")
scrollwindow1.configure(bg="black")
button1 = tk.Button(scrollwindow1, text="Click on W1", command=lambda: print("Button Clicked"))

# Second window instance
scrollwindow2 = tk.Toplevel()
scrollwindow2.title("W2")
scrollwindow2.geometry("400x100+100+200")
scrollwindow2.configure(bg="black")
button2 = tk.Button(scrollwindow2, text="Click on W2", command=lambda: print("Button Clicked"))

# Make the second window a transient window
#scrollwindow2.transient(scrollwindow1) 

canvas = tk.Canvas(scrollwindow1, width=200, height=200, bg="black")
canvas.pack()

def random_text():
    return ''.join(random.choices(string.ascii_uppercase, k=1))

text_id = canvas.create_text(200, 50, text=random_text(), font=("Arial", 24), fill="white")

scrolling = True

def scroll_text():
    if scrolling:
        canvas.move(text_id, -5, 0)
        canvas.itemconfig(text_id, text=random_text())
        canvas.update()
        canvas.after(400, scroll_text)

def stop_scrolling():
    global scrolling
    scrolling = False

stop_button = tk.Button(scrollwindow1, text="Stop", command=stop_scrolling)
stop_button.pack()

scroll_text()

scrollwindow1.mainloop()