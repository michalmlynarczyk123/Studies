number = int(input("Podaj rozmiar: "))
char = input("Podaj znak: ")

for i in range(number):
    for j in range(number):
        print(char, end = " ")
    print()