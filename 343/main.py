if __name__ == '__main__':
    items = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250, 'Milk chocolate': 1680, 'Doughnut': 1075, 'Pancake': 80}
    print("Earned amount:")
    sum = 0
    for key in items.keys():
        print(f"{key}: ${items[key]}")
        sum += items[key]
    print(f"""
    Income: ${sum}""")
    sum -= int(input('Staff expenses:'))
    print(f"Net income: ${sum - int(input('Other expenses:'))}")