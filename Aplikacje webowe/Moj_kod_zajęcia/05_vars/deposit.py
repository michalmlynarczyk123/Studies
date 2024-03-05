#Zadanie 3

initial_balance = 46567.
interest = 7.5
year_balance = initial_balance * (interest/100) + initial_balance
two_year_balance = year_balance *(interest/100) + year_balance
three_year_balance = two_year_balance *(interest/100) + two_year_balance
print(two_year_balance)

print("Inwestowane środki wynoszą: " +str(initial_balance)+ ".","Stałe oprocentowanie wynosi: " +str(interest)+"%.", "Zysk z 3 letniej lokaty bankowej wynosi: " +str(three_year_balance - initial_balance)+" zł.")
