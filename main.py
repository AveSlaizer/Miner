from generators.field_cell import FieldCell
from generators.field_generator import FieldGenerator

def execute_application():
    field = FieldGenerator(10, 10, 8)
    #print(field)

    empty_field = field.get_empty_field()

    for row in empty_field:
        for item in row:
            item.info()
            #print(item, end="  ")
        print()



if __name__ == "__main__":
    execute_application()
