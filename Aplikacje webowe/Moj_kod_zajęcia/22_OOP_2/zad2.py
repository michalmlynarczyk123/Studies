class C:
    counter = 0

    def __init__(self):
        C.counter += 1

    def get_counter(self):
        return C.counter

for _ in range(100):
    c = C()

print(c.get_counter())

C()
print(c.get_counter())