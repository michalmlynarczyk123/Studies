#a = 4
#b = 5
#c = 7
#d = 12
#e = 1
#print(a, b, c, d, e)

#numbers = [1, 2, 3, 4, 5]
#numbers = [1, 1, 1, 1, 1]
#numbers = [1, "dwa", True, 2.0]
#print(numbers)

#fruits = ["banan", "jabłko", "czerśnia"]
#fruits = ["banan", "jabłko", "czerśnia", "banan"]
#print(fruits)

#------------------------------------------------------------
fruits = ["banan", "jabłko", "czereśnia", "banan"]
#            0         1          2          3
#           -4        -3         -2         -1
# print(fruits[2])
# print(fruits[-2])
# #print(fruits[-6]) #error

print(len(fruits))

del fruits[-2]
#del fruits
print(fruits)
print(fruits[2])
print(fruits[-1])

#wynik to się rwna funkcja(argument)
l = len(fruits) #len() to funkcja
print(l)

#wynik to się równa dane.metoda(argument)
fruits.append("mandarynka") #append() to metoda
print(fruits)

#---------------------------insert
fruits = ["banan", "jabłko", "czereśnia", "banan"]
fruits.insert(3, "kiwi")
print(fruits)

#sposób klasyczny
fruits = ["banan", "jabłko", "czereśnia", "banan"]

for i in range(len(fruits)):
    print(fruits[i])

#nowy sposób
fruits = ["banan", "jabłko", "czereśnia", "banan"]

for fruit in fruits:
    print(fruit)