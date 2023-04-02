from generators.field_cell import FieldCell
from generators.field_generator import FieldGenerator


def execute_application():
    field = FieldGenerator(15, 10, 38).full_made_field()

    for row in field:
        for cell in row:
            print(cell, end="  ")
        print()


if __name__ == "__main__":
    execute_application()
