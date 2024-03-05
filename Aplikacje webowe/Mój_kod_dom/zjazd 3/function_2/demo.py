# def show_numbers(numbers):
#     print(numbers)
#
#
# show_numbers([1, 2, 3])
#
# ---------------------------------------------------------------------

def generate_numbers(n):
    numbers = []
    for i in range(n):
        numbers.insert(0, i)
    return numbers
    return sorted(numbers) #posortowane


print(generate_numbers(10))

# ---------------------------------------------------------------------

# def sum_numbers(numbers):
#     sum = 0
#     for element in numbers:
#         sum += element
#     return sum
#
#
# print(sum_numbers([1, 2, 3, 4, 5, 6]))
# print(sum_numbers([5]))
# print(sum_numbers(range(5)))

# ---------------------------------------------------------------------

# def scope_test():
#     # x = 123 #zmienna lokalna
#     global x
#     x = 123 #zmienna lokalna 2
#     print("w srodku funckji: ", x)
#
# x = 999 #zmienna globalna
# scope_test()
# print("poza funkcją", x)
# # print(x) - to nie zadziała, x jest widoczne tylko w bloku funkcji


# ---------------------------------------------------------------------

# def change_value(n):
#     print("przed zmianą:", n)
#     n += 1
#     print("po zmianie:", n)
#
# val = 7
# change_value(val)
# print(val)

# def change_value(my_list_1):
#     print("przed zmianą:", my_list_1)
#     my_list_1 = [0, 0]
#     my_list_1[0] = 9 #!
#     print("po zmianie:", my_list_1)
#
# my_list_2 = [1,2]
# change_value(my_list_2)
# print(my_list_2)

# ---------------------------------------------------------------------

def recursion(number):
    if number > 10:
        return
    print(number)
    number += 1
    recursion(number)

recursion(0)