import random

numbers = []
total_elements = int(input("Podaj liczbę elementów w zbiorze: "))
sumParz = 0
sumNie = 0

for i in range(total_elements):
    numbers.append(int(input("Podaj " + str(i + 1) + " liczbę: ")))
print(numbers)

for i in numbers:
    if i % 2 == 0:
        sumParz += i
    else:
        sumNie += i
print("Liczby to: ", numbers,
      ". Suma liczb parzystych to: " + str(sumParz) + ", a nieparzystych to: " + str(sumNie) + ".")
