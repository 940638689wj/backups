# 给定一个数组
#条件
# num_list = [63,21,6,84,12,112,7,23]

#求出偶数位总和
# num = 0
# for x in num_list[1::2]: #遍历
# 	num = num + x

#求出偶数总和
# num = 0
# for x in num_list: #遍历
# 	if x%2 == 0:
# 		num = num + x

# 求最大值
# max_num = 0
# for x in num_list:
# 	if x > max_num:
# 		max_num = x

# 求第二大的值
num_list = [112,63,21,6,84,12,7,23]
second_max_num = 0 #84
third_max_num = 0 #84
max_num = 0 # 112
for x in num_list:
	if x > max_num:
		third_max_num = second_max_num
		second_max_num = max_num
		max_num = x
	else:
		if x > second_max_num:
			third_max_num = second_max_num
			second_max_num = x
		else:
			if x > third_max_num:
				third_max_num = x

print(third_max_num)
print(second_max_num)
print(max_num)

# 排序
# num_list = [63,21,6,84,12,112,7,23]

# for y in range(0, len(num_list) - 1):
# 	for x in range(0, len(num_list) - 1 - y):
# 		if num_list[x] > num_list[x + 1]:
# 			temp = num_list[x]
# 			num_list[x] = num_list[x + 1]
# 			num_list[x + 1] = temp


# print(num_list)


# # 函数写法
# def sort_list(num_list):
# 	for y in range(0, len(num_list) - 1):
# 		for x in range(0, len(num_list) - 1 - y):
# 			if num_list[x] > num_list[x + 1]:
# 				temp = num_list[x]
# 				num_list[x] = num_list[x + 1]
# 				num_list[x + 1] = temp

# 	print(num_list)


# num_list_for_test = [63,21,6,84,12,112,7,23]
# # sort_list(num_list_for_test)

# s=input()
# print(s)
