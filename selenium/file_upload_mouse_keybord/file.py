with open('io_test.txt') as f:
	print(f.read())

with open('io_test.txt', 'w') as f:
	f.write('hello')


# import xlrd

# data = xlrd.open_workbook('D:\dir\file.xlsx')
# table = data.sheets()[0]
# row = table.row_values(0)
# col = table.col_values(0)
# point = table.cell(1,1).value
# print(row)
# print(col)
# print(point)

# data = xlrd.open_workbook('file.xlsx')
# table = data.sheets()[0]
# print(table.row_values(0))
# print(table.col_values(0))

try:
	f = open('xxx')
	text = f.read()
	text += 1
except Exception as e:
	raise e
finally:
	f.close()
	