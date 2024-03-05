import random

print("Podaj zakres liczb.")
od = int(input("Od: "))
do = int(input("do: "))
series = random.randint(od, do)
counter = 1


print("Liczba wylosowanych serio to", series, ", z zakresu od:", od, "do", do)

for i in range(series):
    print("Seria ", str(counter), ": ", end="")
    for j in range(random.randint(od, do)):
        print(random.randint(od, do), end=" ")
        print(" | ", end="")
    print()
    counter += 1



