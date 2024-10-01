import uuid

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = " ".join([str(uuid.uuid4()).replace("-", "")[:4], str(uuid.uuid4()).replace("-", "")[4:8], str(uuid.uuid4()).replace("-", "")[8:12], str(uuid.uuid4()).replace("-", "")[12:16]])
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесение успешно! Ваш новый баланс: {self.format_balance()}")
        else:
            print("Недействительная сумма для внесения.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Сняятие успешно! Ваш новый баланс: {self.format_balance()}")
        elif amount <= 0:
            print("Недействительная сумма для снятия.")
        else:
            print("Недостаточный баланс для снятия.")

    def check_balance(self):
        print(f"Ваш текущий баланс: {self.format_balance()}")

    def format_balance(self):
        return "{:,} руб.".format(self.balance).replace(",", " ")
    
def save_account_to_file(account):
    with open("account.txt","a") as f:
        f.write(f"{account.account_number},{account.account_holder},{account.balance}\n")

def load_account_from_file():
    accounts ={}
    try:
        with open("accounts.txt", "r") as f:
            for line in f:
                account_number, account_holder, balance = line.strip().split(",")
                accounts[account_number] = BankAccount(account_holder, int(balance))
    except FileNotFoundError:
        pass
    return accounts


def main():
    print("Добро пожаловать в банковскую систему!")
    exit_while_main=0
    accounts = load_account_from_file()

    while exit_while_main == 0:
        print("1. Создать счет")
        print("2. Внести деньги")
        print("3. Снять деньги")
        print("4. Проверить баланс")
        print("5. Выйти")

        choice = int(input("Введите ваш выбор: "))
        if choice == 1:
            account_holder = input("Введите ваше имя: ")
            account = BankAccount(account_holder, 0)
            print(f"Счет создан успешно! Номер счета: {account.account_number}")
            save_account_to_file(account)
            accounts[account.account_number] = account
        elif choice == 2:
            account_number = input("Введите номер счета: ")
            if account_number in accounts:
                amount = int(input("Введите сумму для внесения: "))
                accounts[account_number].deposit(amount)
            else:
                print("Счет не найден!")
        elif choice == 3:
            account_number = input("Введите номер счета: ")
            if account_number in accounts:
                amount = int(input("Введите сумму для снятия: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Счет не найден!")
        elif choice == 4:
            account_number = input("Введите номер счета: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Счет не найден!")
        elif choice == 5:
            print("До свидания!")
            exit_while_main += 1
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
