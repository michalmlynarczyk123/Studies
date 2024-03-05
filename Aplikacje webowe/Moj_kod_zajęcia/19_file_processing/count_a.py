# zliczenie a w pliku data.tx
# file = open("data.txt", encoding="UTF-8") #pierwsza werjsa
with open("data.txt", encoding="UTF-8") as file:  # druga wersja
    txt = file.read()

print("Ilość wystąpień litery: a/A:", txt.lower().count("a"))
# file.close() #pierwsza wersja
