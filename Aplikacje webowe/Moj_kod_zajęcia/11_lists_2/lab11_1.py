'''import random

numbers = []
print("Obstaw 6 liczb od 1-49")

for i in range(0,6):
    numbers.append(input("Podaj " + str(i + 1) + " liczbę: "))
print("twoje liczby to: ", numbers)


numbers = [i for i in range(1, 50)]
random_numbers = random.sample(numbers, 6)
random_numbers.sort()
print("Wylosowane liczby to: ", random_numbers)

if numbers[0] == random_numbers[0] or numbers[1] == random_numbers[1] or numbers[2] == random_numbers[2] or numbers[3] == random_numbers[3] or numbers[4] == random_numbers[4] \
        or numbers[5] == random_numbers[5]:
    print("Gratulacje! Wygrałes")
else:
    print("Przykro mi! Nie wygrales")'''

import random

user_numbers = []
random_numbers = []
hit_total = 0

for i in range(6):
    user_numbers.append(int(input("Podaj " + str(i + 1) + " liczbę (1-49): ")))

random_numbers = random.sample(range(1,50), 6)

for number in user_numbers:
    if number in random_numbers:
        hit_total += 1

random_numbers.sort()
user_numbers.sort()
print("Wylosowano: ", random_numbers)
print("Obstawiono: ", user_numbers)
print("Trafiono: ", hit_total, "liczb.")




