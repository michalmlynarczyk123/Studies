with open('data_zad1.txt', 'r') as file:
    suma = 0
    for line in file:
        liczba = int(line)
        suma += liczba
    print("Suma liczba w pliku data_zad1.txt to: ", suma)