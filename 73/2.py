tokens = input()
list = [[tokens[i * 3], tokens[i * 3 + 1], tokens[i * 3 + 2]] for i in range(3)]
print('---------')
for i in range(3):
    print('| ' + ' '.join(list[i]) + ' |')
print('---------')
