"""
Домашнее задание 1. Задание 1.
Работа с переменными, консольный ввод/вывод (input, print)
и наблюдение за адресами объектов в памяти через id().
"""

# --- Создаём несколько переменных разных типов и выводим их ---
name = "Максим"
age = 25
height = 1.82
is_student = True

print("Имя:", name)
print("Возраст:", age)
print("Рост (м):", height)
print("Студент?", is_student)

# --- Запрашиваем данные у пользователя ---
user_name = input("Введите ваше имя: ")
user_city = input("Введите ваш город: ")
user_number_str = input("Введите любое число: ")

print()
print("Вы ввели:")
print("  Имя :", user_name)
print("  Город:", user_city)
print("  Число:", user_number_str)

# --- Наблюдаем за id() объектов ---
# В Python числа, строки, кортежи — неизменяемые (immutable).
# При «изменении» такой переменной создаётся новый объект и id() меняется.
# Списки, словари, множества — изменяемые (mutable): id() сохраняется.

print()
print("=== Неизменяемые объекты: int ===")
x = 10
print("x =", x, " id(x) =", id(x))
x = x + 1          # создаётся новый int — id меняется
print("x =", x, " id(x) =", id(x))

print()
print("=== Неизменяемые объекты: str ===")
s = "hello"
print("s =", s, " id(s) =", id(s))
s = s + " world"   # новая строка — новый id
print("s =", s, " id(s) =", id(s))

print()
print("=== Изменяемые объекты: list ===")
lst = [1, 2, 3]
print("lst =", lst, " id(lst) =", id(lst))
lst.append(4)      # список меняется «на месте» — id сохраняется
print("lst =", lst, " id(lst) =", id(lst))

print()
print("=== Изменяемые объекты: dict ===")
d = {"a": 1}
print("d =", d, " id(d) =", id(d))
d["b"] = 2         # словарь меняется «на месте» — id сохраняется
print("d =", d, " id(d) =", id(d))
