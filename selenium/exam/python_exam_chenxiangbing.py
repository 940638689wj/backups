def sort_list(num_list):
	for y in range(0, len(num_list) - 1):
		for x in range(y, len(num_list) - 1 ):
			temp = num_list[x]
			num_list[x] = num_list[len(num_list) - 1]
			num_list[len(num_list) - 1] = temp


	print(num_list)

num_li = [63,21,6,84,12,112,7,23]
sort_list(num_li)

print('----------')

def score_class(score):

	if score<0 or score>100:
		print ('分数错误')
	if score<=100 and score>=90:
		print ('A')
	if score<90 and score>=80:
		print ('B')
	if score<80 and score>=70:
		print ('C')
	if score<70 and score>=60:
		print ('D')
	if score<60 and score>=0:
		print ('E')

score=88
score_class(score)

print('----------')

def third_num(num_list):
	max_num = 0
	second_num = 0
	third_num = 0
	for x in range(0,len(num_list)-1):
		if num_list[x]>max_num:
			third_num = second_num
			second_num = max_num
			max_num = num_list[x]
	print(third_num)

num_li = [63,21,6,84,12,112,7,23]
third_num(num_li)

print('----------')

a=9
b=9
for a in range(1,10):
	for b in range(1,10):
		print(a*b)
		b-=b
	a-=a

print('----------')

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
upside_down(num1)

