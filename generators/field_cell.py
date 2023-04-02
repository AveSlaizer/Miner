class FieldCell:

    def __init__(self, value: int = None, row: int = None, column: int = None, status: str = None):
        self.__value = value
        self.__row = row
        self.__column = column
        self.__status = status

    def __str__(self):
        return f"{self.__value}"

    def info(self):
        print(f"Значение: {self.__value}\n"
              f"Адресс: строка {self.__row} столбец {self.__column}\n"
              f"Статус: {self.__status}")