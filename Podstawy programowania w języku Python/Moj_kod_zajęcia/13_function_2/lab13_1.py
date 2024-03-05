# 1

def pow(numbers, exponent):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers


# 2
def pow2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result


# 3

def pow3(numbers, exponent):
    return [x ** exponent for x in numbers]


numbers = [1, 2, 3]

print(pow(numbers, 2))
print(pow2(numbers, 2))
print(pow3(numbers, 2))

print()

print(pow(numbers, 5))
print(pow2(numbers, 5))
print(pow3(numbers, 5))

print()