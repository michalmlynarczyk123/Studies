import random

print("Podaj zakres liczb")
range_from = int(input("od: "))
range_to = int(input("do: "))
series = random.randint(range_from, range_to)
counter = 1

print("Liczba serii: " + str(series) + ". Z przedziału " + str(range_from) + " do " + str(range_to) + ".")
for a in range(series):
    print("Seria " + str(counter) + ": ", end = "")
    for b in range(random.randint(range_from, range_to)):
        print(random.randint(range_from, range_to), end=" ")
        print(" | ", end="")
    print()
    counter += 1