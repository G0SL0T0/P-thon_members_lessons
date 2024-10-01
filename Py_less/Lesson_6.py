def upper_case(s):
    if s.strip() == "":
        print("Ошибка")
    else:
        return s.upper()
    
def main():
    user_input = input("Ввод: ")
    upper_string = upper_case(user_input)
    print(upper_string)

if __name__ == "__main__":
    main()