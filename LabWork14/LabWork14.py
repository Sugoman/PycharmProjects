import tkinter as tk

def create_auth_form():
    root = tk.Tk()
    root.title("Форма авторизации")
    root.geometry("200x300")

    # Метки
    tk.Label(root, text="Логин:").pack(pady=5)
    login_entry = tk.Entry(root)
    login_entry.pack(pady=5)

    tk.Label(root, text="Пароль:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    # Флажок
    remember_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Запомнить пароль", variable=remember_var).pack(pady=5)

    # Кнопка
    tk.Button(root, text="Авторизоваться").pack(pady=10)

    root.mainloop()

create_auth_form()