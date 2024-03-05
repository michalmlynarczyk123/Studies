""" This is my first own module """


def is_string(val):
    """ Simple string value validator """
    return isinstance(val, str)

def sum_list_elem(lst):
    sum = 0
    for e in lst:
        sum += e
    return sum


if __name__ == "__main__":
    print(is_string("hahaha") == True)
    print(is_string(123) == False)
    print(is_string([1, 2, 3]) == False)
    print(sum_list_elem([1, 2, 3]) == 6)
    print(sum_list_elem([]) == 0)

print(dir())
