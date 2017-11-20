num = 1
try:
	num = num + 'abc'
except Exception as e:
	print('报错啦')
	# print('再展示一下原来的异常')
	raise e
finally:
	print('其他操作')

