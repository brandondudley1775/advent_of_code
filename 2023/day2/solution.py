fstream = open("input.txt")
puzzle_input = fstream.readlines()
fstream.close()

def process_game(line):
    tokens = line.split(":")

    game_id = int(tokens[0].split()[-1])
    cube_max = {}
    for round in tokens[-1].split(";"):
        for counts in round.split(","):
            try:
                value = int(counts.split()[0])
                color = counts.split()[-1]
                if color not in cube_max:
                    cube_max[color] = 0
                if cube_max[color] < value:
                    cube_max[color] = value
            except:
                continue
    return game_id, cube_max

red_max = 12
green_max = 13
blue_max = 14
total = 0
power_total = 0
for line in puzzle_input:
    game_id, cube_max = process_game(line)
    # part 1
    add_id = True
    if 'red' not in cube_max or cube_max['red'] > red_max:
        add_id = False
    if 'green' not in cube_max or cube_max['green'] > green_max:
        add_id = False
    if 'blue' not in cube_max or cube_max['blue'] > blue_max:
        add_id = False
    if add_id:
        total += game_id

    # part 2
    blue_power = 0
    red_power = 0
    green_power = 0
    if 'blue' in cube_max:
        blue_power = cube_max['blue']
    if 'red' in cube_max:
        red_power = cube_max['red']
    if 'green' in cube_max:
        green_power = cube_max['green']
    power_total = power_total + (blue_power * green_power * red_power)

print("First answer:", total)
print("Second answer:", power_total)
