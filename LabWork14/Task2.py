import tkinter as tk
from tkinter import ttk

def create_reg_form():
    root = tk.Tk()
    root.title("Форма регистрации")
    root.configure(bg="#f0f0f0")  # Серый фон

    # Логин и пароль
    tk.Label(root, text="Логин:", bg="#f0f0f0").pack(pady=5)
    login_entry = tk.Entry(root)
    login_entry.pack(pady=5)

    tk.Label(root, text="Пароль:", bg="#f0f0f0").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    # Многострочное поле
    tk.Label(root, text="О себе:", bg="#f0f0f0").pack(pady=5)
    about_text = tk.Text(root, height=5)
    about_text.pack(pady=5)

    # Переключатели для пола
    gender_var = tk.StringVar(value="male")
    tk.Label(root, text="Пол:", bg="#f0f0f0").pack()
    tk.Radiobutton(root, text="Мужской", variable=gender_var, value="male", bg="#f0f0f0").pack()
    tk.Radiobutton(root, text="Женский", variable=gender_var, value="female", bg="#f0f0f0").pack()

    # Список материков
    continents = ["Европа", "Азия", "Африка", "Северная Америка", "Южная Америка"]
    tk.Label(root, text="Материк:", bg="#f0f0f0").pack()
    continent_combobox = ttk.Combobox(root, values=continents)
    continent_combobox.pack(pady=5)

    # Кнопка
    tk.Button(root, text="Зарегистрироваться", bg="#e0e0e0").pack(pady=10)

    root.mainloop()

create_reg_form()