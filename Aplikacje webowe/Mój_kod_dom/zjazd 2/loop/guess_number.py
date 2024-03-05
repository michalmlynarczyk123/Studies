import random

number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (1-10): "))
counter = 1

while number != guess:
    while (guess > 10) or (guess < 1):
        guess = int(input("Miał być zakres od 1 do 10. Spróbuj jeszcze raz: "))
    guess = int(input("Nie, to nie ta liczba. Spróbuj jeszcze raz: "))
    counter += 1
    if (counter >=3):
        print("Wykorzystałeś swoje 3 szanse! Koniec gry.")
        break
else:
    print("Brawo! Udało Ci się już za " + str(counter) + " razem.")

