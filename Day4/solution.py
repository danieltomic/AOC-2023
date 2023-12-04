import os

path = os.path.abspath(__file__)
path_list = path.split(os.sep)
dir = path_list[0:len(path_list)-1]
input = "/".join(dir) + "/" + "input.txt"

with open(input, 'r') as file:
    data = file.read().split('\n')

part_one = 0
part_two = [1] * len(data)
for index1, line in enumerate(data):
    line_points = 0
    print(line)
    substring = line.split('|')
    x = len(set(substring[0][9:].split()) & set(substring[1].split()))
    print(x)
    line_points += 2 ** (x - 1)
    if line_points >= 1:
        part_one += line_points
    for w in range(x):
        part_two[index1+w+1] += part_two[index1]
    print(line_points)

print(part_one)
print(sum(part_two))

p1 = [0.5]*len(data)
p2 = [1.0]*len(data)
# print(p1)

for i, line in enumerate(data):
    w, h = map(str.split, line.split('|'))

    for j in range(len(set(w) & set(h))):
        p1[i] *= 2
        p2[i+j+1] += p2[i]

# for p in p1, p2: print(sum(map(int, p)))


    # for winning_number in substring[0][9:].split():
    #     if any(num in winning_number for num in substring[1].split()):
    #         line_points += (2 ** counter)
    #         counter += 1
    # if line_points == 3:
    #     line_points = 2
    # else:
    #     line_points += 1
    # print(str(counter) + ' winning numbers')
    # print(line_points)
    # points += line_points

# print(p1)
# print(p2)