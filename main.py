from generators.field_cell import FieldCell

def execute_application():
    cell = FieldCell(row=1, column=2)

    print(cell)
    cell.info()
    cell.increase_value()
    cell.increase_value()
    cell.increase_value()
    cell.info()



if __name__ == "__main__":
    execute_application()
