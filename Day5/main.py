import sys
io = sys.stdin
lines = []
for line in io:
    lines.append(line.rstrip())

seeds = [int(i) for i in lines[0].split("seeds: ")[1].split()]


def create_map(i):
    mapping = []
    while i < len(lines) and lines[i] != "":
        mapping.append([int(j) for j in lines[i].split()])
        i = i + 1
    return mapping, i

maps = []
i = 3
while i < len(lines):
    mapping, i = create_map(i)
    maps.append(mapping)
    i = i + 2

res = []

for seed in seeds:
    for layer in maps:
        for mapping in layer:
            if seed in range(mapping[1], mapping[1]+mapping[2]):
                seed = mapping[0] + seed - mapping[1]
                break
    res.append(seed)
print(min(res)) 

def get_min(maps, seeds):
    j = 0
    while True:
        seed = j
        for i in range(len(maps) - 1, -1, -1):
            for mapping in maps[i]:
                if seed in range(mapping[0], mapping[0]+mapping[2]):
                    seed = mapping[1] + seed - mapping[0]
                    break
        for k in range(0, len(seeds), 2):
            if seed >= seeds[k] and seed < (seeds[k] + seeds[k+1]):
                print(j)
                return
        j = j + 1

get_min(maps, seeds)