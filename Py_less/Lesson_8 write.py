# Демонстрация команд взаимодействия с файлами в Python

# 1. Открытие файла
def open_file():
    try:
        file = open("example.txt", "r")
        print("Файл открыт в режиме чтения")
        file.close()
    except FileNotFoundError:
        print("Файл не найден")

# 2. Режимы открытия файла
def open_modes():
    print("Режимы открытия файла:")
    print("r - режим чтения (по умолчанию)")
    print("w - режим записи (удаляет содержимое файла, если он существует)")
    print("a - режим добавления (добавляет содержимое в конец файла)")
    print("x - режим создания файла (выбрасывает исключение, если файл уже существует)")
    print("b - режим бинарного файла (используется для работы с файлами, содержащими бинарные данные)")
    print("t - режим текстового файла (по умолчанию)")
    print("+ - режим чтения и записи")

# 3. Чтение из файла
def read_file():
    try:
        file = open("example.txt", "r")
        content = file.read()
        print("Содержимое файла:")
        print(content)
        file.close()
    except FileNotFoundError:
        print("Файл не найден")

# 4. Запись в файл
def write_file():
    file = open("example.txt", "w")
    file.write("Hello, world!")
    print("Записано в файл: Hello, world!")
    file.close()

# 5. Закрытие файла
def close_file():
    try:
        file = open("example.txt", "r")
        file.close()
        print("Файл закрыт")
    except FileNotFoundError:
        print("Файл не найден")

# 6. Контекстный менеджер
def context_manager():
    with open("example.txt", "r") as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)

# 7. Чтение и запись построчно
def read_write_lines():
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())

    with open("example.txt", "w") as file:
        lines = ["Hello, world!", "This is an example."]
        file.writelines(lines)

# 8. Чтение и запись в бинарном режиме
def read_write_binary():
    with open("example.bin", "rb") as file:
        data = file.read()
        print("Бинарные данные:")
        print(data)

    with open("example.bin", "wb") as file:
        file.write(b"Hello, world!")

# Команды: 
open_file()
open_modes()
read_file()
write_file()
close_file()
context_manager()
read_write_lines()
read_write_binary()
