import random

# kod znaku A to 65 --> ord("A")
# kod znaku E to 69 --> ord("A")
# print(ord("E"))

FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 5

def draw_letter():
    # return chr(random.randint(ord("A"), ord("E"))) pierwsza wersja
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))

def draw_row():
    return [draw_letter() for i in range(NUMBER_OF_LETTERS)]

print(draw_row())

# def check(row):
#     #if row[0] == row[1] and row[1] == row[2]: na dole prostszy zapis
#     if row[0] == row[1] == row[2]:
#         return True
#     else:
#         return False #pierwsza wersja

def check(row):
    first_element = row[0]
    for e in row:
        if first_element != e:
            return False
    return True

counter  = 1
while(True):
    row = draw_row()
    print(row, counter)
    if (check(row)):
        break
    counter += 1