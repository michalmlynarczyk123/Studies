graduate = int(input("podaj liczbę punktów (0-100): "))

print("Twoja ocena jest", end=" ")

if graduate  >= 95:
    print("badzo dobra (5,0)")
elif graduate > 84:
    print("ponad dobra (4,5)")
elif graduate >= 70:
    print("dobra (4,0)")
elif graduate >= 60:
    print("dość dobra (3,5)")
elif graduate >= 50:
    print("dostateczna (3,0)")
else:
    print("niedostateczna")