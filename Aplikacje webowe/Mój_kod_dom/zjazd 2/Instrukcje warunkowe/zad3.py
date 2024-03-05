import random

number = random.randint(1,10)
msg = ("Zgadnij jaką liczbę mam na myśli (1-10): ")
guess = int(input(msg))
print(number)

if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli!")
else:
    msg = "Nie taką liczbę miałem na myśli. Moja liczba jest "
    if number % 2 == 0:
        msg += "parzysta: "
    else:
        msg += "nieparzysta: "
    guess = int(input(msg))

    if guess == number:
        print("Brawo! Udało Ci się za drugim razem!")
    else:
        msg = "Masz ostatnią szansę. Moja liczba jest "
        if number > 5:
            msg += "większa od pięciu: "
        else:
            msg += "mniejsza od pięciu: "
        guess = int(input(msg))

        if guess == number:
            print("Brawo! Udało Ci się za trzecim razem!")
        else:
            print("Niestety! Miałem na myśli liczbę", number)