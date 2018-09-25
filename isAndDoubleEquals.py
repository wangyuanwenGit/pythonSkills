# "is" vs "=="

a = [1, 2, 3]
b = a

print(a is b)
# True
print(a == b)
# True

c = list(a)

print(a == c)
# True
print(a is c)
# False

# "is" expressions evaluate to True if two 
# variables point to the same object.

# "==" evaluate to True if the objects referred to by the variables are equal.

# "==",简单来说就是==比较的是两个对象的值是否相同，value作为判断依据
# "is",同一性运算符，比较两个对象是否相同，即是否是同一个引用，id作为判断因素
