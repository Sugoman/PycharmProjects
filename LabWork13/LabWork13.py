import xml.etree.ElementTree as ET
import wave
import struct
import math  # Добавляем импорт модуля math
import sqlite3


def read_xml(file_path):
    """Чтение XML-файла."""
    tree = ET.parse(file_path)
    root = tree.getroot()
    # Вывод структуры
    for child in root:
        print(f"Тег: {child.tag}, Аттрибуты: {child.attrib}")
        for subchild in child:
            print(f"  Подтег: {subchild.tag}, Текст: {subchild.text}")
    return tree

def modify_xml(tree, tag, new_text):
    """Изменение текста первого элемента с указанным тегом."""
    root = tree.getroot()
    for elem in root.iter(tag):
        elem.text = new_text
        break  # Изменяем только первый найденный элемент

# Пример использования
xml_tree = read_xml("24mb.xml")
modify_xml(xml_tree, "name", "Новое значение")
xml_tree.write("modified_data.xml", encoding="utf-8")

def create_wav(file_name):
    """Создание простого WAV-файла с синусоидальным сигналом."""
    sample_rate = 44100  # Частота дискретизации
    duration = 3  # Длительность в секундах
    frequency = 440  # Частота тона (Гц)

    with wave.open(file_name, 'w') as wav_file:
        wav_file.setnchannels(1)  # Моно
        wav_file.setsampwidth(2)  # 2 байта на сэмпл
        wav_file.setframerate(sample_rate)

        # Генерация сигнала
        for i in range(int(duration * sample_rate)):
            value = int(32767 * 0.5 * (1 + (i * frequency * 2 * 3.1415 / sample_rate)))
            data = struct.pack('<h', value)
            wav_file.writeframesraw(data)

def create_wav(file_name):
    sample_rate = 44100
    duration = 3
    frequency = 440

    with wave.open(file_name, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)

        for i in range(int(duration * sample_rate)):
            sample = math.sin(2 * math.pi * frequency * i / sample_rate)
            value = int(sample * 32767 * 0.8)
            data = struct.pack('<h', value)
            wav_file.writeframesraw(data)


def modify_wav(input_file, output_file):
    with wave.open(input_file, 'r') as wav_in:
        params = wav_in.getparams()
        frames = wav_in.readframes(params.nframes)

    # Распаковка данных (для 16-битных сэмплов)
    samples = struct.unpack(f'<{len(frames) // 2}h', frames)
    modified = [min(max(s * 2, -32768), 32767) for s in samples]

    with wave.open(output_file, 'w') as wav_out:
        wav_out.setparams(params)

# Пример использования
create_wav("test.wav")
modify_wav("test.wav", "louder.wav")

def sqlite_operations():
    try:
        # Подключение к базе данных (создание, если не существует)
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Создание таблицы, если она не существует
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

        # Вставка данных
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Иван', 25))
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Мария', 30))
        conn.commit()

        # Чтение данных
        print("Содержимое таблицы users:")
        for row in cursor.execute("SELECT * FROM users"):
            print(row)

        # Модификация данных
        cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, 'Иван'))
        conn.commit()

        # Удаление данных
        cursor.execute("DELETE FROM users WHERE name = ?", ('Мария',))
        conn.commit()

        print("\nПосле изменений:")
        for row in cursor.execute("SELECT * FROM users"):
            print(row)

    except sqlite3.Error as e:
        print(f"Ошибка SQLite: {e}")
    finally:
        if conn:
            conn.close()
sqlite_operations()