import os
path = os.path.abspath(__file__)
path_list = path.split(os.sep)
dir = path_list[0:len(path_list)-1]
input = "/".join(dir) + "/" + "input.txt"

with open(input, 'r') as file:
    data = file.read().split('\n')

def convert(line):
    for index, name in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        line = line.replace(name, f"{name}{index}{name}")
    return line

def solve():
    part_one = 0
    part_two = 0
    for line in data:
        digit = [char for char in line if char.isdigit()]
        part_one += int(digit[0] + digit[-1])
        
        digit = [char for char in convert(line) if char.isdigit()]
        part_two += int(digit[0] + digit[-1])

    print(part_one, part_two)

solve()
