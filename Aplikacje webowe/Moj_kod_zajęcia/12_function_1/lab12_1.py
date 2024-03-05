def print_char(char="*", repeat=10, vertical=False):
    for i in range(repeat):
        if vertical:
            print(char)
        else:
            print(char + " ", end="")
    if not vertical:
        print()
    print()

print_char()
print_char("$", 5, True)
print_char("^", 100)