import tkinter as tk

def change_color(color):
    root.config(bg=color)

def change_size(size):
    root.geometry(size)

root = tk.Tk()
root.title("Меню с горячими клавишами")

# Создание меню
menu_bar = tk.Menu(root)

# Пункт Color
color_menu = tk.Menu(menu_bar, tearoff=0)
color_menu.add_command(label="Red", command=lambda: change_color("red"), accelerator="Ctrl+R")
color_menu.add_command(label="Green", command=lambda: change_color("green"), accelerator="Ctrl+G")
color_menu.add_command(label="Blue", command=lambda: change_color("blue"), accelerator="Ctrl+B")
menu_bar.add_cascade(label="Color", menu=color_menu)

# Пункт Size
size_menu = tk.Menu(menu_bar, tearoff=0)
size_menu.add_command(label="500x500", command=lambda: change_size("500x500"), accelerator="Ctrl+1")
size_menu.add_command(label="700x400", command=lambda: change_size("700x400"), accelerator="Ctrl+2")
menu_bar.add_cascade(label="Size", menu=size_menu)

root.config(menu=menu_bar)

# Горячие клавиши
root.bind("<Control-r>", lambda e: change_color("red"))
root.bind("<Control-g>", lambda e: change_color("green"))
root.bind("<Control-b>", lambda e: change_color("blue"))
root.bind("<Control-1>", lambda e: change_size("500x500"))
root.bind("<Control-2>", lambda e: change_size("700x400"))

root.mainloop()