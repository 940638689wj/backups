'''
6.编写一个函数，实现类似python数组的切片功能
提示：使用 默认参数 或 dict类型参数

例：str_list6 = ['a','b','c','d','e','f']
	function_name(str_list6)，输出原数组，即['a','b','c','d','e','f']
	function_name(str_list6, 2)，输出['c','d','e','f']
	function_name(str_list6, 2, 4)，输出['c','d']
	function_name(str_list6, 0, 6 , 2)，输出['a','c', 'e']
'''
def cut(target_list, start=0, end='', step=1):
	if end == '':
		end = len(target_list)

	result_list = []
	# for x in range(start, end):
	# 	if x < len(target_list):
	# 		result_list.append(target_list[x])
	if end > len(target_list):
		end = len(target_list)

	step_count = 0
	for x in range(start,end):
		if step_count % step == 0:
			result_list.append(target_list[x])
		step_count += 1

	print(result_list)

str_list = ['a','b','c','d','e','f']
# cut(str_list,1 ,5 , 2)

# print(str_list[1::2])

# for x in range(1,10):
# 	x += 2
# 	print(x)






def cut2(target_list, option):
	# start = 0
	# if 'start' in option:
	# 	start = option['start']
	start = option['start'] if 'start' in option else 0
	end = option['end'] if 'end' in option else len(target_list)
	step = option['step'] if 'step' in option else 1

	result_list = []
	step_count = 0
	for x in range(start,end):
		if step_count % step == 0:
			result_list.append(target_list[x])
		step_count += 1

	print(result_list)

option = {
	'start': 2,
	'end': 5,
	'step': 1
}

str_list = ['a','b','c','d','e','f']
cut2(str_list, option)