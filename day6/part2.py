

with open('day6/input.txt') as f:
    input_data = f.read()

input_data = input_data.split('\n')

data_lists = []
for line in input_data:
    data_lists.append([])
    for c in line:
        data_lists[-1].append(c)


# for line in data_lists:
#     print(line)




# find when there is a row of all spaces and convert to another value that we can split on
for i in range(len(data_lists[0])):
    all_spaces = True
    for j in range(len(data_lists)):
        if data_lists[j][i] != ' ':
            all_spaces = False
    if all_spaces:
        for j in range(len(data_lists)):
            data_lists[j][i] = 'split!'

# print('\n\n')
# for line in data_lists:
#     print(line)



# put each problem in a list based on right-left value rules for cephalapods
data_split = []
num_list = []
for i in range(len(data_lists[0])):
    if data_lists[0][i] == 'split!':
        data_split.append(num_list)
        num_list = []
        continue
    num_str = ''
    for j in range(len(data_lists) - 1):
        if data_lists[j][i] != '':
            num_str += data_lists[j][i]
    num_list.append(int(num_str))
# add the last problem's digits
data_split.append(num_list)
    
# print(data_split)
# for problem in data_split:
#     print(problem)

# get the operators for each problem
operators = input_data[-1].strip()
operators = operators.split()
# print(operators)

# go through each problem and get the appropriate total, add this total to a grand total
grand_total = 0
for i in range(len(data_split)):
    operator = operators[i]
    if operator == '*':
        total = 1
        for num in data_split[i]:
            total *= num
    elif operator == '+':
        total = 0
        for num in data_split[i]:
            total += num
    else:
        print(f'Something went wrong with operator: {operator}')
    grand_total += total

print(f'Grand total: {grand_total}')
