# ------------------------------KROTKI------------------------------

# numbers = (1, 2, 3)
# numbers = 1, 2, 3
# numbers = ()
# numbers = (1,)

# for i in numbers:
#     print(i)
#
# print("-" * 15)
#
# print(numbers[1:])
# print(numbers[:])

# --------------------------------------------------------------

# numbers = tuple(x for x in range(10) if x % 2 ==0)

# del numbers
# print(numbers)
#
# print(len(numbers))
# print(numbers * 2)
# print(numbers)
# print(numbers + numbers)

# -------------------------------------------------------------- konwertowanie

# numbers = [1,2,3]
# numbers = tuple(numbers)
#
# print(numbers)

# letters = tuple("Ala ma kota.")
#
# print(letters)

# ------------------------------SŁOWNIKI------------------------------

# phones = {"Tomek": 555666777,"Ada": 123456789, "Karol": 753159684, True: 123}
# phones = {"Tomek": 555666777,"Ada": 123456789, "Karol": 753159684, True: 123, "Tomek": 789428671}
#
# print(phones)
# print(phones["Tomek"])

animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

# print(animals_dic["kot"])
# print(animals_dic.get("kot"))
# # print(animals_dic["wiewiórka"])
# print(animals_dic.get("wiewiórka"))
# print(animals_dic.get("wiewiórka", "Brak takiego klucza w słowniku!"))

words = ["kot", "lew", "chomik"]

# for word in words:
#     if word in animals_dict:
#         print(word, "-->", animals_dict[word])
#     else:
#         print("Nie znaleziono słowa {} w słowniku".format(word))

# for key in animals_dict.keys():
# for key in animals_dict:
for key in sorted(animals_dict):
    print(key, animals_dict[key])

for v in animals_dict.values():
    print(v)

for t in animals_dict.items():
    print(t)

for k, t in animals_dict.items():
    print(k, t)

# ------------------------------SŁOWNIKI MODYFIKACJE------------------------------

# animals_dict["świnka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"świnka": "piggy"})
#
# # print(animals_dict)
#
# animals_dict_2 = animals_dict.copy()
# # del animals_dict_2["kurczak"]
# # animals_dict_2.popitem()
# animals_dict_2.clear()
#
#
# print(animals_dict)
# print(animals_dict_2)