
problems = []

with open('day6/input.txt') as f:
    input_data = f.read()

# print(input_data)

problems = input_data.split('\n')

# print(problems)

cleaned_data = []

for problem in problems:
    # print(type(problem))
    cleaned_data.append(problem.strip())

# print(cleaned_data)

final_data = []
for d in cleaned_data:
    final_data.append(d.split())

# for line in final_data:
#     print(line)
# print(final_data)

# for line in final_data:
#     print(len(line))

grand_total = 0
for i in range(len(final_data[-1])):
    operator = final_data[-1][i]
    nums = []
    for j in range(len(final_data) - 1):
        nums.append(int(final_data[j][i]))
    # print(nums, operator)
    if operator == '*':
        total = 1
        for num in nums:
            total *= num
    elif operator == '+':
        total = 0
        for num in nums:
            total += num
    else:
        print(f'Something went from the operator: {operator}')
    grand_total += total

print(f'Grand total: {grand_total}')
    
 
