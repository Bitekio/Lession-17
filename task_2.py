"""
Hw
"""


def plus_two(number):
    """
    Складывает переданное число с 2 и выводит результат.

    Parameters:
        number (int): Число, которое нужно сложить с 2.

    Returns:
        None
    """
    try:
        result = 2 + number
        print(f"Результат сложения: {result}")

    except TypeError:
        print("Ожидаемый тип данных — число!")

def main():
    """
    Основная функция программы, в которой пользователь вводит число и вызывается функция plus_two.
    """
    try:
        user_input = input("Введите число: ")
        number = int(user_input)
        plus_two(number)

    except ValueError:
        print("Ошибка: Введено некорректное число.")


if __name__ == "__main__":
    main()
