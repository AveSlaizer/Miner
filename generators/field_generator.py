from random import randint
from typing import List, Tuple
from .field_cell import FieldCell


class FieldGenerator:

    def __init__(self, rows: int = None, columns: int = None, mines_qty: int = None):
        self.__rows = rows
        self.__columns = columns
        self.__mines_qty = mines_qty

    def __str__(self):
        return f"Поле {self.__rows} рядов на {self.__columns} столбцов, {self.__mines_qty} мин."

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    @property
    def mines_qty(self):
        return self.__mines_qty

    def get_mine_coordinates_tpl(self) -> Tuple[Tuple[int, int], ...]:
        """
        Возвращает кортеж с уникальными координатами мин в виде (x, y)

        :return:
                Tuple[Tuple[int, int], ...]: Кортеж уникальных кортежей с координатами мин
        """
        mine_tpl = []
        temp_count = 0
        while temp_count < self.__mines_qty:
            mine_col = randint(0, self.__columns - 1)
            mine_row = randint(0, self.__rows - 1)
            mine_coordinate = (mine_col, mine_row)
            if mine_coordinate not in mine_tpl:
                mine_tpl.append(mine_coordinate)
                temp_count += 1
        return tuple(mine_tpl)

    def get_field_with_mines(self) -> List[List[FieldCell]]:
        """
        Возвращает поле с расставленными минами

        :return:
        """
        mine_coordinates = self.get_mine_coordinates_tpl()
        field = []
        for j in range(self.__rows):
            temp_list = []
            for i in range(self.__columns):
                cell = FieldCell(row=j, column=i)
                if (i, j) in mine_coordinates:
                    cell.set_mine()
                temp_list.append(cell)
            field.append(temp_list)
        return field

    def full_made_field(self) -> List[List[FieldCell]]:
        """
        Возвращает поле с подсказками вокруг мин

        :return:
                List[List[int]]: Поле с минами и подсказками
        """

        field = self.get_field_with_mines()

        # Ищем соседние с миной ячейки и генерируем там числа-подсказки
        rows = len(field)
        for i in range(rows):
            columns = len(field[i])
            for j in range(columns):
                if field[i][j].is_mine():
                    temp_i = i
                    temp_j = j
                    # Идем по диапазонам от -1 до 1 от текущих значений i и j
                    for k in range(temp_i - 1, temp_i + 2):
                        for l in range(temp_j - 1, temp_j + 2):
                            # Проверяем позицию ячейки, содержание в ней мины
                            if 0 <= k < rows and 0 <= l < columns and not field[k][l].is_mine():
                                field[k][l].increase_value()

        return field
