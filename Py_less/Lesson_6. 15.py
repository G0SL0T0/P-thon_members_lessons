import random

def lock_user_input ():
    user_input=input("Введи цифры который нужно защищать: ")
    print("")
    user_input_int=user_input

def lock_user_output ():
    user_input_int=00000
    print("Данные которые были защищены: ", user_input_int)

while True:
    print("Вас приветствует программа защиты данных.")
    input_user_command=input("Что бы вы хотели сделать: int - вести данные для записи, out - показать запись прошедшие защитные функции. ")
    if input_user_command == "int":
        lock_user_input()
        input_user_input=input()
    elif input_user_command == "out":
        lock_user_output()
        input_user_input=input()
    else:
        print("Повторите запрос. Я вас не понял.")
        input_user_input=input()
        