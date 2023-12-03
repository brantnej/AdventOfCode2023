import sys
io = sys.stdin
lines = []
for line in io:
    lines.append(line.rstrip())

row_size = len(lines[0])
col_size = len(lines)

gear_dict = {}

def is_part(row_num, start_idx, end_idx):
    # check left
    if start_idx != 0:
        if lines[row_num][start_idx - 1] != '.':
            return True
    if end_idx != row_size - 1:
        if lines[row_num][end_idx + 1] != '.':
            return True
    if row_num != 0:
        for i in range(max(start_idx - 1, 0), min(end_idx + 2, row_size)):
            if lines[row_num - 1][i] != '.':
                return True
    if row_num != col_size - 1:
        for i in range(max(start_idx - 1, 0), min(end_idx + 2, row_size)):
            if lines[row_num + 1][i] != '.':
                return True
    return False

def check_gear(row_num, start_idx, end_idx, num):
    # check left
    if start_idx != 0:
        if lines[row_num][start_idx - 1] == '*':
            if (row_num, start_idx - 1) in gear_dict:
                gear_dict[(row_num, start_idx - 1)].append(num)
            else: 
                gear_dict[(row_num, start_idx - 1)] = [num]
    if end_idx != row_size - 1:
        if lines[row_num][end_idx + 1] == '*':
            if (row_num, end_idx + 1) in gear_dict:
                gear_dict[(row_num, end_idx + 1)].append(num)
            else: 
                gear_dict[(row_num, end_idx + 1)] = [num]
    if row_num != 0:
        for i in range(max(start_idx - 1, 0), min(end_idx + 2, row_size)):
            if lines[row_num - 1][i] == '*':
                if (row_num - 1, i) in gear_dict:
                    gear_dict[(row_num - 1, i)].append(num)
                else: 
                    gear_dict[(row_num - 1, i)] = [num]
    if row_num != col_size - 1:
        for i in range(max(start_idx - 1, 0), min(end_idx + 2, row_size)):
            if lines[row_num + 1][i] == '*':
                if (row_num + 1, i) in gear_dict:
                    gear_dict[(row_num + 1, i)].append(num)
                else: 
                    gear_dict[(row_num + 1, i)] = [num]
    return False

total_sum = 0

for i in range(len(lines)):
    start_idx = 0
    current_num = ""
    in_num = False
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            current_num+=lines[i][j]
            if not in_num:
                start_idx = j
                in_num = True
        else:
            if in_num:
                if is_part(i, start_idx, j - 1):
                    total_sum += int(current_num)
                current_num = ""
                start_idx = 0
                in_num = False
    if in_num:
        if is_part(i, start_idx, len(lines[i]) - 1):
            total_sum += int(current_num)

print(total_sum)

for i in range(len(lines)):
    start_idx = 0
    current_num = ""
    in_num = False
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            current_num+=lines[i][j]
            if not in_num:
                start_idx = j
                in_num = True
        else:
            if in_num:
                check_gear(i, start_idx, j - 1, current_num)
                current_num = ""
                start_idx = 0
                in_num = False
    if in_num:
        check_gear(i, start_idx, len(lines[i]) - 1, current_num)

gear_sum = 0
for (index, arr) in gear_dict.items():
    if len(arr) == 2:
        gear_sum += int(arr[0]) * int(arr[1])
print(gear_sum)