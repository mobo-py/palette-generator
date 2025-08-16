import tkinter as tk

root = tk.Tk()
root.title("Rectangle Example")

screenwidth, screenheight = 800, 600

canvas = tk.Canvas(root, width=screenwidth, height=screenheight, bg="lightgray")
canvas.pack()


canvas.create_rectangle(0, 0, screenwidth/2, screenheight, fill="blue")

root.mainloop()