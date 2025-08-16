import tkinter as tk
import random
import pyperclip

root = tk.Tk()
root.title("Palette Generator")
root.configure(bg="lightgray")

screenwidth, screenheight = 800, 600

canvas = tk.Canvas(root, width=screenwidth, height=screenheight - 100, bg="lightgray", highlightthickness=0)
canvas.pack()

last_color = None  # remember last color to avoid repeats


def random_color(prev_color=None):
    """Generate a random hex color different from prev_color."""
    while True:
        color = "#" + "".join(random.choice("0123456789ABCDEF") for _ in range(6))
        if color != prev_color:
            return color


class ColorBlock:
    def __init__(self, x1, y1, x2, y2, parent_frame):
        self.color = "#0000FF"  # default blue
        self.locked = False

        # create rectangle
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline="")

        # label for hex code
        self.label = tk.Label(parent_frame, text=self.color, font=("Arial", 12), bg="lightgray")
        self.label.pack()

        # lock/unlock button
        self.lock_btn = tk.Button(parent_frame, text="🔓", width=4, command=self.toggle_lock)
        self.lock_btn.pack(pady=2)

        # click label to copy color
        self.label.bind("<Button-1>", lambda e: pyperclip.copy(self.color))

    def toggle_lock(self):
        self.locked = not self.locked
        self.lock_btn.config(text="🔒" if self.locked else "🔓")

    def change_color(self):
        if not self.locked:
            self.color = random_color(self.color)
            canvas.itemconfig(self.rect, fill=self.color)
            self.label.config(text=self.color)
            pyperclip.copy(self.color)  # copy last changed color


# FRAME for labels & lock buttons
bottom_frame = tk.Frame(root, bg="lightgray")
bottom_frame.pack(fill="x", pady=10)

# divide into 4 equal columns
blocks = []
rect_width = screenwidth // 4
for i in range(4):
    x1 = i * rect_width + 10
    x2 = (i + 1) * rect_width - 10

    # subframe under each rectangle
    subframe = tk.Frame(bottom_frame, bg="lightgray")
    subframe.pack(side="left", expand=True, fill="both")

    block = ColorBlock(x1, 50, x2, screenheight - 150, subframe)
    blocks.append(block)


def change_all_colors():
    for block in blocks:
        block.change_color()


# main button
btn = tk.Button(root, text="Change Colors", command=change_all_colors, font=("Arial", 14))
btn.pack(pady=10)

root.mainloop()
