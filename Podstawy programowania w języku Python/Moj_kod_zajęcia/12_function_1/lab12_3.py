# # growth = int(input("Podaj swój wzrost: "))
# # weight = int(input("Podaj swoją wagę: "))
#
# #(weigth / (growth **2))
#
# def get_BMI():
#     return int(input("Proszę podaj swoją wagę: "))
#     return int(input("Proszę podaj swój wzrost: "))
#
#
# print(get_BMI())
# print(get_BMI())

print("Obliczanie wskaźnika BMI")

weight_kg = float(input("Podaj swoją wagę (kg): "))
hight_cm = float(input("Podaj swój wzrost (cm): "))


def calculate_BMI(weight_kg, hight_m):
    return weight_kg / hight_m ** 2


def determine_BMI_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"


bmi = calculate_BMI(weight_kg, hight_cm * .01)
category = determine_BMI_category(bmi)

print("Wskaźnik BMI: ", round(bmi, 2))
print("Kategoria: ", category)
