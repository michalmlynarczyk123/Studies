# def counter(a, b):
#     print("Obwód kwadratu o bokach {} cm i {} cm:".format(a,b), "to: ", 2 * a + 2 * b, "cm.")
#     print("Pole powierzchni kwadratu o bokach {} cm i {} cm:".format(a,b), "to: ", a * b, "cm2.")
#     print("Długość przekątnej kwadratu o bokach {} cm i {} cm:".format(a,b), "to: ", (a ** 2 + b ** 2) ** (1 / 2), "cm.")
#     print("-" * 10)
#
#
# result1 = counter(4, 5)
# result2 = counter(2678, 5678)
# result3  =counter(344555, 788998)

def perimeter(a, b):
    return 2 * a + 2 * b


def surface_area(a, b):
    return a * b


def diagonal_lenght(a, b):
    return (a ** 2 + b ** 2) ** (1 / 2)


def show_result(a, b):
    print("Prostokąt o bokach {} i {}:".format(a, b))
    print("Obwód:", perimeter(a, b))
    print("Pole powierzchni:", surface_area(a, b))
    print("Długość przekątnej: ", diagonal_lenght(a, b))
    print()


show_result(4, 5)
show_result(2678, 5678)
show_result(344555, 788998)
