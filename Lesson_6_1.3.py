import random

user_input=input("Введите число от 0 до 10: ")
if user_input == random.randint(0,11):
    print("Ура, вам улыбнулась удача")
else:
    if user_input != 1 or user_input != 2 or user_input != 0 or user_input != 3 or user_input != 4 or user_input != 5 or user_input != 6 or user_input != 7 or user_input != 8 or user_input != 9 or user_input != 10:
        print ("ТЫ кто такой, чтобы перечить программе? Исправился, бегом!")
        user_input=input("Сейчас нормально введи число от 0 до 10: ")
        if user_input == random.randint(0,11):
            print("Ты везунчик, смог выйграть)")
        else:
            if user_input != 0 or user_input != 1 or user_input != 2 or user_input !=3 or user_input !=4 or user_input !=5 or user_input !=6 or user_input !=7 or user_input !=8 or user_input !=9 or user_input !=10:
                print("Ты опять?")
    else:
        print("Увы не победил")
while True:
    user_input=input("Введи число от 0 до 1: ")
    if user_input == random.randint(0,11):
        print("Победа)")
        print("Возврат в базовый каталог . . . ")
    else:
        if user_input != 0 or user_input !=1 or user_input !=2 or user_input !=3 or user_input !=4 or user_input !=5 or user_input !=6 or user_input !=7 or user_input !=8 or user_input !=9 or user_input !=10:
            print("Повтори запрос:")
        else:
            print("Увы, проигыш")
