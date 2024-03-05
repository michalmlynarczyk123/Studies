#pobierz od użytkownika trzy odcinki (liczby całkowite)
#sprawdź czy można z nich zbudować trójkąt (np. 3, 4, 5 - tak)
#jaki to jest trójkąt ze względu na boki (różnoboczny, równoboczny, równoramienny), (np. 5, 5, 5)
#jaki to trójkąt ze względu na kąty (prostokątny, ostrokątny, rozwarty), (np. 9, 9, 16)

print("Podaj wartości trzech odcinków (liczby całkowite)")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and b + c > a and a + c > b:
    print("Z tych odcinków można zbudować trójkąt", end = " ") #pierwszy warunek

    if a == b and b == c and c == a:
        print("równoboczny", end = " ")         #dugi warunek
    elif a == b or b == c or c == a:
        print("równoramienny", end = " ")
    else:
        print("różnoramienny", end = " ")

    if a ** 2 + b ** 2  == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        print("prostokątny", end = " ")          #trzeci warunek
    elif a ** 2 + b ** 2  < c ** 2 or b ** 2 + c ** 2 < a ** 2 or a ** 2 + c ** 2 < b ** 2:
        print("rozwartokątny", end = " ")
    else:
        print("ostrokątny.")
else:
    print("Niestety z tych odcinków nie powstanie trójkąt")
