import random

num=0
exit=0
while exit == 0:
    sum = random.randint(0,11)
    if sum % 2 == 0:
        num+=sum
    for i in range(1,11):
        if num % 5 == 0:
            print ("Удача!")
        if sum % 3 == 0 and sum % 2 ==0:
            exit = 1
            print ("Великая удача!")


