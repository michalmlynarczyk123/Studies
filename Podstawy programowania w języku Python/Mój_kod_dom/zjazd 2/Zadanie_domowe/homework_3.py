print("Podaj liczbę do konwersji i obliczenia jedynek")

liczba = int(input("Podaj liczbę całkowitą: "))
jedynki = 0
wynik = []

print(f'Wprowadziłeś liczbę dziesiętną: {liczba};')

while liczba > 0:
    wynik.append(liczba % 2)
    if liczba % 2:
        jedynki += 1
    liczba = int(liczba / 2)

wynik.reverse()

print(f"Liczba ta w reprezentacji binarnej: {wynik}")
print(f"W reprezentacji binarnej podana liczba ma tyle jedynek: {jedynki} ")