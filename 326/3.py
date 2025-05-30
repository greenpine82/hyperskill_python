import re


re_id = re.compile("^[A-Za-z]+(['-]?[A-Za-z]+)+$")
re_mail = re.compile("^[\w.]+@([\w]+\.)+[\w]+$")
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
        if len(list(filter(lambda r: r[0] == tokens[-1], records))) > 0:
            print("This email is already taken.")
            continue
        records.append([tokens[-1], 10000 + len(records)])
        print("The student has been added.")
        counter += 1
    print(f"Total {counter} students have been added.")


def list_students(records):
    if len(records) == 0:
        print("No students found.")
    print("Students:")
    print('\n'.join([str(r[1]) for r in records]))


def validate(inputs):
    return len(inputs) == 5 and all([t.isnumeric() for t in inputs[1:]])


def add_points(records):
    print("Enter an id and points or 'back' to return:")
    while (text := input()) != 'back':
        tokens = text.split()
        if not validate(tokens):
            print("Incorrect points format.")
            continue
        if tokens[0].isnumeric() and 0 <= (index := int(tokens[0]) - 10000) < len(records):
            record = records[index]
            if len(record) != 6:
                record += [int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4])]
            else:
                record[2] += int(tokens[1])
                record[3] += int(tokens[2])
                record[4] += int(tokens[3])
                record[5] += int(tokens[4])
            print("Points updated.")
        else:
            print(f"No student is found for id={tokens[0]}.")


def find_student(records):
    print("Enter an id or 'back' to return:")
    while (text := input()) != 'back':
        if text.isnumeric() and 0 <= (index := int(text) - 10000) < len(records):
            record = records[index]
            print(f"{record[1]} points: Python={record[2]}; DSA={record[3]}; Databases={record[4]}; Flask={record[5]}")
        else:
            print(f"No student is found for id={text}.")


print("Learning progress tracker")
records = list()
while True:
    i = input()
    if len(i.strip()) == 0:
        print("No input.")
        continue
    if i == "back":
        print("Enter 'exit' to exit the program")
        continue
    if i == "add students":
        add_student(records)
    if i == "list":
        list_students(records)
        continue
    if i == "add points":
        add_points(records)
        continue
    if i == "find":
        find_student(records)
        continue
    if i == "exit":
        print("Bye.")
        break
    print("Unknown command!")
    continue