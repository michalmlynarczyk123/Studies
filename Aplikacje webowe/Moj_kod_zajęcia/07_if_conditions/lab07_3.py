import random

number = random.randint(1, 10)
msg = "Zgadnij jaką liczbę mam na myśli (od 1 do 10): "
guess = int(input(msg)) #pierwsza szansa

if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli")
else:
    msg = "Masz kolejną szansę, moja liczba jest "
    if number % 2 == 0:
        msg += "parzysta: "
    else:
        msg += "nieparzysta: "
    guess = int(input(msg)) #druga szansa

    if guess == number:
        print("Brawo! Udało Ci się odgadnąć już za drugim razem!")
    else:
        msg = "Masz ostatnią szansę. Moja liczba jest "
        if number > 5:
            msg += "większa niż "
        else:
            msg += "mniejsza niż "
        msg += "pięć: " #msg  = msg + "pięć"
        guess = int(input(msg))  # trzecia szansa

        if guess == number:
            print("Brawo! A jednak do trzech razy sztuka!")
        else:
            print("Myślałem o liczbie " + str(number) + ".")

