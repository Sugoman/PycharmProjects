import tkinter as tk
from tkinter import filedialog

def save_file(event=None):
    text_content = text.get("1.0", tk.END)
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if filepath:
        with open(filepath, 'w') as file:
            file.write(text_content)

root = tk.Tk()
root.title("Сохранение текста")

text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack()

root.bind('<Control-s>', save_file)
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()