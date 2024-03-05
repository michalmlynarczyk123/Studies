def is_list_of_integers(lst):
    for e in lst:
        if not isinstance(e, int):
            return False
    return True

def sum_list(lst):
    return sum(lst)

def product_list(lst):
    product = 1
    for e in lst:
        product *= e
    return product

if __name__ == "__main__":
    lst = [1,2,3]
    print(is_list_of_integers((lst) == True))
    print(sum_list(lst) == 6)
    print(product_list(lst) == 6)
    print(is_list_of_integers([0,4, "99"] == False))