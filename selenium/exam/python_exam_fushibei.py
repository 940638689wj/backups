'''
要求：将所有实现写成函数的形式，通过调用函数验证对错
以下为完整示例：

题目：给定数组，输出所有元素
'''

# 函数实现：
'''
def show_list(target_list):
	for target in target_list:
		print(target)


# 调用函数，验证对错：
str_list = ['a','b','c']
show_list(str_list) # 控制台按顺序输出a b c即证明函数实现正确


'''


#以下为测试题正文


'''
1、将数组内容倒序输出

例：str_list1 = ['a','b','c','d']
	function_name(str_list1)，输出['d','c','b','a']

'''
'''

str_list = ['a','b','c']

def show(str_list):
	for x in range(0, len(str_list) - 1)
		if str_list[x] > str_list[x + 1]:
				temp = str_list[x]
				str_list[x] = str_list[x + 1]
				str_list[x + 1] = temp
	print(str_list)



str_list = ['a','b','c']

'''

'''
2、根据给定的分数，输出对应的评级，
   90~100输出A，80~90输出B，70~80输出C，60~70输出D，60以下输出E，
   给定的分数大于100或小于0时输出"分数错误"
提示：与js不同，python的判断中，多个条件的与、或关系不使用&&、||符号，应使用and、or

例：score = 78
	function_name(score)，输出C

'''
def function_score(score):
	if 90<score<=100:
		print('A')
	elif 80<score<=90:
		print('B')
	elif 70<score<=80:
		print('C')
	elif 60<=score<=70:
		print('D')
	elif 0<=score<60:
		print('E')
	elif score<0 or score>100:
		print('分数错误')

function_score1=function_score(95)
function_score2=function_score(85)
function_score3=function_score(102)



'''
3、给定一个数字数组，输出其中第三大的数

例：num_list = [52, 16, 78, 21, 35]
	function_name(num_list)，输出35
'''
'''
num_list = [52, 16, 78, 21, 35] 
#third_max_num = 0	
second_max_num = 0 #52
max_num = 0 # 78
for x in num_list:
	if x > max_num:
		#third_max_num = second_max_num
		second_max_num = max_num
		max_num = x

num_list.remove(max_num)

#print(third_max_num)
#print(second_max_num)
print(max_num)

'''


'''
4、输出一个九九乘法表
不用粟子吧-_-||
'''
# for y in range(1, 10):	
# 	for x in range(1, 10):
# 		print(x*y)




'''
5、给定一个任意位数的数字，输出该数字的位数，并逆序打印该数字

例：num = 5217，输出"4 7125"
	num = 16429，输出"5 92461"
'''
'''
def function_num(num):
	num1 = num%10
	num2 = (num/10)%10
	num3 = (num/100)%10
	num4 = (num/100)%100


function_num1 = function_num(7125)
function_num2 = function_num(16429)


'''

'''
！！！！！！WARNING！！！！！！

6.编写一个函数，实现类似python数组的切片功能
提示：使用 默认参数 或 dict类型参数

例：str_list6 = ['a','b','c','d','e','f']
	function_name(str_list6)，输出原数组，即['a','b','c','d','e','f']
	function_name(str_list6, 2)，输出['c','d','e','f']
	function_name(str_list6, 2, 4)，输出['c','d']
	function_name(str_list6, 0, 6 , 2)，输出['a','c', 'e']
'''

