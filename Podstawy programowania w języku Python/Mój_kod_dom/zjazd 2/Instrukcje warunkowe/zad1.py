number = int(input("Podaj liczbę: "))

if (number ** (1 / 2)) % 1 == 0:
    str1 = "Tak"
    str2 = ""
else:
    str1 = "Nie"
    str2 = "nie"
print(str1 + ", piewiastek kwadratowy z liczby " + str(number) + " " + str2 + "jest liczbą całkowitą.")
