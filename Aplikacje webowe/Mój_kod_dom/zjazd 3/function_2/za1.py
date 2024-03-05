# pierwsze podejście
def power(numbers, exponent):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers


# drugie podejście
def power2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result


# trzecie podejście

def power3(numbers, exponent):
    return [x ** exponent for x in numbers]





print(power([1, 2, 3], 2))
print(power2([1, 2, 3], 2))
print(power3([1, 2, 3], 2))

print()

print(power([1, 2, 3], 5))
print(power2([1, 2, 3], 5))
print(power3([1, 2, 3], 5))