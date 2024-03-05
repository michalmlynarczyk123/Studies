# dokonaj analizy wystąpień poszczególnych liter

letters = {}

try:
    for line in open("znachor.txt", encoding="UTF-8"):
        if len(line) > 1:
            for char in line:
                char = char.lower()
                if char >= "a" and char <= "z":
                    if char in letters:
                        letters[char] = letters[char] + 1
                    else:
                        letters[char] = 1
except IOError as e:
    print(f"Nie mogę otworzyć pliku: {e}")

letters = dict(sorted(letters.items()))
print(letters)