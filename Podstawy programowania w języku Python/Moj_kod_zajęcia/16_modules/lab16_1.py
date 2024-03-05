import platform
import random
import math

# print("1", "-" * 100)
# print(platform.processor())
#
# print("2","-" * 100)
#
# lst = [x for x in range(1, 11)]
#
# print(sample(lst, 3))
# print("3","-" * 100)
#
# print(math.sin(90))

print("Procesor:", platform.processor())
print("Losowanie:", random.sample([x for x in range(1, 11)], 3))
print("Sinus:", math.sin(math.radians(90)))