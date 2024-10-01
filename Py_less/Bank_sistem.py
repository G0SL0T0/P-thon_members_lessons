class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"Внесение успешно! Ваш новый баланс: {self.balance}")
        else:
            print("Недействительная сумма для внесения.")
    
    def withdraw(self, amount):
        if 0<amount <= self.balance:
            self.balance-=amount
            print(f"Сняятие успешно! Ваш новый баланс: {self.balance}")
        elif amount <= 0:
            print("Недействительная сумма для снятия.")
        else:
            print("Недостаточный баланс для снятия.")

    def check_balance(self):
        print(f"Ваш текущий баланс: {self.balance}")

def main():
    print("Добро пожаловать в банковскую систему!")
    exit_while_main=0

    while exit_while_main == 0:
        print("1. Создать счет")
        print("2. Внести деньги")
        print("3. Снять деньги")
        print("4. Проверить баланс")
        print("5. Выйти")

        choice = int(input("Введите ваш выбор: "))
        if  choice == 1:
            account_holder = input("Введите ваше имя: ")
            account_number = input("Введите номер счета: ")
            account= BankAccount(account_number, account_holder)
            print("Счет создан успешно!")
        elif choice == 2:
            if 'account' in locals():
                amount = int(input("Введите сумму для внесения: "))
                account.deposit(amount)
            else:
                print("Сначала создайте счет!")
        elif choice == 3:
            if 'account' in locals():
                amount = int(input("Введите сумму для снятия: "))
                account.withdraw(amount)
            else:
                print("Сначала создайте счет!")
        elif choice == 4:
            if 'account' in locals():
                account.check_balance()
            else:
                print("Сначала создайте счет!")
        elif choice == 5:
            print("До свидания!")
            exit_while_main+=1
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
