from random import randint
from typing import List
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

    @staticmethod
    def get_empty_pole(columns: int, rows: int) -> List[List[FieldCell]]:
        """
        Возвращает двумерный список widht x height заполненный нулями (пустое поле)

        :param columns (int): Ширина
        :param rows (int): Высота
        :return:
                List[List[int]]: Двумерный список из объектов класса FieldCell
        """
        return [[FieldCell(row = j, column = i) for i in range(columns)] for j in range(rows)]
