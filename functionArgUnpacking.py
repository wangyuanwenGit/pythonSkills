# Function arguement unpacking:

def myfunc(x, y, z):
    print(x, y z)

tuple_vec = (1, 0, 1)
dict_vec = {'x':1, 'y':0, 'z':1}

print(myfunc(*tuple_vec))
# 1, 0, 1
print(myfunc(**dict_vec))
# 1, 0, 1
