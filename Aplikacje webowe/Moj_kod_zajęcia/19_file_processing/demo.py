# # odczyt z pliku
# file = open("./data.txt") #("data.txt", mode="rt") # domyślnie
# # operacje na pliku
# file.close()

# file = open("data.txt", encoding="UTF-8")
# print(file.read())
# file.close()

# bezwzględna/absolutna - pełna ścieżka od folderu głównego
# C:\folder\plik.txt, /home/user/plik.txt
# ścieżka względna
# plik.txt, ../plik.txt, ./folder/plik.txt

# ---------------------------------------------------------------------------------------------------------------------
# zapis do pliku
# jeśli plik nie istnieje to zostanie stworzony
# jeśli istnieje to zostanie wyzerowany

# with open("data2.txt", "wt", encoding="UTF-8") as file:
#     file.write("Cześć! Mam na imię Michał.")

# ---------------------------------------------------------------------------------------------------------------------
# from os import strerror
#
# try:
#     with open("data3.txt") as file:
#         pass
# except IOError as e:
#     print(f"Błąd podczas przetwarzania pliku", {strerror(e.errno)})

# ---------------------------------------------------------------------------------------------------------------------

# odczytaj plik tekstowy po 1 znaku

# try:
#     counter = 0
#     with open("data.txt", encoding="UTF-8") as file:
#         char = file.read(1)
#         while char != "":
#             print(char, end="")
#             counter += 1
#             char = file.read(1)
#         print(f"\nZnaki w pliku:{counter}")
# except IOError as e:
#     print(f"Błąd odczytu pliku: {e}")

# ---------------------------------------------------------------------------------------------------------------------

try:
    for line in open("data.txt", encoding="UTF-8"):
        print(line, end="")
except IOError as e:
    print(f"Błąd odczytu z pliku: {e}")