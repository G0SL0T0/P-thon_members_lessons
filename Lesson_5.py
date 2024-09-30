def reverse_string(s):
    if s.strip() == "":
        return "Ошибка"
    else:
        return "".join(reversed(s))
def main():
    user_input = input("")
    reversed_string = reverse_string(user_input)
    print(reversed_string)

if __name__ == "__main__":
    main()