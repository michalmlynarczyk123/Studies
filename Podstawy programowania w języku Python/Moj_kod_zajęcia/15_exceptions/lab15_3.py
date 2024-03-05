def fetch_and_validate_int(standard_msg, error_msg="To nie jest liczba!"): #dodano to i potem do każdego inputa#
    while True:
        try:
            result_int = int(input(standard_msg))
            return result_int
        except:
            print(error_msg)

def define_player(player_no):
#    player_points = []
    player_name = input("Podaj imię {} gracza: ".format(player_no))
    return {player_name: []}
#    return {player_name, player_points}

def define_players():
    players = {}
    players_total = fetch_and_validate_int("Podaj liczbę graczy (od 1 do 8): ")
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players

def define_win_points():
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ")

def is_winner(players, win_points):
    for player_name, player_points in players.items():
        # print("---------------------------", player_name, player_points, sum(player_points))
        if sum(player_points) >= win_points:
            return True
    return False

def count_points(players, win_points):
    counter = 1
    while(True):
        print("\nTura", counter)
        for player_name in players.keys():
            player_points = fetch_and_validate_int("Podaj punkty dla gracza  - {}: ".format(player_name))
            players[player_name].append(player_points)
            if is_winner(players, win_points):
                return player_name
        counter += 1

def show_results(players, winner):
    print("\n Wygrał gracz o imieniu {}, brawo!\n".format(winner))
    print("Szczegółowa tabela wyników")
    for player, points, in players.items():
        print(player, "->", points)

players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)

