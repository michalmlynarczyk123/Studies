#---------------------------------------------sortowanie bąbelkowe------------------------------------------------------
#iterujemy po wszystkich elementach, jeżeli el1 > el 2 to zamieniamy miejscami
#np. numbers = [4, 5, 2, 1]
#np. numbers = [4, 2, 1 ,5]
#np. numbers = [2, 1, 4 ,5]
#np. numbers = [1, 2, 4 ,5] - powtarzamy operacje tyle razy, aż nie będzie potrzeba nic zmieniać

numbers = [4, 5, 2, 1]
swapped = True
print(numbers) #przed posortowaniem

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True
print(numbers) # po sortowaniu