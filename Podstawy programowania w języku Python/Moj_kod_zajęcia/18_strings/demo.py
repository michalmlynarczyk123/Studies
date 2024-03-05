# txt = "Ala ma kota."
#
# print(len(txt))
# print(len(""))
# print(len("\n\t\\"))

# txt = """To jest tekst.
# ten tekst ma kilka linii.
# Raz, dwa, trzy"""

# txt = """a
# b
# c"""
#
# print(txt)
# print(len(txt))

# ---------------------------------------------------------------------------

# str1 = "a"
# str2 = "b"
#
# print(str1 + str2)
# print(str2 + str1)
#
# print(5 * str1)
# print(str1 * 5)


# ---------------------------------------------------------------------------

# char1 = "a"
# char2 = " "
#
# print(ord(char1))
# print(ord(char2))
# print(chr(98))

# print(hex(ord("ę")))
# print("\u0119")


# ---------------------------------------------------------------------------
# UTF-8

# character = "a"
# character = "€"
#
# print(character, ord(character), hex(ord(character)), character.encode())


# ---------------------------------------------------------------------------
#      123456789......
# txt = "Ala ma kota."
#
# # for c in txt:
# #     print(c, end=" ")
#
# print(txt[4:6])
# print(txt[-1:])
# print(txt[2::3])

# ---------------------------------ALFABET------------------------------------------
# generuj alfabet

# print(ord("a"))
# print(ord("z"))

alfabet = ""

# for i in range(ord("a"), ord("z") +1):
#     print(chr(i), end=" ")

for i in range(ord("a"), ord("z") +1):
    alfabet += chr(i)
# print(alfabet)

# print("a" in alfabet)
# print("ą" in alfabet)
# print("ą" not in alfabet)

# del alfabet[0]
# del alfabet
# alfabet.append("A") #nie działa tutaj
# alfabet.insert(2, "A") #nie działa tutaj
# alfabet = "A" + alfabet
# print(alfabet)


# print(min([1,2,3]))
# print(min("aaabbABC"))
#
# for c in "aaabbABC":
#     print(c, ord(c))
#
# print(">" + min("Ala ma kota.") + "<")

# print(alfabet.index("W"))
# print("aAbB".index("A"))
# print([1,2,3].index(1))
print(list(alfabet))
print(alfabet.count("a"))
print("Ala ma kota.".count(" ", ))
print([1,2,3,2].count(2))