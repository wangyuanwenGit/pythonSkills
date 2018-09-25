# function can be pass as arguements to other functions,
# return as values from functions, and 
# assigned as variables and stored in data structure.

def func(a, b):
    return a + b

funcs = [func]

print(funcs[0])
# <function func at 0X1070...>

funcs[0](1, 2)
# 3

