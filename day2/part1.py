
invalid_ids = 0

# import data
with open('day2/input.txt', encoding="UTF-8") as f:
    test_data = f.read()

# print(test_data)
# print(type(test_data))

test_data = test_data.split(',')

# print(test_data)

# go through each range one by one and determine the min and max of the range
for r in test_data:
    split = r.split('-')
    minimum = int(split[0])
    maximum = int(split[1])
    # print(f'For range {r}, the min is {minimum} and the max is {maximum}')
    # check each ID in the range one by one
    for i in range(minimum, maximum + 1):
        # convert to string
        i = str(i)
        # no need to check an ID if it's length is odd
        if len(i) % 2 == 0:
            # if the ID length is even, slice the string in half assigning to variables
            half1 = i[:len(i)//2]
            half2 = i[len(i)//2:]
            # print(f'{half1},{half2}')
            # convert the halfs back to ints and evaluate for equality
            if int(half1) == int(half2):
                # print(f'ID: {i} is invalid, splits to {half1} and {half2}')
                # if the halves are equal add to running total of invalid IDs (e.g. 123123)
                invalid_ids += int(i)

print(f'The invalid IDs sum to {invalid_ids}')