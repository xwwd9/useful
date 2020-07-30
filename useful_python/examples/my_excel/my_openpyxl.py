from openpyxl import load_workbook


def read_line():
    wb = load_workbook("../../examples_jupyter/docs/demo.xlsx")
    ws = wb.active
    for row in ws.rows:
        for cell in row:
            print(cell.value)




if __name__ == "__main__":

    read_line()










