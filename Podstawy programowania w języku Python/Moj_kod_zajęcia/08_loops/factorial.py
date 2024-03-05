#silnia - 3! = 1 * 2 * 3 = 6

number = 3
factorial = 1

#for i in range(1, number + 1):
    #print("---", "i=" + str(i), "factorial" + str(factorial))
    #factorial *= i

#print(factorial)

#wszystko prócz zera jest True

while number:
    factorial *= number
    number -= 1
print(factorial)
