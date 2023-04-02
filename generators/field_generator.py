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


    def __get_mine_coordinates(self):
        pass
