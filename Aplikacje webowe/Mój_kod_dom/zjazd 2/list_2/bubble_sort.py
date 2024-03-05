#sortowanie bąbelkowe
#iterujemy po wszystkich elementach, jeżeli el1 >el2 to zamieniamy miejscami
#
#numbers = [4, 5, 2, 1]
#numbers = [4, 2, 1, 5]
#numbers = [2, 1, 4, 5]
#numbers = [1, 2, 4, 5]

numbers = [4, 5, 2, 1]
swapped = True
print(numbers)

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i +1]:
            numbers[i], numbers[i +1] = numbers[i +1], numbers[i]
            swapped = True
print(numbers)


numbers = [4, 5, 2, 1]
print(numbers)
numbers.sort()
print(numbers)