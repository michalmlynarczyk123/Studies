import random
words = []

def break_point():
    print(" " * 50)
    print()

def check_value(msg, error_msg="To nie jest liczba! Spróbuj ponownie!"):
    while True:
        try:
            msg = int(input(msg))
            return msg
        except:
            print(error_msg)

def get_players():
    players = []
    while True:
        no_of_players = check_value("Podaj liczbę graczy (1-3): ")
        if no_of_players < 1 or no_of_players > 3:
            print("Podałeś liczby z poza zakresu (1-3). Spróbuj ponownie!")
            continue
        for p in range(no_of_players):
            player = input("Podaj imię {} gracza: ".format(p + 1))
            players.append(player)
            if p > no_of_players:
                break
        return players

def add_words():
    while True:
        word = input("Dodaj słowo: ")
        if word in words:
            print("Słowo już istnieje! Spróbuj jeszcze raz!")
            continue
        if word == "":
            print('Nie podano słowa! Spróbuj jeszcze raz!')
            continue
        else:
            words.append(word)
        break


def check_word(words):
    for word in words:
        user_word = input("Powtórz wszystkie poprzednie słowa: ")
        if user_word != word:
            return False
    return True


def game(players):
    counter = 1
    first_player = random.randint(0, len(players))
    print("*** Runda {} ***".format(counter))
    print("Rozpoczyna gracz {}.".format((players[first_player])))
    add_words()
    while True:
        for player in players:
            break_point()
            print("{} twoja kolej!".format(player))
            break_point()
            if check_word(words):
                counter += 1
                add_words()
            else:
                print("Przegrałeś! Koniec gry!")
                break





players = get_players()
game(players)
break_point()
