print("Podaj zakres liczb od 1 do 100")
range_from = int(input("od: "))
range_to = int(input("do: "))

for number in range(range_from, range_to + 1):
    if number % 3 == 0 or number % 5 ==0 or number %7 ==0:
        print(number, end=" ")