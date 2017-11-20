def sort_list(num_list):
	for y in range(0, len(num_list) - 1):
		for x in range(0, len(num_list) - 1 - y):
			if num_list[x] < num_list[x + 1]:
				temp = num_list[x]
				num_list[x] = num_list[x + 1]
				num_list[x + 1] = temp


	print(num_list[2])

num_li = [63,21,6,84,12,112,7,23]
# sort_list(num_li)

print(max(num_li))
print(sorted(num_li))
