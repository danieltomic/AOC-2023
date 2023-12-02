import os

path = os.path.abspath(__file__)
path_list = path.split(os.sep)
dir = path_list[0:len(path_list)-1]
input = "/".join(dir) + "/" + "input.txt"

with open(input, 'r') as file:
    data = file.read().split('\n')

max_counts = {'red': 12, 'green': 13, 'blue': 14}
part_one = 0
part_two = 0

for line in data:
    game_id, cubes_info = line.split(':')
    game_id = int(game_id[5:])  

    cubes_info = cubes_info.replace(',', '').replace(';', '').split()
    valid = True
    highest_appearing = {'red': 0, 'green': 0, 'blue': 0}

    for i in range(0, len(cubes_info), 2):
        color = cubes_info[i + 1]
        count = int(cubes_info[i])

        highest_appearing[color] = max(highest_appearing[color], count)  

        if count > max_counts[color]:
            valid = False

    part_two += highest_appearing['red'] * highest_appearing['green'] * highest_appearing['blue']

    if valid:
        part_one += game_id

print(part_one)
print(part_two)