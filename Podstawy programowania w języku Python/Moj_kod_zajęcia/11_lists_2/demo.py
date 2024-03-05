'''

a = 1
b = 4

print("a =", a, "b =", b)

tmp = a
a = b
b = tmp

a, b = b, a

print("a =", a, "b =", b)

'''

#--------------------------------

'''

numbers = [1, 2 ,3]

numbers[0], numbers[1] = numbers[1], numbers[0]

print(numbers)

'''

#--------------------------------

'''

numbers = [4, 5, 2, 1]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

'''

#------------------
'''

letters = ["c", "a", "", "z"]
letters.sort()
print(letters)
letters.sort(reverse=True)
print(letters)

'''
#--------------------------
#lista jako typ referencyjny
#nazwa miejsca w pamięci gdzie przechowywana jest lista

'''
list1 = [9]
list2 = list1 #kopiuje nazwę listy, a nie jej zawartość (mamy dwie nazwy ale jedną listę)
list2[0] = 13
print(list1)

'''

#--------------------------
#wyciananie (slicing)
#umożliwia tworzenie zupełnie nowej kopii listy lub jej części
'''

list1 = [9]
list2 = list1[:] #kopiuje całą listę
list2[0] = 13
print(list1)

'''

#------------

'''
#           0  1  2  3  4
numbers = [10, 8, 6, 4, 2]
#          -5 -4 -3 -2 -1
new_numbers = numbers[1]


new_numbers = numbers[1:3]
print(numbers)
print(new_numbers)
'''
'''
numbers = [10, 8, 6, 4, 2]

del numbers[]
print(numbers)

numbers = [10, 8, 6, 4, 2]
print( not in numbers)

'''

#----------wyrażenia listowe

#numbers = []

#for i in range(30):
#    numbers.append(i + 1)
#print(numbers)

'''numbers = [i + 1 for i in range(30)]
#or
numbers = [i for i in range(1,31)]
print(numbers)'''

#numbers = [i for i in range(1, 101) if i % 2 == 0]
#print(numbers)


#zadanie
#ile jest liczb w przedziale 1-30, które dzielą się przez 3, 7 jednocześne


#print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))

#----------listy wielowymiarowe

row = [1, 2]

matrix = [row[:], row[:]]
matrix[0][0] = 99
print(matrix)
