# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ -> ST...
# delta 3
# tylko wielkie litery, bez polskich znaków, tylko litery (bez znaków sterujących i specjalnych)


delta = 3

# for i in range(ord("A"), ord("Z") + 1):
#     print(chr(i), end="")
#
# print()
#
# for i in range(ord("A") + delta, ord("Z") + delta + 1):
#     if i > ord("Z"):
#         i -= ord("Z") - ord("A") + 1
#     print(chr(i), end="")
#
# print("\n\n")

def decode_letter(letter, delta):
    if letter < "A" or letter > "Z":
        return letter
    n = ord(letter) - delta
    if n < ord("A"):
        n += ord("Z") - ord("A") + 1
    return chr(n)

def decote(string,delta):
    decoded = ""
    for c in string:
        decoded += decode_letter(c, delta)
    return decoded

txt = "VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ"
# VCBIU - szyfr
print(decote("VCBIU", delta))
print(decote("VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ", delta))
print(decote(txt, delta))
