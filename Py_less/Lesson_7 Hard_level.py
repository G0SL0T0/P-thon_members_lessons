cars =[]

# Функция для добавления новой машины
def add_car(brand, quantity):
    cars.append({"brand": brand, "quantity": quantity})
    print(f"Машина {brand} добавлена в автосервис. Количество: {quantity}")

# Функция для удаления машины
def remove_car(brand):
    for car in cars:
        if car["brand"] == brand:
            cars.remove(car)
            print(f"Машина {brand} удалена из автосервиса.")
            return
    print(f"Машина {brand} не найдена в автосервисе.")

# Функция для вывода информации о всех машинах
def print_cars():
    print("Информация о машинах в автосервисе:")
    for car in cars:
        print(f"Марка: {car['brand']}, Количество: {car['quantity']}")

# Функция для поиска машины по марке
def find_car(brand):
    for car in cars:
        if car["brand"] == brand:
            print(f"Машина {brand} найдена в автосервисе. Количество: {car['quantity']}")
            return
    print(f"Машина {brand} не найдена в автосервисе.")

add_car("Toyota",5)
add_car("Ford",2)
add_car("Lada",6)
add_car("Honda",3)

print_cars()

remove_car("Lada")

print_cars()

find_car("Honda")

print_cars()