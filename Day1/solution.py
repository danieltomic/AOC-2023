import os
path = os.path.abspath(__file__)
path_list = path.split(os.sep)
dir = path_list[0:len(path_list)-1]
input = "/".join(dir) + "/" + "input.txt"

with open(input, 'r') as file:
    data = file.read().split('\n')

### PART ONE ###
def part_one():
    points = 0
    for line in data:
        digit = []
        for char in line:
            if char.isdigit():
                digit.append(char)
        combined = digit[0] + digit[-1]
        points += int(combined)
    print(points)


### PART TWO ###
import re
digit_dict = {
    'one': 'o1ne',
    'two': 't2wo',
    'three': 't3hree',
    'four': 'f4our',
    'five': 'f5ive',
    'six': 's6ix',
    'seven': 's7even',
    'eight': 'e8ight',
    'nine': 'n9ine'
}
def part_two():
    points = 0
    for line in data:

        for original, replacement in digit_dict.items():
            line = line.replace(original, replacement)
        
        digit = re.sub('\D', '', line)
        points += int(digit[0] + digit[-1])
    print(points)
    

part_one()
part_two()
        


