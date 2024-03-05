# sumuj elemnty przykładowej listy

sumNumber = 0
numbers = [1, 5, 6, 2, 4, 6, 7, 3, 6, 6, 7, 4]

for n in numbers:
    sumNumber += n
print("Suma wszystkich elementów listy", numbers, "to", str(sumNumber), ".")

print(sum(numbers))