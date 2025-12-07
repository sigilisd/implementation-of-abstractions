class Phone:
    def __init__(self, brand: str, model: str, price: float, color: str, storage_gb: int, is_in_stock: bool):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.storage_gb = storage_gb
        self.is_in_stock = is_in_stock

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        self.price = self.price * (1 - discount_percent / 100)

    def check_availability(self) -> str:
        if self.is_in_stock:
            return "В наличии"
        else:
            return "Нет в наличии"

    def __str__(self) -> str:
        return f"Телефон: {self.get_full_name()}, Цвет: {self.color}, Память: {self.storage_gb}GB, Цена: {self.price} руб., {self.check_availability()}"


# Создание экземпляров класса Phone
phone1 = Phone("Apple", "iPhone 15", 89990.0, "Черный", 128, True)
phone2 = Phone("Samsung", "Galaxy S24", 79990.0, "Синий", 256, True)
phone3 = Phone("Xiaomi", "Redmi Note 12", 19990.0, "Белый", 64, False)
phone4 = Phone("Google", "Pixel 8", 59990.0, "Серый", 128, True)

# Демонстрация работы методов
print("=== Демонстрация работы класса Phone ===\n")

print("Телефон 1:")
print(phone1)
print(f"Полное название: {phone1.get_full_name()}")
print(f"До скидки: {phone1.price} руб.")
phone1.apply_discount(10)
print(f"После скидки 10%: {phone1.price} руб.")
print(f"Наличие: {phone1.check_availability()}")
print()

print("Телефон 2:")
print(phone2)
print(f"Полное название: {phone2.get_full_name()}")
print(f"До скидки: {phone2.price} руб.")
phone2.apply_discount(15)
print(f"После скидки 15%: {phone2.price} руб.")
print(f"Наличие: {phone2.check_availability()}")
print()

print("Телефон 3:")
print(phone3)
print(f"Полное название: {phone3.get_full_name()}")
print(f"До скидки: {phone3.price} руб.")
phone3.apply_discount(5)
print(f"После скидки 5%: {phone3.price} руб.")
print(f"Наличие: {phone3.check_availability()}")
print()

print("Телефон 4:")
print(phone4)
print(f"Полное название: {phone4.get_full_name()}")
print(f"До скидки: {phone4.price} руб.")
phone4.apply_discount(20)
print(f"После скидки 20%: {phone4.price} руб.")
print(f"Наличие: {phone4.check_availability()}")

