#Wyświetlamy cyfrę, chyba że:
#liczba parzysta lub liczba większa od 6 to wyświetl gwiazdkę

for i in range(10):
    if i  % 2 == 0 or i > 6:
        print("*")
    else:
        print(i)