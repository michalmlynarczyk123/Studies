# # a = 1
# # b = 4
# #
# # print("a = ", a, "b = ", b)
# #
# # a, b = b, a
# #
# # print("a = ", a, "b = ", b)
#
# numbers = [1, 2, 3]
# print(numbers)
# numbers[0], numbers[1] = numbers[1], numbers[0]
# print(numbers)
#
# letters = ["c", "a", "", "z"]
#
# letters.sort()
# print(letters)
#
# # lista jako typ referencyjny
# # nazwa miejsca w pamięci gdzie przechowywana jest lista
#
# list1 = [9]
#
# list2 = list1  # kopiuję nazwę list, a nie jej zawartość(mamy 2 nazwy ale jedną listę)
#
# list2[0] = 13
# print(list1)
#
# print("-----------------------------------------------")
# # wycinanie(slicing)
# # umożliwia tworzenie zupełnie nowej kopii listy lub jej części
#
# list1 = [9]
# list2 = list1[:]  # kopiuje całą listę
# list2[0] = 13
# print(list1)

# --------------

# #           0  1  2  3  4
# numbers = [10, 8, 6, 4, 2]
# #          -5 -4 -3 -2 -1
#
# new_numbers = numbers[:]
#
# print(numbers)
# print(new_numbers)

# -Wyrażenia listowe
# numbers = [1,2,3,4,5]
#
# numbers = []
# for i in range(30):
#     numbers.append(i + 1)
#
# print(numbers)

# numbers = [i + 1 for i in range(30)]  # to samo co to na górze (for i in range(30)) !!!!!!!
# # numbers = [i * 2 for i in range(30)] #można mnożyć
#
# numbers = [i for i in range(1, 101) if i % 2 == 0]
#
# print(numbers)
#
# # Za pomocą jednej lini - ile jest liczb w przedziale 1 - 300, które dzielą się przez 3 i jednocześnie
#
# print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))

#----------listy wielowymiarowe

row = [1, 2]

matrix = [row[:], row[:]]
matrix[0][0] = 99
print(matrix)