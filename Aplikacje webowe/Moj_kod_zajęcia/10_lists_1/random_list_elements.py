#wylosować 10 liczb
#liczby z zakresu 1-100
#umieścić w liście
#wyświetlić listę

import random

numbers = []

for i in range(10):
    number = random.randint(1, 100)
    numbers.append(number)
print(numbers)