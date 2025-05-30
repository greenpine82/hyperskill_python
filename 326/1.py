print("Learning progress tracker")
while True:
    i = input()
    if len(i.strip()) == 0:
        print("No input.")
        continue
    if i == "exit":
        print("Bye.")
        break
    print("Unknown command!")
    continue