import random

number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli od 1 do 10: "))
counter = 1

while number != guess:
    guess = int(input("Nie to nie ta liczba. Spróbuj jeszcze raz: "))
    counter += 1

print("Brawo! Udało Ci się już za " + str(counter) + " razem!")
#print("Brawo! Udało Ci się już za ", counter, " razem!")
