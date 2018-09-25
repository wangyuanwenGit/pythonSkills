# value swapping:

# How to swap the values of a and b...

a = 23
b = 42

# The classic way to do it with a temporary variable:
temp = a
a = b
b = temp

# Python also let us this short-hand:
a, b = b, a
