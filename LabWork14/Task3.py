import tkinter as tk

def update_label(*args):
    label_text = f"{entry_var.get()}, {check_var.get()}, {radio_var.get()}"
    result_label.config(text=label_text)

root = tk.Tk()
root.title("Связанные переменные")

# Переменные
entry_var = tk.StringVar()
check_var = tk.IntVar()
radio_var = tk.StringVar(value="Option 1")

# Виджеты
tk.Entry(root, textvariable=entry_var).pack(pady=5)
entry_var.trace_add("write", update_label)

tk.Checkbutton(root, text="Флажок", variable=check_var).pack(pady=5)
check_var.trace_add("write", update_label)

tk.Radiobutton(root, text="Вариант 1", variable=radio_var, value="Option 1").pack()
tk.Radiobutton(root, text="Вариант 2", variable=radio_var, value="Option 2").pack()
radio_var.trace_add("write", update_label)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()