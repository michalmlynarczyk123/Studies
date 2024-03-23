# class MyClass:
#     y = 99
#     def my_method(self, x):  # obowiązkowy parametr self
#         self.other_method()
#         print("To jest moja metoda:", x, self.y)
#
#     def other_method(self):
#         print("To jest inna metoda", self.y)

# obj = MyClass()  # tworzenie instancji klasy (instancji)
# obj.my_method("A")  # wywołanie metody (zachowania) my_method na obiekcie obj klasy MyClass
# obj.my_method(1)
# obj.my_method(2)

# ---------------------------------------------------------------------------------------------------------------------

# class MyClass:
#
#     def __init__(self, name): # konstruktor bezparametrowy / z parametrem (name)
#         print("Inicjalizuję obiekt")
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#
# obj = MyClass("Kamila")
# print(obj.get_name())

# ---------------------------------------------------------------------------------------------------------------------

# class MyClass:

#     def __my_private_method(self):
#         print("To jest metoda niepubliczna")
#
#     def my_public_method(self):
#         self.__my_private_method()
#         print("To jest metoda publiczna")

# obj = MyClass()
# # obj._MyClass__my_private_method()
# obj.my_public_method()
# print(obj.__dict__)
# print(MyClass.__dict__)

# ---------------------------------------------------------------------------------------------------------------------

# class MyClass:
#     pass

# print(MyClass.__name__)
# obj = MyClass()
# print(type(obj).__name__)
# print(MyClass.__module__)

# ---------------------------------------------------------------------------------------------------------------------

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# print(C.__bases__)

# for c in C.__bases__:
#     print(c.__name__)

# ---------------------------------------------------------------------------------------------------------------------

class MyClass:
    x = 5

    def __init__(self):
        self.y = 9


obj = MyClass()
print(obj.x, obj.y)

print(MyClass.__dict__)
print(obj.__dict__)

setattr(obj, "z", 1)
print(obj.__dict__)

print(getattr(obj, "x"))
print(obj.z)