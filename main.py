from generators.field_cell import FieldCell
from generators.field_generator import FieldGenerator


def execute_application():
    field = FieldGenerator(15, 10, 38).full_made_field()

    FieldGenerator.print_field(field)


if __name__ == "__main__":
    execute_application()
