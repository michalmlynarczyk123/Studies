#Wyświetl liczby podzielne przez 3, 5 lub 7 ze zbioru z zakresu określonego przez użytkownika
print("Podaj zakres liczb")
range_from = int(input("od: "))
range_to = int(input("do: "))
print("Liczby z zakresu od", range_from, " do ", range_to, "podzielne przez 3, 5 lub 7 to: ", end = " ")


for number in range(range_from, range_to + 1):
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            print(number, end = " ")