import re


re_id = re.compile("^[A-Za-z]+(['-]?[A-Za-z]+)+$")
re_mail = re.compile("^[\w.]+@(\w+\.)+\w+$")
def add_student(records):
    print("Enter student credentials or 'back' to return:")
    counter = 0
    while (text := input()) != 'back':
        tokens = text.split()
        if len(tokens) < 3:
            print("Incorrect credentials")
            continue
        if not re_id.match(tokens[0]):
            print("Incorrect first name")
            continue
        if not re_id.match(tokens[-2]):
            print("Incorrect last name")
            continue
        if not re_mail.match(tokens[-1]):
            print("Incorrect email")
            continue
        if len(list(filter(lambda r: r[1] == tokens[-1], records))) > 0:
            print("This email is already taken.")
            continue
        records.append([20000 + len(records), tokens[-1]])
        print("The student has been added.")
        counter += 1
    print(f"Total {counter} students have been added.")


def list_students(records):
    if len(records) == 0:
        print("No students found.")
    print("Students:")
    print('\n'.join([str(r[0]) for r in records]))


def validate(inputs):
    return len(inputs) == 5 and all([t.isnumeric() for t in inputs[1:]])


def add_points(records, data):
    print("Enter an id and points or 'back' to return:")
    while (text := input()) != 'back':
        tokens = text.split()
        if not validate(tokens):
            print("Incorrect points format.")
            continue
        if tokens[0].isnumeric() and 0 <= (index := int(tokens[0]) - 20000) < len(records):
            record = records[index]
            points = [int(t) for t in tokens[1:]]
            counts = [(1 if p > 0 else 0) for p in points]
            if len(record) != 6:
                record += points
                data['pop'] = [x + y for x, y in zip(data['pop'].copy(), counts)]
            else:
                record[2] += points[0]
                record[3] += points[1]
                record[4] += points[2]
                record[5] += points[3]
            data['activity'] = [x + y for x, y in zip(data['activity'].copy(), counts)]
            data['sum'] = [x + y for x, y in zip(data['sum'].copy(), points)]
            data['mean'] = [x / y if y > 0 else 0 for x, y in zip(data['sum'].copy(), data['activity'].copy())]
            print("Points updated.")
        else:
            print(f"No student is found for id={tokens[0]}.")


def find_student(records):
    print("Enter an id or 'back' to return:")
    while (text := input()) != 'back':
        if text.isnumeric() and 0 <= (index := int(text) - 20000) < len(records):
            record = records[index]
            print(f"{record[0]} points: Python={record[2]}; DSA={record[3]}; Databases={record[4]}; Flask={record[5]}")
        else:
            print(f"No student is found for id={text}.")


def report(name, data, get_top=True):
    top = ', '.join([name[i] for i, v in enumerate(data) if v == max(data)]) if sum(data) > 0 else 'n/a'
    bottom = ', '.join([name[i] for i, v in enumerate(data) if v == min(data)]) if (sum(data) > 0 and min(data) != max(data)) else 'n/a'
    return top if get_top else bottom


def statistic(student_records, data, name):
    print("Type the name of a course to see details or 'back' to quit:")
    print(f"Most popular: {report(name, data['pop'])}")
    print(f"Least popular: {report(name, data['pop'], get_top=False)}")
    print(f"Highest activity: {report(name, data['activity'])}")
    print(f"Lowest activity: {report(name, data['activity'], get_top=False)}")
    print(f"Easiest course: {name[data['mean'].index(max(data['mean']))] if sum(data['sum']) > 0 else 'n/a'}")
    print(f"Hardest course: {name[data['mean'].index(min(data['mean']))] if sum(data['sum']) > 0 else 'n/a'}")

    while (text := input()) != 'back':
        t = text[0].upper() + text[1:]
        c = text.upper()
        index = -1
        for i, v in enumerate(name):
            if v == t or v == c:
                index = i
                break
        else:
            print("Unknown course.")
            continue

        print(name[index])
        print(f"{'id':<6} points completed")
        for record in sorted(student_records, key=lambda x: x[index + 2], reverse=True):
            if record[index + 2] > 0:
                print(f"{record[0]:<6} {record[index + 2]:<6} {round(record[index + 2] / p[index] * 100, 1)}%")
        continue


print("Learning progress tracker")
student_records = list()
p = [600, 400, 480, 550]
name = ['Python', 'DSA', 'Databases', 'Flask']
data = {'pop': [0] * 4, 'activity': [0] * 4, 'sum': [0] * 4, 'mean': [0] * 4}
while True:
    i = input()
    if len(i.strip()) == 0:
        print("No input.")
        continue
    if i == "back":
        print("Enter 'exit' to exit the program")
        continue
    if i == "add students":
        add_student(student_records)
    if i == "list":
        list_students(student_records)
        continue
    if i == "add points":
        add_points(student_records, data)
        continue
    if i == "find":
        find_student(student_records)
        continue
    if i == "statistics":
        statistic(student_records, data, name)
        continue
    if i == "exit":
        print("Bye!")
        break
    print("Unknown command!")
    continue