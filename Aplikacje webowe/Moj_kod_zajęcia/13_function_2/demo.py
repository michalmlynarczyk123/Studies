# def sum_numbers(numbers):
#     sum = 0
#     for element in numbers:
#         sum += element
#     return sum
#
#
# print(sum_numbers([1, 2, 3, 4, 5, 6]))


# def scope_test():
#     x = 123 #zmienna lokalna
#
# scope_test()
# print(x) #to nie zadziała, x jest widoczne tylko w bloku funkcji


# def scope_test():
#     print("w środku funkcji: ", x)
#
# x = 999 #zmienna globalna
# scope_test()
# print("poza funkcją: ", x)

# def scope_test():
#     global x
#     x = 123 #zmienna lokalna
#     print("w środku funkcji: ", x)
#
# x = 999 #zmienna globalna
# scope_test()
# print("poza funkcją: ", x)


# def change_value(n):
#     print("przed zmianą:", n)
#     n += 1
#     print("po zmianie: ", n)
#
# val = 7
# change_value(val)
# print(val)

# def change_value(my_list_1):
#     print("przed zmianą", my_list_1)
#     my_list_1[0] = 9
#     print("po zmianie", my_list_1)
#
#
# my_list_2 = [1, 2]
# change_value(my_list_2)
# print(my_list_2)

def recursion(number):
    if number > 100:
        return
    print(number)
    number += 1
    recursion(number)

recursion(-100)

