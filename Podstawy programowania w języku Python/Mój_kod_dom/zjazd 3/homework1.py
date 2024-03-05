def merge_list_withouth_duplicates(source, target):
    for element in source:
        if element not in target:
            target.append(element)

def transform_data(list1):
    result = []
    merge_list_withouth_duplicates(list1, result)
    return tuple(result)

print(transform_data([1,2,2, 3,3,3,4,4,5,6,7,7,7,8,8,9,9,9,9,10]))