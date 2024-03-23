with open("pies-baskervilleow.txt", encoding="UTF-8") as file:  # druga wersja
    txt = file.read()

print("Ilość wystąpień imienia: Holmes:", txt.count("Holmes"))
print("Ilość wystąpień imienia: Watson:", txt.count("Watson"))
