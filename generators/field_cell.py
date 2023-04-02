class FieldCell:

    def __init__(self, value: int = 0, row: int = None, column: int = None, status: bool = True):
        self.__value = value
        self.__row = row
        self.__column = column
        self.__status = status

    def __str__(self):
        return f"{self.__value}"

    def info(self):
        print(f"Значение: {self.__value}\n"
              f"Адресс: строка {self.__row} столбец {self.__column}\n"
              f"Статус: {self.status}")

    def set_mine(self):
        if self.__value == 0:
            self.__value = -1
        raise Exception("Для установки мины значение ячейки должно быть равным 0")

    def increase_value(self):
        if self.__value >= 0:
            self.__value += 1
        else:
            raise Exception("В ячейке установлена мина")

    @property
    def value(self):
        return self.__value

    @property
    def row(self):
        return self.row

    @row.setter
    def row(self, row: int):
        self.__row = row

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

    @property
    def status(self):
        if self.__status:
            return "Закр"
        return "Откр"

    def change_status(self):
        if self.__status:
            self.__status = False