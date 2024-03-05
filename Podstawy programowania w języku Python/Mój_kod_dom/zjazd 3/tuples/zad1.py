phones = {
    "Adam": 123456789,
    "Karol": 459687425,
    "Mariola": 159753852,
    "Iza": 789564231
}

while(True):
    name = input("Podaj imię: ")
    if name == "":
        break
    print(phones.get(name, "Nie znaleziono telefonu dla imienia"))  #druga opcja, krótsza

    # elif name in phones:
    #     print("Telefon: ", phones[name])
    # else:
    #     print("Nie znaleziono telefonu dla imienia", name) # pierwsza opcja dłuższa