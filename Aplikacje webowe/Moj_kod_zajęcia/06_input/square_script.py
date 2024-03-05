#Zadanie 1

char = input("Podaj znak: ")
columns = int(input("Podaj liczbę kolumn: "))
rows = int(input("Podaj liczbę wierszy: "))

print()
print((char * columns + "\n") * rows, end="")

