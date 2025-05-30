import re


re_id = re.compile("^[A-Za-z]+(['-]?[A-Za-z]+)+$")
re_mail = re.compile("^[\w.]+@([\w]+\.)+[\w]+$")
def add_student():
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
        print("The student has been added.")
        counter += 1
    print(f"Total {counter} students have been added.")


print("Learning progress tracker")
while True:
    i = input()
    if len(i.strip()) == 0:
        print("No input.")
        continue
    if i == "back":
        print("Enter 'exit' to exit the program")
        continue
    if i == "add students":
        add_student()
    if i == "exit":
        print("Bye.")
        break
    print("Unknown command!")
    continue