numbers = [1,2,3,4,5]

print ("Масив: ")
for num in numbers:
    print(num)

numbers.append(10)
print("Массив после добавления элемента:")
print(numbers)

numbers.remove(2)
print("Массив после удаления элемента:")
print(numbers)

numbers.sort()
print("Массив после сорировки:")
print(numbers)

numbers.reverse()
print("Массив в обратном порядке:")
print(numbers)
