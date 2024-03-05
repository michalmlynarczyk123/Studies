from random import sample

def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = sample(numbers, 6)
    lucky_numbers.sort()
    return lucky_numbers

def get_user_numbers():
    n = 6
    counter = 1
    user_numbers = []
    while counter < n + 1:
        try:
            number = int(input("Podaj liczbę {} (1-49): ".format(counter)))
            if number in user_numbers:
                print("Powtórzona liczba!")
                continue
            if number < 1 or number > 49:
                print("Należy podać liczbę z przedziału 1-49!")
                continue
        except:
            print("To nie jest liczba.")
            continue
        user_numbers.append(number)
        counter += 1
    user_numbers.sort()
    return user_numbers

def check_numbers(user_numbers, lucky_numbers):
    counter = 0
    for number in user_numbers:
        if number in lucky_numbers:
            counter += 1
    return counter

if __name__ == "__main__":
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_numbers(user_numbers, lucky_numbers)
    print(user_numbers)
    print(lucky_numbers)
    print(result)

