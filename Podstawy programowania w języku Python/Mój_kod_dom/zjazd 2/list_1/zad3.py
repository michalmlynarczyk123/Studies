digits = [4, 1, 2, 9, 4, 4, 4, 4, 5, 1, 2, 2, 2, 2, 2, 2]
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for digit in digits:
    frequency[digit] += 1
print(digits)
print(frequency)

most_common = 0
for i in range(len(frequency)):
    if frequency[i] > frequency[most_common]:
        most_common = i
print("Najczęściej występująca cyfrą jest", str(most_common), ",", "wystąpiła", frequency[most_common], "razy.")
