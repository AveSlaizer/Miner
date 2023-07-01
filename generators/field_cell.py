class FieldCell:

    def __init__(self, value: int = 0, row: int = None, column: int = None, status: bool = True):
        self.__value = value
        self.__row = row
        self.__column = column
        self.__status = status

    def __str__(self):
        if self.__value == -1:
            return "*"
        return f"{self.__value}"

    def info(self):
        print(f"Значение: {self.__value}\n"
              f"Адресс: строка {self.__row} столбец {self.__column}\n"
              f"Статус: {self.status}")

    def set_mine(self):
        if not self.is_mine():
            self.__value = -1
        else:
            raise ValueError("Ошибка! В ячейке уже установлена мина")

    def is_mine(self):
        return self.__value == -1

    def increase_value(self):
        if self.__value >= 0:
            self.__value += 1
        else:
            raise ValueError("В ячейке установлена мина")

    def print_status(self):
        if self.__status:
            print("Закр.")
        else:
            print("Откр.")

    def open_cell(self):
        self.__status = False

    @property
    def value(self):
        return self.__value

    @property
    def row(self):
        return self.__row

    @property
    def column(self):
        return self.__column

    @property
    def status(self):
        return self.__status
