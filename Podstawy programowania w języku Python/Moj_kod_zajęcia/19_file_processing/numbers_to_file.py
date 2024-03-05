# wylosuj 100 liczb z zakresu 0-999 i zapisz do pliku numbers.txt

from random import randint

with open("numbers.txt", "wt", encoding="UTF-8") as file:
    for _ in range(100):
        number = randint(0,999)
        file.write(f"{number}\n")