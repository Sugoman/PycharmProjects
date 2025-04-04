import tkinter as tk

def on_key_press(event):
    if event.char:
        label.config(text=f"Нажатая клавиша: {event.char}")

root = tk.Tk()
root.title("Нажатые клавиши")
root.focus_set()

label = tk.Label(root, text="Нажатые клавиши: ")
label.pack(fill=tk.BOTH, expand=True)

root.bind('<KeyPress>', on_key_press)

root.mainloop()