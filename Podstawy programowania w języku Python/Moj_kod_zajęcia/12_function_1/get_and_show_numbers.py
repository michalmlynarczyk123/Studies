# def show_message(number_no):
#     print("Proszę podaj {} liczbę: ".format(number_no))

def get_number(number_no):
    print("Proszę podaj {} liczbę: ".format(number_no))
    return int(input())

#print("Podaj liczbę: ")
#show_message(1)
#a = int(input())
#a = get_number(1)

#print("Podaj liczbę: ")
#show_message(2)
#b = int(input())
#b = get_number(2)

#print("Podaj liczbę: ")
#show_message(3)
#c = int(input())
#c = get_number(3)

# print("podano liczby: ", a, b, c)
print("podano liczby: ", get_number(1), get_number(2), get_number(3), get_number(4))

