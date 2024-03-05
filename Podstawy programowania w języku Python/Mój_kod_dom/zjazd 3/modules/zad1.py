import platform
import random
import math

print("Procesor:", platform.processor())
print("Losowanie: ", random.sample([x for x in range(1,11)], 3))
print("Sinus 90 stopni to: ", math.sin(math.radians(90)))