def fetch_and_validate_int(standard_msg, error_msg="To nie jest liczba!"):  # dodano funkcję w 1 kroku
    while True:
        try:
            result_int = int(input(standard_msg))
            return result_int
        except:
            print(error_msg)


def define_player(player_no):
    player_name = input("Podaj imię {} gracza: ".format(player_no))
    return {player_name: []}


def define_players():
    players = {}
    # players_total = int(input("Podaj liczbę graczy (1-8): ")) #usunięto w 3 kroku
    players_total = fetch_and_validate_int("Podaj liczbę graczy (1-8): ")  # dodano w 2 kroku
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players


def define_win_points():
    # return int(input("Zdefiniuj liczbę punktów wygranej: ")) #usunięto w 5 kroku
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ")  # dodano w 4 kroku


def is_winner(players, win_points):
    for player_name, player_points in players.items():
        if sum(player_points) >= win_points:
            return True
    return False


def count_points(players, win_points):
    counter = 1
    while (True):
        print("\nTura", counter)
        for player_name in players.keys():
            # player_points = int(input("Podaj punkty dla gracza - {}: ".format(player_name))) #usunięto w 7 kroku
            player_points = fetch_and_validate_int(
                "Podaj punkty dla gracza - {}: ".format(player_name))  # dodano w 6 kroku
            players[player_name].append(player_points)
            if is_winner(players, win_points):
                return player_name
        counter += 1


def show_results(players, winner):
    print("\nWygrał gracz o imieniu {}, brawo!\n".format(winner))
    print("Szczegółowa tabela wyników:")
    for player, points in players.items():
        print(player, "->", points)


players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)

# print(fetch_and_validate_int("Podaj jakąś liczbę: "))
