from generators.field_cell import FieldCell
from generators.field_generator import FieldGenerator

def execute_application():
    field = FieldGenerator(10, 10, 8)
    #print(field)

    mines = field.get_mine_coordinates()

    print(mines)




if __name__ == "__main__":
    execute_application()
