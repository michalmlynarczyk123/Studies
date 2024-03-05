#Xq|`gf(bm{|(nibfq) - szyfr

#każdy czwarty bit zmieniono na przeciwny
#bity liczymy od najmniej znaczącego
# 0 0 0 0 1 0 1 1 ---> 0 0 0 0 0 0 1 1

print(ord("c"), chr(99))
print("{:08b}".format(ord("c")))
# 0011 - chcemy zmienić czwarty bit od prawej
# 1000 - maska pozwala nam wyizolować dany bit
# 1011 - używamy XORa (alternatywy rozłącznej) do zmiany bitu

print("{:08b}".format(ord("c") ^ (1 << 3)))

print(chr(ord("c") ^ (1 << 3)))

str = "Xq|`gf(bm{|(nibfq)"

for c in str:
    t = chr(ord(c) ^ (1 << 3))
    print(t, end = "")