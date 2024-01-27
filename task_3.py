"""
Hw
"""


def access_element(array, index):
    """
    Получает доступ к элементу массива и обрабатывает исключение при выходе за границы.

    Parameters:
        array (list): Массив, к которому производится доступ.
        index (int): Индекс элемента, к которому нужно получить доступ.

    Returns:
        None
    """
    try:
        element = array[index]
        print(f"Значение по индексу {index}: {element}")

    except IndexError:
        print(f"Ошибка: Индекс {index} выходит за границы массива.")

def main():
    """
    Основная функция программы, в которой пользователь вводит индекс элемента массива.
    """
    my_array = [1, 2, 3, 4, 5]

    try:
        user_index = int(input("Введите индекс элемента массива: "))
        access_element(my_array, user_index)

    except ValueError:
        print("Ошибка: Введенное значение не является целым числом.")


if __name__ == "__main__":
    main()
