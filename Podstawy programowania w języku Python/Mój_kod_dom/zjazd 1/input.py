#char = input("Podaj znak: ")
#columns = int(input("Podaj liczbę kolumn: "))
#rows = int(input("Podaj liczbę wierszy: "))

#print((char * columns + "\n") * rows, end=" ")

account_balacne = input("Podaj kwotę: ")
interest = float(input("podaj oprocentowanie"))
period = float(input("Okres trwania lokaty: "))

print("Przy kwocie: " + str(account_balacne) + ", oraz oprocentowniu: " + str(interest) + ", na okres: " + str(period) + ". lokata zarobi: " + str(account_balacne * (1 + int(interest / 100 * str(period))) + "zł"))
