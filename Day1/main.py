import sys
io = sys.stdin
lines = []
for line in io:
    lines.append(line)

num_dict = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine',
    'zero': 'zero0zero',
}

sum = 0
for x in lines:
    # Day 2 modification
    for key, val in num_dict.items():
        x = x.replace(key, val)

    num = ''
    for i in range(len(x)):
        if x[i-1].isdigit():
            num = x[i-1]
            break
    for i in range(len(x), 0, -1):
        if x[i-1].isdigit():
            num += x[i-1]
            break
    sum += int(num)
print(sum)
