name = "Michał"
age = 28
town = "Kraków"


print("Mam na imię: " + str(name) + ". " + "Mam " + str(age) + "lat. Mieszkam w " + str(town))

initial_balance = 46_576
percent = 7.5
one_year = initial_balance * 1.075
two_year = one_year * 1.075
three_year = two_year * 1.075



print("Inwestycja wynosi: " +str(initial_balance)+ "zł. Po roku przy stałym rocznym oprocentowaniu: " + str(percent)+ "% wynosi: " +str(one_year)+ "zł. Po dwóch latach wynosi: " +str(two_year)+ "zł. Po trzech latach wynosi: " +str(three_year)+ "zł.Całkowity zysk z 3 letniej lokaty wynosi: " +str(three_year - initial_balance)+ "zł")