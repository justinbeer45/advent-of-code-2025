

accessible = 0


with open('day4/input.txt', encoding="UTF-8") as f:
    input_data = f.read()

input_data = input_data.split()
print(input_data)

for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        print(input_data[i][j])


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

# when evaluating a paper bale at a specific position
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        counter = 0
        # only need to evaluate if the position holds a paper bale 
        if input_data[i][j] != '@':
            continue
        # it's impossible for position [0][0] to be boxed in so if there is a paper bale in [0][0] it will be accessible 
        if i == 0 and j == 0:
            print(f'position: [{i}][{j}] is accessible')
            accessible += 1
        # the same logic holds for position [0][-1]
        elif i == 0 and j == len(input_data[i]) - 1:
            print(f'position: [{i}][{j}] is accessible')
            accessible += 1
        # the logic for the the rest of row 0 is to check the position to the left, right, below-left, below, below-right
        elif i == 0:
            if input_data[i][j-1] == '@':
                counter += 1
            if input_data[i][j+1] == '@':
                counter += 1
            if input_data[i+1][j-1] == '@':
                counter += 1
            if input_data[i+1][j] == '@':
                counter += 1
            if input_data[i+1][j+1] == '@':
                counter += 1
            if counter < 4:
                print(f'position: [{i}][{j}] is accessible')
                accessible += 1
        # it's impossible for position [-1][0] to be boxed in so if there is a paper bale in [-1][0] it will be accessible 
        elif i == len(input_data) - 1 and j == 0:
            print(f'position: [{i}][{j}] is accessible')
            accessible += 1
        elif i == len(input_data) - 1 and j == len(input_data[i]) - 1:
            print(f'position: [{i}][{j}] is accessible')
            accessible += 1
        # the logic for the rest of row -1 is to check the position to the left, right, above-left, above, above-right
        elif i == len(input_data) - 1:
            if input_data[i][j-1] == '@':
                counter += 1
            if input_data[i][j+1] == '@':
                counter += 1
            if input_data[i-1][j-1] == '@':
                counter += 1
            if input_data[i-1][j] == '@':
                counter += 1
            if input_data[i-1][j+1] == '@':
                counter += 1
            if counter < 4:
                print(f'position: [{i}][{j}] is accessible')
                accessible += 1
        # the logic for position 0 of any other row is to check to the right, above, above-right, below, below-right
        elif j == 0:
            if input_data[i][j+1] == '@':
                counter += 1
            if input_data[i-1][j] == '@':
                counter += 1
            if input_data[i-1][j+1] == '@':
                counter += 1
            if input_data[i+1][j] == '@':
                counter += 1
            if input_data[i+1][j+1] == '@':
                counter += 1
            if counter < 4:
                print(f'position: [{i}][{j}] is accessible')
                accessible += 1
        # the logic for position -1 of any other row is to check to the left, above, above-left, below, below-left
        elif j == len(input_data[i]) - 1:
            if input_data[i][j-1] == '@':
                counter += 1
            if input_data[i-1][j] == '@':
                counter += 1
            if input_data[i-1][j-1] == '@':
                counter += 1
            if input_data[i+1][j] == '@':
                counter += 1
            if input_data[i+1][j-1] == '@':
                counter += 1
            if counter < 4:
                print(f'position: [{i}][{j}] is accessible')
                accessible += 1
        # for all other positions check to the left, right, above-left, above, above-right, below-left, below, below-right
        else:
            if input_data[i][j-1] == '@':
                counter += 1
            if input_data[i][j+1] == '@':
                counter += 1
            if input_data[i+1][j-1] == '@':
                counter += 1
            if input_data[i+1][j] == '@':
                counter += 1
            if input_data[i+1][j+1] == '@':
                counter += 1
            if input_data[i-1][j-1] == '@':
                counter += 1
            if input_data[i-1][j] == '@':
                counter += 1
            if input_data[i-1][j+1] == '@':
                counter += 1
            if counter < 4:
                print(f'position: [{i}][{j}] is accessible')
                accessible += 1
        

# count if a paper bale is in the previous or subsequent position on the same line
# in the previous, same, or subsequent position on the previous line
        
# in the previous, same, or subsequent position on the subsequent line
# if there are 4+ bales in any of the described surrounding positions, change the '@' to 'x'

print(f'There are {accessible} accessible paper bales.')
