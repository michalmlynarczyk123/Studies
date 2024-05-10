import csv

with open('test.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(f'{row.get("Imię", "Brak Imienia")} {row["Nazwisko"]}, {row["Pesel"]}')

print(20 * '-')

with open('test.csv', 'r', encoding='utf-8', newline='') as file:
    headers = ['jeden', 'dwa', 'trzy', 'cztery']
    reader = csv.DictReader(file, delimiter=',', fieldnames=headers)
    for row in reader:
        print(row)
