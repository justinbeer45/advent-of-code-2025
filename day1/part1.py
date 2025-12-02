# initialize arrow pointing value
arrow = 50
zeros = 0

test_data = []

# import input data
with open('day1/input.txt', encoding="utf-8") as f:
    for line in f:
        test_data.append(line.strip())

# if L then subtract from current arrow value, else if R then add to current arrow value
# rotor values 0-99
for rotation in test_data:
    if rotation[0] == 'L':
        if (arrow - int(rotation[1:])) < 0:
            if (abs(arrow - int(rotation[1:])) % 100) == 0:
                arrow = (abs(arrow - int(rotation[1:])) % 100)
            else:
                arrow = 100 - (abs(arrow - int(rotation[1:])) % 100)
        else:
            arrow = arrow - int(rotation[1:])
    else:
        arrow = (arrow + int(rotation[1:])) % 100
    if arrow == 0:
        zeros += 1

print(f'Zeros: {zeros}')
