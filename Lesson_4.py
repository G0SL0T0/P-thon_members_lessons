def sort_numbers(numbers):
    try:
        numbers = numbers.split(',')
        numbers = [int(x) for x in numbers]
        numbers.sort()
        return numbers
    except ValueError:
        return "Ошибка!"

def main():
    user_input = input("Введите список чисел через запятую: ")
    if user_input.strip() == "":
        print("Ошибка")
    else:
        sorted_numbers = sort_numbers(user_input)
        print(sorted_numbers)

if __name__ == "__main__":
    main()