numbers = []
numbers_total = int(input("Podaj liczbę elementów zbioru: "))

for i in range(numbers_total):
    number = int(input("Podaj " + str(i + 1) + " element zbioru: "))
    numbers.append(number)
numbers.sort(reverse=True)

number_without_duplicates = []
for number in numbers:
    if number not in number_without_duplicates:
        number_without_duplicates.append(number)

print(number_without_duplicates)