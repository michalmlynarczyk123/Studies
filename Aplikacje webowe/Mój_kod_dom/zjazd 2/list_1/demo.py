# a = 4
# b = 5
# c = 7
# d = 12
# e = 1
#
# numbers = [1, "dwa", True, 2.0, int]
# print(numbers)

#indeksy#
#            0        1           2          3         4
fruits = ["banan", "jabłko", "czereśnia", "banan", "gruszka"]
#           -5       -4          -3         -2        -1

# print(fruits[-5])
#
# print(len(fruits))

# print(fruits)
# print(fruits[3])
# del fruits[-2]
# print(fruits)
# print(fruits[3])


#------------------wynik = funkcja(argument)-------------#
# l = len(fruits)
# print(l)

#------------------wynik =dane.metoda(argument)-------------#
# fruits.append("mandarynka") # append() to metoda
# print(fruits)


# #-----------podsumowanie append i insert-----------------------#
# print(fruits)
# fruits.append("śliwka")
# print(fruits)
#
# fruits.insert(3, "kiwi")
# print(fruits)


#------------iterowanie po liście - sposób klasyczny!!!-------------#
for i in range(len(fruits)):
    print(fruits[i])
print("")
#------------iterowanie po liście - sposób nowy!!!-------------#

for fruit in fruits:
    print(fruit)
