import random

number = random.randint(1, 3)
guess = int(input("Zgadnij jaką liczbę mam na myśli (1, 2, 3):"))

if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli.")
else:
    print("Niestety miałem na myśli liczbę: " +str(number)+ ".")

