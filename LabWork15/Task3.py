import tkinter as tk

def update_coords(event):
    label.config(text=f"Координаты мыши: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Координаты мыши")

label = tk.Label(root, text="Координаты мыши: ")
label.pack(fill=tk.BOTH, expand=True)

root.bind('<Motion>', update_coords)

root.mainloop()