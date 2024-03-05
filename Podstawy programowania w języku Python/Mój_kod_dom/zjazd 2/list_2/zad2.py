numbers = []
total_numbers = int(input("Podaj zakres liczb: "))

for i in range(total_numbers):
    numbers.append(int(input("Podaj " + str(i + 1) + " liczbę: ")))
numbers.sort(reverse=True)

number_without_duplicates = []
for number in numbers:
    if number not in number_without_duplicates:
        number_without_duplicates.append(number)
print(number_without_duplicates)