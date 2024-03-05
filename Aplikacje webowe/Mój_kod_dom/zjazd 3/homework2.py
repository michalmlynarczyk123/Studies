print("***Budujemy wieżę!***")

level = int(input("Podaj z ilu poziomów ma składać się wieża: "))
print("Wieża będzie miała {} poziomy/poziomów.\n".format(level))


def tower(n):
    sum = 0
    if n < 1:
        return level
    return tower(n - 1) - 1

def sumL(n):
    if n < 1:
        return n
    else:
        return n + sumL(n-1)

for n in range(level):
    # print("Poziom: ", n + 1, " -->  Liczba puszek, z których zbudowany jest poziom: ", tower(n))
    print("Poziom {} -->  Liczba puszek, z których zbudowany jest poziom: {} sztuk.".format(n + 1, tower(n)))
print("\nSuma puszek potrzebnych do zbudowania wieży to: {} sztuk.".format(sumL(level)))
