#Elektorniczny dziennki z ocenami studentów
# - wprwadzanie ocen studentów
# - wyświetlanie ocen wraz z obliczoną średnią


def text_format(text, width=25):
    pattern = "{:" + str(width) + "s}"
    return pattern.format(text)

def average(marks):
    return sum(marks) / len(marks)

def get_data():
    students = {}
    while(True):
        student = input("Podaj imię studenta: ")
        if student == "":
            break
        mark = float(input("Podaj ocenę: "))
        if mark < 2 or mark > 5:
            break
        if student in students:
            marks = students[student]
            marks.append(mark)
        else:
            marks = [mark]
        students.update({student: marks})
    return students

def print_summary(students):
    counter = 1
    for student in students:
        marks = students[student]
        print(counter, student, "oceny:", text_format(str(marks)), "średnia:", round(average(marks), 2))
        counter += 1

print_summary(get_data())