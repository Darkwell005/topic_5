fruits: dict = {
    'яблоко': 50,
    'банан': 30,
    'груша': 40,
    'апельсин': 35
}

print("Список фруктов и их цены:")
print(fruits)

user_input: str = input('Выберите фрукт из списка: ')

price: int = fruits[user_input]
print('Цена', user_input, '-', price)

# ===================== №2 ==========================

fruit_values: list = [
    ('яблоко', 50),
    ('банан', 30),
    ('груша', 40),
    ('апельсин', 35)
]

fruits_2: dict = dict(fruit_values)

print("Список фруктов и их цены:")
print(fruits_2)

user_input: str = input('Выберите фрукт из списка: ')

price: int = fruits_2[user_input]
print('Цена', user_input, '-', price)
