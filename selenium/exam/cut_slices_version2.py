def cut_slices(target_list, options):
	# 如果b未赋值 则设置为数组长度
	start = options['start'] if 'start' in options else 0
	end = options['end'] if 'end' in options else len(target_list)
	step = options['step'] if 'step' in options else 1

	result_list = [] # 切片后的数组
	step_count = 0 # 步数

	for x in range(start, end):
		# 防止下标越界
		if(x < len(target_list) and step_count % step == 0):
			result_list.append(target_list[x])

		step_count += 1

	print(result_list)


target_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

options = {
	'step': 2
}
cut_slices(target_list, options)

options = {
	'end': 3,
}
cut_slices(target_list, options)

options = {
	'start': 2,
	'end': 5,
	'step': 2
}
cut_slices(target_list, options)

