import csv

with open('test.csv', encoding='UTF-8') as file:
    headers = file.readline()
    reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)

headers = ['Imię', 'Nazwisko', 'Pesel']
users = [
    ["Janek", "Kowalski", 123456],
    ["Michał", "Kowal", 123456],
    ["Anna", "Kowal", 123456],
    ["Test", "Test", 123456],
]

with open('test.csv', 'w', encoding='utf-8', newline='') as output:
    writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(headers)
    writer.writerows(users)
