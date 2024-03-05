# import math
# from math import pi
# import sys
# #
# # print(math.pi)
# # print(math.sin(math.pi/2))
#
# print(math.factorial(5))
# print(pi)
# print(dir())

# ---------------------------------------------------------------------------------------------------------

# from math import *
#
# print(sin(pi/2))
# print(factorial(3))
# print(ceil(4.7))

# ---------------------------------------------------------------------------------------------------------

# import math as m
#
# print(m.pi)

# ---------------------------------------------------------------------------------------------------------

# import random

# print(random.randint(1, 3))
# print(random.random())

# ---------------------------------------------------------------------------------------------------------

# from random import random, seed
# seed(0)
# for i in range(5):
#     print(random())

# ---------------------------------------------------------------------------------------------------------

from random import choice, sample

lst = [x for x in range(1,11)]

print(choice(lst))
print(sample(lst, 3))
print(sorted(sample(lst, 10)))

# ---------------------------------------------------------------------------------------------------------

# import platform
#
# print(platform.machine())
# print(platform.processor())
# print(platform.system())
# print(platform.version())
# print(platform.python_implementation())
# print(platform.python_version())
# print(platform.python_version_tuple())
# print(platform.machine())


# ---------------------------------------------------------------------------------------------------------

# import module
#
# print(dir(module))
# print(("Czy to jest ciąg znaków?", module.is_string("test")))
# print(("Suma elementów listy:", module.sum_list_elem([1,2,3,4])))