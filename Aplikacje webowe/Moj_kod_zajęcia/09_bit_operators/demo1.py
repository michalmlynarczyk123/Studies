a = 5
b = 3

#-------------------------------------------------koniunkcja bitowa-----------------------------------------------------
print(a, "&", b, "=", a & b)
#print(bin(a)) #binarnie

print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a & b))

#-------------------------------------------------alternatywa bitowa----------------------------------------------------

print(a, "|", b, "=", a | b)


print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a | b))

#-------------------------------------------------alternatywa rozłączna-------------------------------------------------

print(a, "^", b, "=", a ^ b)


print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a ^ b))

#-------------------------------------------------przesunięcie bitowew prawo--------------------------------------------

print(a, ">>", b, "=", a >> b)


print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a >> b))

#-------------------------------------------------przesunięcie bitowew lewo---------------------------------------------

print(a, "<<", b, "=", a << b)


print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a << b))

#-------------------------------------------------negacja bitowa--------------------------------------------------------

print("~" + str(a), "=", ~a)

print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))

#print("{:08b}".format(~a & 255))