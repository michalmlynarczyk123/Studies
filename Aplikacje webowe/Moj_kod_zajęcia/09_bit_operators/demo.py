#jeżeli będzie dodatnia temperatura i będzie słonecznie to..
#pojdziemy na spacer..
#a jeśli nie to zostaniemy w domu..

temperature = -1 #12
is_sun_shining = True #False

if temperature > 0 and is_sun_shining:
    print("Idziemy na spacer.")
else:
    print("Zostaniemy w domu.")
print("-" * 20)

#jeżeli będzie dodatnia temperatura lub będzie pochmurnie to...
#zostaniemy w domu, a jeśli nie to pójdziemy na spacer

if not(temperature < 0 or not is_sun_shining): #not() jest zastosowane żeby zanegować printy poniżej
    print("Idziemy na spacer")
else:
    print("Zostaniemy w domu")

#Operatory logiczne
#and - koniunkcja logiczna. Czytamy jak "i"
#or - alternatywa, to albo to. Czytamy jak "lub"
#not - czytamy jak "nie"

a, b, c = 2, 3, 4

if a < b and b < c:
    print("!!!")

if a < b < c:
    print("!!!")  #łączenie łańcuchowe, to samo co na górze tylko zapis inny