#Napisz program, który zasymuluje 16 rzutów kostką do gry, a następnie wyświetlić poniższe informacje:
#zestaw wylosowanych wyników,
#wyrzucaną wartość za 8 razem,
#liczbę wyrzuconych szóstek,
#maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

import random
"""numbers = []

for i in range(16):
    number = random.randint(1, 6)
    numbers.append(number)
print("wylosowane liczby to:", numbers)
print("Za 8 rzutem wyrzuciłeś: ", numbers[7])
print("Suma wyrzuconych szóstek to: ", )
print("Najczęście pod rząd wyrzucałeś: ", )"""

DICE_ROLLS_TOTAL = 16
rolls = []

for i in range(DICE_ROLLS_TOTAL):
    rolls.append((random.randint(1, 6)))
print("Zbiór wyników po", DICE_ROLLS_TOTAL, "rzutach kostką do gry: ", rolls)
print("Za 8 rzutem wyrzuciłeś:", str(rolls[7]) + ".")

sixes_total = 0

for roll in rolls:
    if (roll == 6):
        sixes_total += 1

print("Wyrzucono", sixes_total, "razy szóstkę.")

value_tmp = rolls[0]
total_tmp = 0
value = rolls[0]
total = 0

for roll in rolls:
    if roll == value_tmp:
        total_tmp += 1
    else:
        value_tmp = roll
        total_tmp = 1
    if total_tmp > total:
        total = total_tmp
        value = value_tmp
print("Pod rząd wyrzucono:", total, "razy wartość:", str(value) + ".")