from generators.field_generator import FieldGenerator


def execute_application():
    field = FieldGenerator(10, 10, 9).make_field()

    FieldGenerator.print_field(field)


if __name__ == "__main__":
    execute_application()
