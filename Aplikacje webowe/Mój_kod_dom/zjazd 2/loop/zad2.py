mark = int(input("Podaj rozmiar: "))
char = input("Podaj znak: ")

for i in range(mark):
    for j in range(mark):
        print(char, end=" ")
    print()