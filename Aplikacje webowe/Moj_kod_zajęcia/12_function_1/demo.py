# name = input("Jak masz na imię: ")
# name = input("Jak masz na imię: ")
# print("Witaj {}! ".format(name) * 10)
# print(("Witaj " + name + "! ") * 10)
#
# def introduce(first_name, last_name):
#     print("Cześć, jestem {} {}.".format(first_name, last_name))
#
#
# introduce("Kochanowski", "Jan")
#
# def show_numbers(a, b, c):
#     print("a = ", a)
#     print("b = ", b)
#     print("c = ", c)
#
#
# show_numbers(3, 1,2)
#
# introduce(first_name="Jan", last_name="Kochanowski")
# introduce(last_name="Kochanowski", first_name="Jan")
# introduce("Kochanowski", "Jan")
# # introduce(first_name="Kochanowski","Jan")
#
# show_numbers(a=1, b=2, c=3)
# show_numbers(b=1, a=2, c=3)
# show_numbers(c=2, a=1, b=3)
#
# print("---------------------------")
#
# print("raz", "dwa", "trzy", sep="-")
#
# print("---------------------------")
#
# def introduce(first_name="Jan", last_name="Kochanowski"):
#     print("Cześć, jestem {}{}.".format(first_name, last_name))
#
# introduce("Michał", "Młynarczyk")
# introduce()
# introduce(last_name="Młynarczyk")

# print("---------------------------")

# def show_name(name="Jan"):
#     print("Cześć, mam na imię {}.".format(name))
#
# result = show_name("Michał")
# print(result)

print("---------------------------")

def empty_function():
    pass
    #print("nic")
    #return 2
#print(empty_function())

if empty_function() is None:
    print("Funkcja nic nie zwróciła.")

