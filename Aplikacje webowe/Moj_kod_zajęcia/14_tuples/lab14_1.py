phones = {
    "Adam": 111222333,
    "Karol":777888999,
    "Mariola": 456789123,
    "Iza": 123456789,
    "Michał": 654321789,
    "Kasia": 951753852
}

while(True):
    name = input("Podaj imię: ")
    if name == "":
        break
    print(phones.get(name, "Nie znaleziono telefonu dla imienia"))

    # elif name in phones:
    #     print("Telefon: ", phones[name])
    # else:
    #     print("Nie znaleziono telefonu dla imienia", name)