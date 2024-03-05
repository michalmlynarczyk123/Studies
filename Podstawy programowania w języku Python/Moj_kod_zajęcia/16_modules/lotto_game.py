import lotto

print("Witaj w grze LOTTO!")
user_numbers = lotto.get_user_numbers()
print("Podane liczby to:", user_numbers)

input("\nNaciśnij ENTER, aby dokonać losowania liczb!\n")
lucky_numbers = lotto.draw_numbers()
print("Wylosowano liczby:", lucky_numbers)
print()

result = lotto.check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("GRATULACJE!", "Jesteś milionerem!")
elif result == 5:
    print("BRAWO!", "Trafiono piątkę!", "Zgarniesz sporą sumę!")
elif result == 4:
    print("Hurra!", "Trafiono czwórkę!", "To całkiem niezły wynik!")
elif result == 3:
    print("Trafiono trójkę!", "Przysługuje Ci minimalna wygrana!")
elif result == 2 or result == 1:
    print("Trafion {} liczbę/y. Było bardzo blisko!".format(result))
else:
    print("To nie jest Twój dzień")