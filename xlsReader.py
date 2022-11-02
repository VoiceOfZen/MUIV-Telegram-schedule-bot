import xlrd

book = xlrd.open_workbook('timetable.xls')
sheet = book.sheet_by_index(2)

sheetNames = book.sheet_names()
print(sheetNames)

a = 16
b = 6

print(sheet.cell_value(rowx=a, colx=b), xlrd.cellname(rowx=a, colx=b))

