import sys
io = sys.stdin
lines = []
for line in io:
    lines.append(line.rstrip())

sum = 0

def valid_pull(game):
    for pulls in game:
        for colors in pulls.split(", "):
            [count, color] = colors.split()
            count = int(count)
            if color == "red" and count > 12:
                return False
            if color == "green" and count > 13:
                return False
            if color == "blue" and count > 14:
                return False
    return True

def get_mins(game):
    min_red = min_blue = min_green = 0
    for pulls in game:
        for colors in pulls.split(", "):
            [count, color] = colors.split()
            count = int(count)
            if color == "red" and count > min_red:
                min_red = count
            if color == "green" and count > min_green:
                min_green = count
            if color == "blue" and count > min_blue:
                min_blue = count
    return min_red * min_blue * min_green

for line in lines:
    [id, game] = line[5:].split(":")
    id = int(id)
    game = game[1:]
    game = game.split("; ")
    sum += get_mins(game)
    # if valid_pull(game):
    #     sum += id
print(sum)

