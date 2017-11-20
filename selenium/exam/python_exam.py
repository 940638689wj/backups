'''
要求：将所有实现写成函数的形式，通过调用函数验证对错
以下为完整示例：

题目：给定数组，输出所有元素
'''

# 函数实现：
# def show_list(target_list):
# 	for target in target_list:
# 		print(target)

# # 调用函数，验证对错：
# str_list = ['a','b','c']
# show_list(str_list) # 控制台按顺序输出a b c即证明函数实现正确





#以下为测试题正文


'''
1、将数组内容倒序输出

例：str_list1 = ['a','b','c','d']
	function_name(str_list1)，输出['d','c','b','a']
'''

# def show_list(str_list):
	
# 	for x in range(0,len(str_list))[::-1]:
		
# 		print(str_list[x])

# 	# print(str_list)

# str_list1 = ['a','b','c','d']
# show_list(str_list1)

def function_list(str_list):
	new_str_list = []
	for x in range(0,len(str_list)):
		new_str_list.append(str_list[len(str_list) - 1 - x])
	print(new_str_list)


str_list1 = ['a','b','c','d']
function_list(str_list1)


'''
2、根据给定的分数，输出对应的评级，
   90~100输出A，80~90输出B，70~80输出C，60~70输出D，60以下输出E，
   给定的分数大于100或小于0时输出"分数错误"
提示：与js不同，python的判断中，多个条件的与、或关系不使用&&、||符号，应使用and、or

例：score = 78
	function_name(score)，输出C
# '''
def print_score(score):
	if score > 100 or score < 0:
		print('分数错误')
	elif score < 60:
		print('E')
	elif score >=60 and score <70:
		print('D')
	elif score >=70 and score <80:
		print('C')
	elif score >=80 and score <90:
		print('B')
	elif score >=90 and score <=100:
		print('A')

score = 78
print_score(score)


'''
3、给定一个数字数组，输出其中第三大的数

例：num_list = [52, 16, 78, 21, 35]
	function_name(num_list)，输出35
'''

def sort_list(num_list):
	for y in range(0, len(num_list) - 1):
		for x in range(0, len(num_list) - 1 - y):
			if num_list[x] > num_list[x + 1]:
				t = num_list[x]
				num_list[x] = num_list[x + 1]
				num_list[x + 1] = t


	print(num_list[2])

num_li = [52, 16, 78, 21, 35]
sort_list(num_li)


# num_list = [112,63,21,6,84,12,7,23]
# second_max_num = 0 #84
# third_max_num = 0 #84
# max_num = 0 # 112
# for x in num_list:
# 	if x > max_num:
# 		third_max_num = second_max_num
# 		second_max_num = max_num
# 		max_num = x
# 	else:
# 		if x > second_max_num:
# 			third_max_num = second_max_num
# 			second_max_num = x
# 		else:
# 			if x > third_max_num:
# 				third_max_num = x

# print(third_max_num)
# print(second_max_num)
# print(max_num)



'''
4、输出一个九九乘法表
不用粟子吧-_-||
'''

for x in range(1,10):
	num_str = ''
	for j in range (1,x+1):
		# print()
		num_str += str(j) + '*' + str(x) + '=' + str(x * j) + ' '

	print(num_str)



'''
5、给定一个任意位数的数字，输出该数字的位数，并逆序打印该数字

例：num = 5217，输出"4 7125"
	num = 16429，输出"5 92461"
'''

def upside_down(num1):
	num_len=0 #3
	result=0 # 4320
	while num1>0:
		c = num1%10
		result = (c+result)*10
		num1=num1//10
		num_len = num_len+1

	result=result//10
	print(num_len)
	print(result)

num1=12345
# upside_down(num1)

# s = '89897'
# print (s[::-1])
# print(len(s)) 



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
# cut2(str_list, option)