"""
Домашнее задание 3. Задание 1.
Три функции для математических вычислений:
 1) факториал числа,
 2) наибольшее число из трёх (аргумент — кортеж),
 3) площадь прямоугольного треугольника по двум катетам.
"""


def factorial(n: int) -> int:
    """Возвращает факториал натурального числа n (n!)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал определён только для целых n >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def max_of_three(numbers: tuple) -> float:
    """Возвращает наибольшее число из кортежа из трёх чисел."""
    if len(numbers) != 3:
        raise ValueError("Нужен кортеж ровно из трёх чисел")
    a, b, c = numbers
    biggest = a
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest


def right_triangle_area(leg_a: float, leg_b: float) -> float:
    """Площадь прямоугольного треугольника по двум катетам."""
    if leg_a <= 0 or leg_b <= 0:
        raise ValueError("Катеты должны быть положительными")
    return leg_a * leg_b / 2


# --- Демонстрация работы ---
if __name__ == "__main__":
    print("factorial(5) =", factorial(5))          # 120
    print("factorial(0) =", factorial(0))          # 1
    print("factorial(10) =", factorial(10))        # 3628800

    print("max_of_three((7, 15, 3)) =", max_of_three((7, 15, 3)))     # 15
    print("max_of_three((-1, -5, -2)) =", max_of_three((-1, -5, -2))) # -1

    print("right_triangle_area(3, 4) =", right_triangle_area(3, 4))   # 6.0
    print("right_triangle_area(5, 12) =", right_triangle_area(5, 12)) # 30.0
