def reverse_dict(d):
    d_swap = {v: k for k, v in d.items()}
    return d_swap

print(reverse_dict({'a': 1, 'b': 2}))