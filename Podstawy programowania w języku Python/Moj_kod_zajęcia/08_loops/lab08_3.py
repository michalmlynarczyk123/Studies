sum = 0

for i in range(64):
    #r = 2 ** i
    sum += 2 ** i
    #print("pole nr: ", i + 1, "ile ziaren", r)

print("Suma wszystkich zairen na szachownicy: ", sum)

#rozważania
#założenia:
#waga 1 ziarenka pszenicy 0,4 mg -> 0,0004 g
#1kg = 1000 g
#1t = 1000 kg

tons = sum * 0.0004 / 1000 / 1000
print("Ton: ", tons)

#roczna produkcja pszenicy na świecie 782 mln ton

years = int(tons / 782_000_000)
print("lata: ", years)

#pociąg może transportować 2200 t

trains = int(tons / 2200)
print("ile pociągów: ", trains)