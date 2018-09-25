# The "timeit" module lets you measure the execution
# time of small bits of Python code.

import timeit
time = timeit.timeit('"-".join(str(n) for n in rang(100))', number=10000)
print(time)
# 0.3412662749997253

time = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(time)
# 0.2996307989997149

time = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(time)
# 0.24581470699922647

