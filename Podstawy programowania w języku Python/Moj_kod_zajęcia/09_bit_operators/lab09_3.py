#Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby całkowitej.
#Bity liczymy od 0 od najmniej znaczącego bitu

number = int(input("Podaj liczbę: "))
n = int(input("Podaj numer bitu: "))

mask = 1 << n
result = number & mask
bit = int(bool(result)) #zamiana dowolnej liczby całkowitej na wartość 1 (0 zawsze będzie 0)
print("Bit na pozycji", n, "dla liczby", number, "wynosi", bit, ".")

#sprawdzenie

print("---")
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" * 8)
print("{:08b}".format(number & mask))