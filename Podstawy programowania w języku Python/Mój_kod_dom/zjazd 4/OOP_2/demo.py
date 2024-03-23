# class MyClass:
#     def __init__(self, x=1):
#         # self.x = x
#         self.__x = x
#
#     def set_y(self, y=2):
#         self.__y = y
#
# obj1 = MyClass() # ustawiamy właściwość x=1
# # obj1.__x = 101
# # print(obj1.__x)
# # print(obj1.__dict__)
#
# obj2 =MyClass(2) # właściwość x=2
# obj2.set_y(7) # właściwość y=7
#
# obj3 = MyClass(3) # właściwość x=3
# obj3.z = 99 # właściwość z=99
#
# # __dict__ - nazwy i wartości wszystkich właściwości, które obecnie posiada obiekt
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
#
# print(obj1._MyClass__x)

# ----------------------------------------------------------------------------------------------------------------------

# class MyClass:
#     __counter = 0 # niepubliczna zmienna klas
#
#     def __init__(self, x=1):
#         self.__x = x # niepubliczna zmienna egzemplarza
#         MyClass.__counter += 1
#
#
# # obj1 = MyClass()
# # obj2 = MyClass(2)
# # obj3 = MyClass(3)
# #
# # print(obj1.__dict__, obj1._MyClass__counter)
# # print(obj2.__dict__, obj2._MyClass__counter)
# # print(obj3.__dict__, obj3._MyClass__counter)
# #
# # obj4 = MyClass()
# # print(obj4._MyClass__counter)
#
# print(MyClass.__dict__)
# obj1 = MyClass()
# print(obj1.__dict__)

# ----------------------------------------------------------------------------------------------------------------------

# class MyClass:
#     def __init__(self, x=1):
#         if x % 2 == 0:
#             self.a  = x
#         else:
#             self.b = x
#
# obj = MyClass(9)
# # try:
# #     obj = MyClass()
# #     # print(obj.a)
# #     print(obj.b)
# # except AttributeError:
# #     print("Nie ma takiej właściwości")
#
# if hasattr(obj, "a"):
#     print(obj.a)
# if hasattr(obj, "b"):
#     print(obj.b)

# ----------------------------------------------------------------------------------------------------------------------

class MyClass:
    x = 1

obj = MyClass()

print(hasattr(MyClass, "x"))
print(hasattr(MyClass, "y"))