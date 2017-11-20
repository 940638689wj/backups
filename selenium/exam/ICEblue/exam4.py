for x in range(1,10):
	num_str = ''
	for j in range (1,x+1):
		# print()
		num_str += str(j) + '*' + str(x) + '=' + str(x * j) + ' '

	print(num_str)
			 