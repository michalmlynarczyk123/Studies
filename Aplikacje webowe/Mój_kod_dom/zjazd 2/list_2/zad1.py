import random

print("Podaj 6 liczb z zakresu 1-49")
user_number = []
random_number = []
hit_total = 0
for i in range(6):
    user_number.append(int(input("Podaj "+ str(i + 1)+ " liczbę: " )))
random_numbers = random.sample(range(1,50), 6)

for number in user_number:
    if number in random_numbers:
        hit_total += 1

random_numbers.sort()
user_number.sort()
print("Wylosowano: ", random_numbers)
print("Obstawiono: ", user_number)
print("Trafiono: ", hit_total, "liczb.")

