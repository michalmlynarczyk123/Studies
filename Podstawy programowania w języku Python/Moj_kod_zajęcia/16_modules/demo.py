# import math
#
# # import sys
# #
# # print(math.pi)
# # print(math.sin(math.pi/2))
#
# print(math.factorial(5)) #silnia
# print(math.floor(4.999))
# --------------------------------------------------------------
from math import pi, factorial, sin
# from math import *
#
# print(pi)
# print(dir())
# print(sin(pi / 2))
# print(factorial(3))
# print(ceil(4.7))
# --------------------------------------------------------------

# from math import pi as liczba_pi
#
# print(liczba_pi)
# # print(math.pi)
# # print(pi)
# print(dir())

# --------------------------------------------------------------

# import math
#
# print(dir(math))

# --------------------------------------------------------------

# import random
# from random import random, seed

# print(random.randint(1,3))
# print(random.random())

# seed(0)
#
# for i in range(5):
#     print(random())

# --------------------------------------------------------------

# from random import choice, sample
#
# lst = [x for x in range(1, 11)]
#
# print(choice(lst))
# print(sample(lst, 3))
# print(sample(lst, 10))

# --------------------------------------------------------------

# import platform
#
# # help(platform)
# print(platform.machine()) #ogólna nazwa procesora
# print(platform.processor()) #rzeczywista nazwa procesora
# print(platform.system()) # ogólna nazwa systemu operacyjnego
# print(platform.version()) # ogólna wersja systemu operacyjnego
# print(platform.python_implementation()) # implementacja pythona
# print(platform.python_version()) # wersja Pythona
# print(platform.python_version_tuple()) # wersja Pythona w krotce
#
# help(platform.machine)

# --------------------------------------------------------------
# IMPORTOWANIE MODUŁU MODULES

import modules

# print(dir(modules))
# help(modules)

print("Czy to jest ciąg znaków?", modules.is_string("test"))
print("Suma elementów listy: ", modules.sum_list_elem([1, 2, 3, 4, 5]))
