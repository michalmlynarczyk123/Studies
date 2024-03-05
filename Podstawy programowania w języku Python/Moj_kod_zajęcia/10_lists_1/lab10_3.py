#Napisz skrypt, który znajdzie najczęsciej występującą cyfrę w zbiorze.
#Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4, występuje 3 razy.

digits = [1, 2, 3, 99, 99]
frequency = []
for i in range(100):
    frequency.append(0)

for digit in digits:
    frequency[digit] += 1
print(digits)
print(frequency)

most_common = 0

for i in range(len(frequency)):
    if frequency[i] > frequency[most_common]:
        most_common = i
print("Najczęściej występującą cyfrą jest: ", str(most_common), ". Wystąpiła: ", frequency[most_common], "razy.")