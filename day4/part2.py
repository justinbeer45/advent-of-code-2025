

bales_removed = 0
formatted_data = []
remove = []
bales_accessible = True


with open('day4/input.txt', encoding="UTF-8") as f:
    input_data = f.read()

input_data = input_data.split()
# print(input_data)




for i in range(len(input_data)):
    formatted_data.append([])
    for j in range(len(input_data[i])):
        formatted_data[i].append(input_data[i][j])

# print('-----------------------------------------')
# for line in formatted_data:
#     print(line)
# print('------------------------------------------')


# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.

while bales_accessible:
    accessible = 0
    # when evaluating a paper bale at a specific position
    for i in range(len(formatted_data)):
        for j in range(len(formatted_data[i])):
            counter = 0
            # only need to evaluate if the position holds a paper bale 
            if formatted_data[i][j] != '@':
                continue
            # it's impossible for position [0][0] to be boxed in so if there is a paper bale in [0][0] it will be accessible 
            if i == 0 and j == 0:
                # print(f'position: [{i}][{j}] is accessible')
                accessible += 1
                remove.append((i,j))
            # the same logic holds for position [0][-1]
            elif i == 0 and j == len(formatted_data[i]) - 1:
                # print(f'position: [{i}][{j}] is accessible')
                accessible += 1
                remove.append((i,j))
            # the logic for the the rest of row 0 is to check the position to the left, right, below-left, below, below-right
            elif i == 0:
                if formatted_data[i][j-1] == '@':
                    counter += 1
                if formatted_data[i][j+1] == '@':
                    counter += 1
                if formatted_data[i+1][j-1] == '@':
                    counter += 1
                if formatted_data[i+1][j] == '@':
                    counter += 1
                if formatted_data[i+1][j+1] == '@':
                    counter += 1
                if counter < 4:
                    # print(f'position: [{i}][{j}] is accessible')
                    accessible += 1
                    remove.append((i,j))
            # it's impossible for position [-1][0] to be boxed in so if there is a paper bale in [-1][0] it will be accessible 
            elif i == len(formatted_data) - 1 and j == 0:
                # print(f'position: [{i}][{j}] is accessible')
                accessible += 1
                remove.append((i,j))
            elif i == len(formatted_data) - 1 and j == len(formatted_data[i]) - 1:
                # print(f'position: [{i}][{j}] is accessible')
                accessible += 1
                remove.append((i,j))
            # the logic for the rest of row -1 is to check the position to the left, right, above-left, above, above-right
            elif i == len(formatted_data) - 1:
                if formatted_data[i][j-1] == '@':
                    counter += 1
                if formatted_data[i][j+1] == '@':
                    counter += 1
                if formatted_data[i-1][j-1] == '@':
                    counter += 1
                if formatted_data[i-1][j] == '@':
                    counter += 1
                if formatted_data[i-1][j+1] == '@':
                    counter += 1
                if counter < 4:
                    # print(f'position: [{i}][{j}] is accessible')
                    accessible += 1
                    remove.append((i,j))
            # the logic for position 0 of any other row is to check to the right, above, above-right, below, below-right
            elif j == 0:
                if formatted_data[i][j+1] == '@':
                    counter += 1
                if formatted_data[i-1][j] == '@':
                    counter += 1
                if formatted_data[i-1][j+1] == '@':
                    counter += 1
                if formatted_data[i+1][j] == '@':
                    counter += 1
                if formatted_data[i+1][j+1] == '@':
                    counter += 1
                if counter < 4:
                    # print(f'position: [{i}][{j}] is accessible')
                    accessible += 1
                    remove.append((i,j))
            # the logic for position -1 of any other row is to check to the left, above, above-left, below, below-left
            elif j == len(formatted_data[i]) - 1:
                if formatted_data[i][j-1] == '@':
                    counter += 1
                if formatted_data[i-1][j] == '@':
                    counter += 1
                if formatted_data[i-1][j-1] == '@':
                    counter += 1
                if formatted_data[i+1][j] == '@':
                    counter += 1
                if formatted_data[i+1][j-1] == '@':
                    counter += 1
                if counter < 4:
                    # print(f'position: [{i}][{j}] is accessible')
                    accessible += 1
                    remove.append((i,j))
            # for all other positions check to the left, right, above-left, above, above-right, below-left, below, below-right
            else:
                if formatted_data[i][j-1] == '@':
                    counter += 1
                if formatted_data[i][j+1] == '@':
                    counter += 1
                if formatted_data[i+1][j-1] == '@':
                    counter += 1
                if formatted_data[i+1][j] == '@':
                    counter += 1
                if formatted_data[i+1][j+1] == '@':
                    counter += 1
                if formatted_data[i-1][j-1] == '@':
                    counter += 1
                if formatted_data[i-1][j] == '@':
                    counter += 1
                if formatted_data[i-1][j+1] == '@':
                    counter += 1
                if counter < 4:
                    # print(f'position: [{i}][{j}] is accessible')
                    accessible += 1
                    remove.append((i,j))
    bales_removed += accessible
            

    # count if a paper bale is in the previous or subsequent position on the same line
    # in the previous, same, or subsequent position on the previous line
            
    # in the previous, same, or subsequent position on the subsequent line
    # if there are 4+ bales in any of the described surrounding positions, change the '@' to 'x'

    # print(f'There are {accessible} accessible paper bales.')
    print(f'{bales_removed} bales have been removed')

    # print(remove)

    for removal in remove:
        formatted_data[removal[0]][removal[1]] = '.'

    # for line in formatted_data:
    #     print(line)

    if accessible == 0:
        bales_accessible = False