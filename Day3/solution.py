import os

path = os.path.abspath(__file__)
path_list = path.split(os.sep)
dir = path_list[0:len(path_list)-1]
input = "/".join(dir) + "/" + "input.txt"

with open(input, 'r') as file:
    data = file.read().split('\n')

from collections import defaultdict

part_one = 0
part_two = 0
gears = defaultdict(list)

for i, line in enumerate(data):
    n = 0
    valid = False
    gear = False

    for j, char in enumerate(line):
        if char.isdigit():
            n = n * 10 + int(char)

            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    try:
                        cc = data[i + y][j + x]
                        if cc != '.' and not cc.isdigit():
                            valid = True
                            if cc == '*':
                                gear = (i + y, j + x)
                    except IndexError:
                        continue

        if not char.isdigit() or j == len(line) - 1:
            if valid:
                part_one += n
                valid = False
            if gear:
                gears[gear].append(n)
                if len(gears[gear]) == 2:
                    part_two += n * gears[gear][0]
                gear = False
            n = 0

print(part_one)
print(part_two)

