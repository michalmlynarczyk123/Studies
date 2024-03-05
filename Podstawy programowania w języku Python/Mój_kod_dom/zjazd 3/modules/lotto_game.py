# import lotto
import zad3 #zmienione z zadanie 3

print("Witaj w grze LOTTO!")
user_numbers = zad3.get_user_numbers()
print("Podane liczby to:", user_numbers)

input("\nNaciśnij ENTER, aby dokonać losowania liczb!\n")

lucky_numbers = zad3.draw_numbers()
print("Wylosowano liczby:", lucky_numbers)
print()

result = zad3.check_numbers(user_numbers, lucky_numbers)

if result == 6:
    print("GRATULACJE!!!", "Jesteś milionerem!")
elif result == 5:
    print("BRAWO!!!", "Trafiono piątkę!", "Zgarniesz sporą sumę!")
elif result == 4:
    print("Hurra!!!", "Trafiono czwórkę!", "To całkiem niezły wynik!")
elif result == 3:
    print("Trafiono trójkę!", "Przysługuje ci minimalna wygrana!")
elif result == 2 or result == 1:
    print("Trafiono {} liczbę/y. Było bardzo blisko!".format(result))
else:
    print("To nie jest Twój dzień!")