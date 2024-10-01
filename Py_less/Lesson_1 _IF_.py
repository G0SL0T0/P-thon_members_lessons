import random

def int_random(number_random):
    return random.randint(0,11)

number_random =0
exit_while_1=0
while exit_while_1 == 0:
    number_random = int(input("Введите число: "))
    if number_random == 5:
        print("Победа")
        exit_while_1+=1
    elif number_random == 6:
        print("Цифра 6")
        exit_while_1+=1
    elif number_random == 7:
        print("Цифра 7")
        exit_while_1+=1
    elif number_random == 8:
        print("Цифра 8")
        exit_while_1+=1
    else:
        print("Проиграл")
        user_input = int( input("Продолжить? 1 - да, 2 - закончить."))
        if user_input == 1:
            exit_while_1=0
        elif user_input == 2:
            exit_while_1=1