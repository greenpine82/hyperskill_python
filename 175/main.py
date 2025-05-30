import random


number = int(input("Enter the number of friends joining (including you):"))
if number <= 0:
    print("No one is joining for the party")
    exit()
print("Enter the name of every friend (including you), each on a new line:")
results = {input(): 0 for i in range(number)}
bill = int(input("Enter the total bill value:"))
lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
if lucky == 'Yes':
    name = list(results)[random.randint(0, number - 1)]
    print(f"{name} is the lucky one!")
    for member in results:
        if member == name:
            continue
        results[member] = round(bill / (number - 1), 2)
elif lucky == 'No':
    print("No one is going to be lucky")
    for member in results:
        results[member] = round(bill / number, 2)
print(results)