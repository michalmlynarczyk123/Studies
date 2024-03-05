import random

DICE_RICE_TOTAL = 16
rolls = []
counter = 0

for i in range(DICE_RICE_TOTAL):
    rolls.append(random.randint(1,6))
    counter += 1
print("Zestaw wylosowanych liczb: ", rolls)
print("za ósmym razem wyrzucono", rolls[7])

six_total = 0
for roll in rolls:
    if (roll == 6):
        six_total += 1
print("Liczba wyrzuconych szóstek to", six_total)

tmp_value