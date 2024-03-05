numbers = []
numbers_total = int(input("Podaj liczbę elemntów w zbiorze: "))
sumNumberparzyste = 0
sumNumbernieparzyste = 0

for i in range(numbers_total):
    number = int(input("Podaj " + str(i + 1) + " element zbioru: "))
    numbers.append(number)
print(numbers)

for i in numbers:
    if i % 2 == 0:
        sumNumberparzyste += i
    else:
        sumNumbernieparzyste += i
print("Liczby pobrane od użytkownika to: " + str(numbers) +
      " Suma liczb parzystych to: " + str(sumNumberparzyste) + " Natomiast suma liczb nieparzystych to: " + str(
    sumNumbernieparzyste) + ".")
