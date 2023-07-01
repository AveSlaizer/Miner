from generators.field_generator import FieldGenerator


def execute_application():
    field = FieldGenerator(5, 5, 5)
    field.print_field()

if __name__ == "__main__":
    execute_application()
