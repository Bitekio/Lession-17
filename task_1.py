"""
Hw
"""


class ChessBoard:
    """
    Класс, представляющий шахматную доску и шахматные фигуры.
    """
    def __init__(self):
        """Инициализация шахматной доски."""
        pass

    def is_valid_square(self, square):
        """
        Проверяет, является ли клетка шахматной доски допустимой.

        Parameters:
            square (str): Координаты клетки в формате "a1", "b2", и т.д.

        Returns:
            bool: True, если клетка допустима, иначе False.
        """
        return len(square) == 2 and 'a' <= square[0] <= 'h' and '1' <= square[1] <= '8'

    def is_valid_move(self, start, end, piece):
        """
        Проверяет, может ли шахматная фигура совершить ход из одной клетки в другую за один ход.

        Parameters:
            start (str): Начальная клетка.
            end (str): Конечная клетка.
            piece (str): Тип шахматной фигуры ("ферзь" или "конь").

        Returns:
            bool: True, если ход допустим, иначе False.
        Raises:
            ValueError: Если введены некорректные данные.
        """
        try:
            if not (self.is_valid_square(start) and self.is_valid_square(end)):
                raise ValueError("Неверный формат клетки")

            start_col, start_row = ord(start[0]) - ord('a'), int(start[1])
            end_col, end_row = ord(end[0]) - ord('a'), int(end[1])

            if piece == "ферзь":
                return start_col == end_col or start_row == end_row or abs(start_col - end_col) == abs(start_row - end_row)
            if piece == "конь":
                return (
                    (abs(start_col - end_col) == 2 and abs(start_row - end_row) == 1) or
                    (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 2)
                )

            raise ValueError("Неверная шахматная фигура")

        except ValueError as e:
            print(f"Ошибка: {e}")
            return False


def main():
    """
    Проверяет возможность хода фигуры.
    """
    chessboard = ChessBoard()

    try:
        start_square = input("Введите начальную клетку (например, a1): ").lower()
        end_square = input("Введите конечную клетку (например, b2): ").lower()
        piece = input("Введите шахматную фигуру (ферзь/конь): ").lower()

        if chessboard.is_valid_move(start_square, end_square, piece):
            print(f"{piece.capitalize()} может совершить ход из {start_square} в {end_square} за один ход.")
        else:
            print(f"{piece.capitalize()} не может совершить ход из {start_square} в {end_square} за один ход.")

    except ValueError as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
