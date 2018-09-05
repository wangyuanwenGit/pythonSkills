# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a':4, 'b':3, 'c':2, 'd':1}

def sort_dict_1(dic):
	temp = sorted(dic.items(), key=lambda x:x[1])
	print(temp)
	
def sort_dict_2(dic):
	import operator
	temp = sorted(dic.items(), key=operator.itemgetter(1))
	print(temp)
	
print("method_1:")
sort_dict_1(xs)

print("method_2:")
sort_dict_2(xs)
	

