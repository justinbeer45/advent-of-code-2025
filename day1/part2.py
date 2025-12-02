# initialize arrow pointing value
arrow = 50
zeros = 0

# import input data
test_data = []

with open('day1/input.txt', encoding="utf-8") as f:
    for line in f:
        test_data.append(line.strip())

# print(len(test_data))
# print(test_data)
# test_data = ['L898','R100','L5']

# if L then subtract from current arrow value, else if R then add to current arrow value
# rotor values 0-99
# L127 means we subtract 127 from 27 and the new arrow value is 100
for rotation in test_data:
    if rotation[0] == 'L':
        if (arrow - int(rotation[1:])) < 0:
            if arrow > 0:
                zeros += 1
            if (abs(arrow - int(rotation[1:]))) > 100:
                if (abs(arrow - int(rotation[1:]))) % 100 == 0:
                    zeros += ((abs(arrow - int(rotation[1:]))) // 100) - 1
                else:
                    zeros += (abs(arrow - int(rotation[1:]))) // 100
            if (abs(arrow - int(rotation[1:])) % 100) == 0:
                print(f'{rotation} means we subtract {rotation[1:]} from {arrow} and the new arrow value is 0')
                arrow = (abs(arrow - int(rotation[1:])) % 100)
            else:
                print(f'{rotation} means we subtract {rotation[1:]} from {arrow} and the new arrow value is {100 - (abs(arrow - int(rotation[1:])) % 100)}')
                arrow = 100 - (abs(arrow - int(rotation[1:])) % 100)
        else:
            print(f'{rotation} means we subtract {rotation[1:]} from {arrow} and the new arrow value is {arrow - int(rotation[1:])}')
            arrow = arrow - int(rotation[1:])
    else:
        print(f'{rotation} means we add {rotation[1:]} to {arrow} and the new arrow value is {(arrow + int(rotation[1:])) % 100}')
        if (arrow + int(rotation[1:])) > 100:
            if (arrow + int(rotation[1:])) % 100 == 0:
                zeros += ((arrow + int(rotation[1:])) // 100) - 1
            else:
                zeros += (arrow + int(rotation[1:])) // 100
        arrow = (arrow + int(rotation[1:])) % 100
    if arrow == 0:
        zeros += 1
    print(f'Zeros: {zeros}')

print(f'Zeros: {zeros}')
