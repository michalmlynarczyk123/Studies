names = []

total_elements = int(input("Ile imion chcesz wprowadzić: "))

for i in range(total_elements):
    names.append(input("Podaj " +str(i +1)+ " imię: "))
print(names)