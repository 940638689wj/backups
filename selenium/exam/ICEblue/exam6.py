# def function_name(str_list,a,b,c):
	# print (str_list[a:b:c])

# list_a=[5,2,5,8,9]
# function_name(list_a,1,5)

def function_name(list_a,b,c,d):
	if(b==0 and c==0 and d==0):
		print(list_a)
		if(b!=0 and c!=0 and d==0):
			print(list_a[b:c])
			if(b!=0 and c!=0 and d!=0):
				print(list_a[b:c:d])
				
list_a=[5,2,5,8,9]
function_name(list_a,1,1,0)
 
