import tkinter as tk
import random
import pyperclip

root = tk.Tk()
root.title("Palette Generator")
root.configure(bg="lightgray")

screenwidth, screenheight = 800, 600

canvas = tk.Canvas(root, width=screenwidth, height=screenheight - 100, bg="lightgray", highlightthickness=0)
canvas.pack()

history = []
history_index = -1


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

        self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline="")

        self.label = tk.Label(parent_frame, text=self.color, font=("Arial", 12), bg="lightgray")
        self.label.pack()

        self.lock_btn = tk.Button(parent_frame, text="🔓", width=4, command=self.toggle_lock)
        self.lock_btn.pack(pady=2)

        self.label.bind("<Button-1>", lambda e: pyperclip.copy(self.color))

    def toggle_lock(self):
        self.locked = not self.locked
        self.lock_btn.config(text="🔒" if self.locked else "🔓")

    def change_color(self):
        if not self.locked:
            self.color = random_color(self.color)
            canvas.itemconfig(self.rect, fill=self.color)
            self.label.config(text=self.color)
            pyperclip.copy(self.color)
    def set_color(self, color):
        """Set a specific color (used for history navigation)."""
        self.color = color
        canvas.itemconfig(self.rect, fill=color)
        self.label.config(text=color)


bottom_frame = tk.Frame(root, bg="lightgray")
bottom_frame.pack(fill="x", pady=10)

blocks = []
rect_width = screenwidth // 4
for i in range(4):
    x1 = i * rect_width + 10
    x2 = (i + 1) * rect_width - 10

    subframe = tk.Frame(bottom_frame, bg="lightgray")
    subframe.pack(side="left", expand=True, fill="both")

    block = ColorBlock(x1, 50, x2, screenheight - 150, subframe)
    blocks.append(block)


def get_current_palette():
    return [block.color for block in blocks]


def apply_palette(palette):
    for block, color in zip(blocks, palette):
        block.set_color(color)


def change_all_colors():
    global history, history_index
    for block in blocks:
        block.change_color()
    if history_index != len(history) - 1:
        history = history[:history_index+1] 
    history.append(get_current_palette())
    history_index += 1


def prev_palette():
    global history_index
    if history_index > 0:
        history_index -= 1
        apply_palette(history[history_index])


def next_palette():
    global history_index
    if history_index < len(history) - 1:
        history_index += 1
        apply_palette(history[history_index])


btn_frame = tk.Frame(root, bg="lightgray")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Previous", command=prev_palette, font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Change Colors", command=change_all_colors, font=("Arial", 14)).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Next", command=next_palette, font=("Arial", 12)).grid(row=0, column=2, padx=10)

change_all_colors()

root.mainloop()
