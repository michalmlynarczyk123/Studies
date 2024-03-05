########################TUPLES _ KROTKI########################

# numbers = (1, 2, 3)
# numbers = ()
# numbers = 1, 2, 3
# numbers = (1,)


# print(numbers[1:])
# print(numbers[:])
# ------------------------------------------


# numbers = tuple(x for x in range(10) if x % 2 == 0)
#
# print(len(numbers))
# print(numbers * 2)
# print(numbers + numbers + numbers)
# ------------------------------------------


# numbers = [1, 2, 3]
# numbers = tuple(numbers)
#
# print(numbers)
# ------------------------------------------


# letters = tuple("Ala ma kota.")
# print(letters)


########################SŁOWNIKI########################

# phones = {"Tomek": 555678856, "Ada": 234333444, "Karol": 777777777, "Tomek": 111111111}
#
# print(phones)
# ------------------------------------------

# animals_dict = {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
#
# print(animals_dict["kot"])
# print(animals_dict.get("kot"))
# print(animals_dict.get("wiewiórka", "Brak takiego klucza w słowniku."))

words = ["kot", "lew", "chomik"]
#
# for word in words:
#     if word in animals_dict:
#         print(word, "->", animals_dict[word])
#     else:
#         print("Nie znaleziono słowa {} w słowniku".format(word))
# ------------------------------------------


animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

# for key in sorted(animals_dict.keys()):
#     print(key, animals_dict[key])

# for k, v in animals_dict.items():
#     print(k, v)

# animals_dict["świnka"] = "pig"
# animals_dict.update({"kurczak": "chicken"})
# animals_dict.update({"świnka": "piggy"})

# print(animals_dict)

# animals_dict_2 = animals_dict.copy()
# del animals_dict_2["kurczak"]
# animals_dict_2.popitem()
#
#
# print(animals_dict)
# print(animals_dict_2)