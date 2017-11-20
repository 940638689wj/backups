num_list = [1,6,3,76,87]
# print(num_list[-1])

# 取出部分数组
new_num_list = []
for x in range(0,2):
	new_num_list.append( num_list[x])

# 切片
# print(num_list[1:5:2])

def area(r, num=1):
	return r * r * 3.14 * num

area1 = area(5)
area2 = area(6)
area3 = area(7)
area4 = area(8, 4)
print(area1)
print(area2)
print(area3)
print(area4)
# area(8)

