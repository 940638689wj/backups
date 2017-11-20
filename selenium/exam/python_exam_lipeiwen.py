'''
要求：将所有实现写成函数的形式，通过调用函数验证对错
以下为完整示例：

题目：给定数组，输出所有元素
'''

# 函数实现：
#def show_list(target_list):
	#for target in target_list:
		#print(target)

# 调用函数，验证对错：
#str_list = ['a','b','c']
#show_list(str_list) # 控制台按顺序输出a b c即证明函数实现正确





#以下为测试题正文


'''
1、将数组内容倒序输出

例：str_list1 = ['a','b','c','d']
	function_name(str_list1)，输出['d','c','b','a']
'''
def show_list(target_list):
	for x in range(0,len(target_list)):
		# target_list[x]=target_list[-1-x]
		print(target_list[-1-x])

# str_list=['a','b','c','d']
# show_list(str_list)





'''
2、根据给定的分数，输出对应的评级，
   90~100输出A，80~90输出B，70~80输出C，60~70输出D，60以下输出E，
   给定的分数大于100或小于0时输出"分数错误"
提示：与js不同，python的判断中，多个条件的与、或关系不使用&&、||符号，应使用and、or

例：score = 78
	function_name(score)，输出C
'''
def level(score):
	if 90<score<100 or score==100:
		print('A')
	if 80<score<90  or score==90:
		print('B')
	if 70<score<80  or score==80:
		print('C')
	if 60<score<70  or score==70:
		print('D')
	if 0<score<60   or score==100 or score==0:
		print('E')
	else: print('分数错误')

# level(78)


'''

3、给定一个数字数组，输出其中第三大的数

例：num_list = [52, 16, 78, 21, 35]
	function_name(num_list)，输出35
'''
'''
def show_list(target_list):
	max_num=0
	sec_num=0
	third_num=0
	for target in target_list:
		if target>max_num:
			third_num=sec_num
			sec_num=max_num
			max_num=target
	print(third_num)
num_list = [52, 16, 78, 21, 100]
show_list(num_list)

	


'''

'''
4、输出一个九九乘法表
不用粟子吧-_-||
'''
def chengfa(x,y):
	for x in x_list:
		for y in y_list:
			num=x*y
			print(str(x) + '*' + str(y) + '=' + str(num))

x_list=[1,2,3,4,5,6,7,8,9]
y_list=[1,2,3,4,5,6,7,8,9]
chengfa(x_list,y_list)


'''
5、给定一个任意位数的数字，输出该数字的位数，并逆序打印该数字

例：num = 5217，输出"4 7125"
	num = 16429，输出"5 92461"
'''


# def show(a):
# 	i=1
# 	for x in x!=0:
# 		a=a%10
# 		x=a
# 		i++
# 	print(i)
# show(5217)



'''

！！！！！！WARNING！！！！！！

6.编写一个函数，实现类似python数组的切片功能
提示：使用 默认参数 或 dict类型参数

#例：str_list6 = ['a','b','c','d','e','f']
	function_name(str_list6)，输出原数组，即['a','b','c','d','e','f']
	function_name(str_list6, 2)，输出['c','d','e','f']
	function_name(str_list6, 2, 4)，输出['c','d']
	function_name(str_list6, 0, 6 , 2)，输出['a','c', 'e']
'''
