import sys
io = sys.stdin
lines = []
for line in io:
    lines.append(line.rstrip())

for i in range(len(lines)):
    lines[i] = lines[i].split(": ")[1]

total_score = 0

for line in lines:
    score = 0
    [winning_nums, my_nums] = line.split(" | ")
    winning_nums = set([int(i)for i in winning_nums.split(" ") if i.isnumeric()])
    my_nums = [int(i) for i in my_nums.split(" ") if i.isnumeric()] 
    for num in my_nums:
        if num in winning_nums:
            if score == 0:
                score = 1
            else:
                score = score * 2
    total_score += score

print(total_score)

match_arr = [{"matches": 0, "count": 1 } for i in range(len(lines))]

for i in range(len(lines)):
    [winning_nums, my_nums] = lines[i].split(" | ")
    winning_nums = set([int(i)for i in winning_nums.split(" ") if i.isnumeric()])
    my_nums = [int(i) for i in my_nums.split(" ") if i.isnumeric()] 
    for num in my_nums:
        if num in winning_nums:
            match_arr[i]["matches"] = match_arr[i]["matches"] + 1


running_sum = 0
for i in range(len(match_arr)):
    for j in range(match_arr[i]["matches"]):
        if i + j + 1 < len(match_arr):
            match_arr[i + j + 1]["count"] = match_arr[i + j + 1]["count"] + match_arr[i]["count"] 


print(sum([i["count"] for i in match_arr]))