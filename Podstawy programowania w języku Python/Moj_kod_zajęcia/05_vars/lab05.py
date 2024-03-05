#Zadanie 1
name = "Michał"
age = 30
city = "Kraków"

print("Dane użytownika.\nImię: " +str(name)+", \nwiek: " +str(age)+", \nmiasto: " +str(city)+".")


#Zadanie 2
square_1 = 2
square_2 = 7
square_3 = 11
square_4 = 19

print("Pole powierzchni kwadratu 1 wynosi:" +str(square_1 ** 2))
print("Pole powierzchni kwadratu 2 wynosi:" +str(square_2 ** 2))
print("Pole powierzchni kwadratu 3 wynosi:" +str(square_3 ** 2))
print("Pole powierzchni kwadratu 4 wynosi:" +str(square_4 ** 2))

print("Obwód kwadratu 1 wynosi:" +str(square_1 * 4))
print("Obwód kwadratu 2 wynosi:" +str(square_2 * 4))
print("Obwód kwadratu 3 wynosi:" +str(square_4 * 4))
print("Obwód kwadratu 4 wynosi:" +str(square_4 * 4))

print("Długość przekątnej kwadratu 1 wynosi:" +str(square_1 * 2**(1/2)))
print("Długość przekątnej kwadratu 2 wynosi:" +str(square_2 * 2**(1/2)))
print("Długość przekątnej kwadratu 3 wynosi:" +str(square_3 * 2**(1/2)))
print("Długość przekątnej kwadratu 4 wynosi:" +str(square_4 * 2**(1/2)))


#Zadanie 3

initial_balance = 46567.
interest = 7.5
year_balance = initial_balance * (interest/100) + initial_balance
two_year_balance = year_balance *(interest/100) + year_balance
three_year_balance = two_year_balance *(interest/100) + two_year_balance
print(two_year_balance)

print("Inwestowane środki wynoszą: " +str(initial_balance)+ ".","Stałe oprocentowanie wynosi: " +str(interest)+"%.", "Zysk z 3 letniej lokaty bankowej wynosi: " +str(three_year_balance - initial_balance)+" zł.")