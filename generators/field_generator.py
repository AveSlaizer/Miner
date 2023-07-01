from random import randint
from typing import List, Tuple
from .field_cell import FieldCell


class FieldGenerator:

    def __init__(self, rows: int, columns: int, mines_qty: int):
        self.__rows = self.__field_side_validator(rows)
        self.__columns = self.__field_side_validator(columns)
        self.__mines_qty = self.__mine_quantity_validator(mines_qty)
        self.__field = self.__make_field()

    def info(self):
        print(f"Поле {self.__rows} рядов на {self.__columns} столбцов, {self.__mines_qty} мин.")

    @staticmethod
    def __field_side_validator(value: int):
        if not isinstance(value, int):
            raise ValueError(f"Недопустимый тип данных '{value.__class__.__name__}'. Ожидался 'int'.")
        if value < 2:
            raise ValueError(f"Недопустимое значение стороны поля: '{value}'. Ожидалось число больше, чем '2'.")
        return value

    def __mine_quantity_validator(self, mines_qty: int):
        if not isinstance(mines_qty, int):
            raise ValueError(f"Недопустимый тип данных '{mines_qty.__class__.__name__}'. Ожидался 'int'.")
        if not 0 < mines_qty <= self.__rows * self.__columns:
            raise ValueError(f"Недопустимое количество мин: '{mines_qty}'. "
                             f"Ожидалось число от '1' до '{self.__rows * self.__columns}'.")
        return mines_qty

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    @property
    def mines_qty(self):
        return self.__mines_qty

    @property
    def field(self):
        return self.__field

    def __get_mine_coordinates_tpl(self) -> Tuple[Tuple[int, int], ...]:
        """
        Возвращает кортеж с уникальными координатами мин в виде (column, row)
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

    def __empty_field_generator(self) -> List[List[FieldCell]]:
        """
        Возвращает поле rows рядов, column столбцов с пустыми ячейками FieldCell
        :return:
                List[List[FieldCell]]
        """
        return [[FieldCell(column=c, row=r) for c in range(self.__columns)] for r in range(self.__rows)]

    def __make_field(self) -> List[List[FieldCell]]:
        """
        Возвращает поле с расставленными минами и подсказками
        :return:
                field: (List[List[FieldCell]]) Поле
        """
        mine_coordinates = self.__get_mine_coordinates_tpl()
        field = self.__empty_field_generator()
        for coord in mine_coordinates:
            r = coord[0]  # Row
            c = coord[1]  # Column
            field[c][r].set_mine()
            for k in range(c - 1, c + 2):
                for l in range(r - 1, r + 2):
                    if 0 <= k < self.__rows and 0 <= l < self.__columns and not field[k][l].is_mine():
                        field[k][l].increase_value()
        return field

    def print_field(self) -> None:
        """
        Печатает в консоль поле с минами и подсказками
        """
        for row in self.__field:
            for cell in row:
                print(cell, end="  ")
            print()
