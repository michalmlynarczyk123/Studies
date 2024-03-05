number = int(input("Podaj liczbę:"))
print("Liczba jest: " + str(number))

if number % 2 == 0:
    print("- jest liczbą parzystą.")
else:
    print("- jest liczbą nieparzystą.")

if number % 5 == 0:
    print("- jest podzielna przez 5")
else:
    print("- jest niepodzielna przez 5")

if number % 7 == 0:
    print("- jest podzielna przez 7")
else:
    print("- jest niepodzielna przez 7")