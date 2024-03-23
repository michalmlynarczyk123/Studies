# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# print(issubclass(Dog, Animal))
# print(issubclass(Cat, Animal))
# print(issubclass(Dog, Cat))
# print()
#
# dog = Dog()
# cat = Cat()
#
# print(isinstance(dog, Dog))
# print(isinstance(cat, Cat))
# print(isinstance(dog, Cat))
# print(isinstance(dog, Animal))

# ---------------------------------------------------------------------------------------------------------------------

# class MyClass:
#     def __init__(self):
#         self.x = 1
#
# obj1 = MyClass()
# obj2 = MyClass()
# obj3 = obj1
#
# obj3.x += 1
#
# # print(obj1 is obj2)
# # print(obj2 is obj3)
# # print(obj3 is obj1)
#
# print(obj1.x, obj2.x, obj3.x)

# ---------------------------------------------------------------------------------------------------------------------

# str1 = "Ala ma"
# str2 = "Ala ma kota"
# str1 += (" kota")
#
# print(str1 == str2)
# print(str1 is str2)

# ---------------------------------------------------------------------------------------------------------------------

# class Animal:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     # def __str__(self):
#     #     return f"Jestem zwierzęciem, mam na imię {self.__name}."
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         # Animal.__init__(self, name)
#         super().__init__(name)
#
#     def __str__(self):
#         return f"Jestem zwierzęciem, mam na imię {super().get_name()}."
#
# dog = Dog("Pluto")
# print(dog)

# ---------------------------------------------------------------------------------------------------------------------

# class Car:
#     def drive(self):
#         print("Jedzie...")
#
# class Boat:
#     def sail(self):
#         print("Płynie...")
#
# class Amphibian(Car, Boat):
#     pass
#
# amph = Amphibian()
# amph.sail()
# amph.drive()

# ---------------------------------------------------------------------------------------------------------------------

# class Left:
#     x = "l"
#     x_left = "ll"
#
#     def foo(self):
#         return "left"
#
#
# class Right:
#     x = "r"
#     x_right = "rr"
#
#     def foo(self):
#         return "right"
#
#
# class Subclass(Left, Right):
#     # x = "sx"
#     # x_left = "sxl"
#     # x_right = "sxr"
#     #
#     # def foo(self):
#     #     return "subclass"
#     pass
#
#
# obj = Subclass()
# print(obj.x_left, obj.x_right)
# print(obj.x, obj.foo())
#
# print(Subclass.__dict__)

# ---------------------------------------------------------------------------------------------------------------------

class A:
    def foo(self):
        print("Jestem foo() z klasy A")

    def bar(self):
        self.foo()

class B(A):
    def foo(self):
        print("Jestem foo() z klasy B")


objA = A()
objB = B()

# objA.bar()
objB.bar()