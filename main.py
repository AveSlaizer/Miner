from generators.field_cell import FieldCell
from generators.field_generator import FieldGenerator

def execute_application():
    field = FieldGenerator(15, 10, 38)
    #print(field)

    #mines = field.get_mine_coordinates_tpl()

    #print(mines)

    #field_1 = field.place_mines()

    """for row in field_1:
        for cell in row:
            print(cell, end="  ")
        print()"""

    field = field.full_made_field()

    for row in field:
        for cell in row:
            if cell == -1:
                print("*", end="  ")
            else:
                print(cell, end="  ")
        print()




if __name__ == "__main__":
    execute_application()
