graduate = int(input("Podaj liczbę punktów (0-100): "))
print("Twoja ocena to:", end = ' ')

if graduate >= 95:
    print("5.0")
elif graduate > 85:
    print("4.5")
elif graduate >= 70:
    print("4.0")
elif graduate >= 60:
    print("3.5")
elif graduate >= 50:
    print("3.0")
else:
    print("niedostateczna")