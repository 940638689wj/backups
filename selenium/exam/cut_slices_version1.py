def cut_slices(target_list, a=0, b='', c=1):
	# 如果b未赋值 则设置为数组长度
	if b == '':
		b = len(target_list)
	
	result_list = [] # 切片后的数组
	step = 0 # 步数

	for x in range(a, b):
		# 防止下标越界
		if(x < len(target_list) and step % c == 0):
			result_list.append(target_list[x])

		step += 1

	print(result_list)


target_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
cut_slices(target_list, 1, 9, 2)

