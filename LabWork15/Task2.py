import tkinter as tk

def on_entry_click(event):
    widget = event.widget
    for name, entry in entries.items():
        if entry == widget:
            label.config(text=f"Активное поле: {name}")

def on_right_click(event):
    widget = event.widget
    for name, entry in entries.items():
        if entry == widget:
            print(f"Правая кнопка на поле: {name}")

root = tk.Tk()
root.title("Три поля ввода")

entries = {
    "Поле 1": tk.Entry(root),
    "Поле 2": tk.Entry(root),
    "Поле 3": tk.Entry(root)
}

label = tk.Label(root, text="Активное поле: ")
label.pack()

for entry in entries.values():
    entry.pack(pady=5)

root.bind_class('Entry', '<Button-1>', on_entry_click)
root.bind_class('Entry', '<Button-3>', on_right_click)

root.mainloop()