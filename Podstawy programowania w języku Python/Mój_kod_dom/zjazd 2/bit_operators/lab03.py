number = int(input("Podaj liczbę: "))
n = int(input("Podaj numer bitu: "))

mask = 1 << n
result = number & mask
bit = int(bool(result))
print("Bit na pozycji", n, "dla liczby", number, "wynosi", bit, ".")

#sprawdzenie

print("---")
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" * 8)
print("{:08b}".format(number & mask))