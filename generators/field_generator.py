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


    def get_empty_field(self) -> List[List[FieldCell]]:
        """
        Возвращает двумерный список widht x height заполненный нулями (пустое поле)

        :param columns (int): Ширина
        :param rows (int): Высота
        :return:
                List[List[int]]: Двумерный список из объектов класса FieldCell
        """
        return [[FieldCell(row = j, column = i) for i in range(self.__columns)] for j in range(self.rows)]


    def get_mine_coordinates(self) -> Tuple[Tuple[int, int], ...]:
        """
        Возвращает список с уникальными координтами мин в виде [x, y]

        :param quantity (int): Количество мин
        :param columns (int): Ширина
        :param rows (int): Высота
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
