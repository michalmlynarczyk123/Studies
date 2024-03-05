#pobierz 5 liczb całkowitych od użytkownika

# numbers = []
# for i in range(5):
#     number = int(input("Podaj liczbę całkowitą: "))
#     numbers.append(number)
# print(numbers)

numbers = []
counter = 1
while True:
    if counter > 5:
        break
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        numbers.append(number)
        counter += 1
    except:
        print("To nie jest liczba całkowita! Spróbuj ponownie!")

print(numbers)