import re

def task1():
    text = input("Введите текст: ")
    sentences = re.split(r'(?<=[.!?])\s*', text)
    for sentence in sentences:
        print(sentence)

#task1()

def task2():
    text = input("Введите текст: ")
    pattern = r'\b(редиск\w*|нехорош\w+\s+человек\w*)\b'
    replaced = re.sub(pattern, '*давайте жить дружно*', text, flags=re.IGNORECASE)
    print(f"Результат замены: {replaced}")

#task2()

def task3():
    text = input("Введите текст для поиска дат: ")
    pattern = r'(?<!\d)(0?[1-9]|[12]\d|3[01])\.(0?[1-9]|1[0-2])\.(\d{2}|\d{4})(?!\d)'
    dates = re.findall(pattern, text)
    print("Найденные даты: ")
    for date in dates:
        print('.'.join(date))

#task3()

def task4():
    password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$')
    while True:
        password = input("Введите пароль: ")
        if password_pattern.search(password):
            print("Пароль надежный!")
            break
        print("Пароль не соответствует требованиям. Попробуйте снова.")

task4()