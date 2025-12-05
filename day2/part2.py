import math

invalid_ids = 0

# import data
with open('day2/input.txt', encoding="UTF-8") as f:
    test_data = f.read()

# print(test_data)
# print(type(test_data))

test_data = test_data.split(',')

# print(test_data)
def all_same(str_id):
    all_same = True
    for c in str_id:
        if len(str_id) == 1:
            all_same = False
        if int(c) != int(str_id[0]):
            all_same = False
    return all_same


def half_and_half(str_id):
    half_and_half = False
    # no need to check an ID if it's length is odd
    if len(str_id) % 2 == 0:
        # if the ID length is even, slice the string in half assigning to variables
            half1 = i[:len(i)//2]
            half2 = i[len(i)//2:]
            if int(half1) == int(half2):
                # if the halves are equal return True
                half_and_half = True
    return half_and_half


def mod2_pattern(str_id):
    # # divide  string into chunks of 2
    if len(str_id) % 2 != 0:
        return False
    if len(str_id) == 2:
        return False
    number_chunks = []
    counter = 0
    same_numbers = True
    for i in range(len(str_id) // 2):
        number_chunks.append(int(str_id[counter:counter+2]))
        counter += 2
    for i in number_chunks:
        if i != number_chunks[0]:
            same_numbers = False
    return same_numbers

def mod3_pattern(str_id):
    # # divide  string into chunks of 3
    if len(str_id) % 3 != 0:
        return False
    if len(str_id) == 3:
        return False
    number_chunks = []
    counter = 0
    same_numbers = True
    for i in range(len(str_id) // 3):
        number_chunks.append(int(str_id[counter:counter+3]))
        counter += 3
    for i in number_chunks:
        if i != number_chunks[0]:
            same_numbers = False
    return same_numbers



def mod4_pattern(str_id):
    # # divide  string into chunks of 3
    if len(str_id) % 4 != 0:
        return False
    if len(str_id) == 4:
        return False
    number_chunks = []
    counter = 0
    same_numbers = True
    for i in range(len(str_id) // 4):
        number_chunks.append(int(str_id[counter:counter+4]))
        counter += 4
    for i in number_chunks:
        if i != number_chunks[0]:
            same_numbers = False
    return same_numbers



def mod5_pattern(str_id):
    # # divide  string into chunks of 3
    if len(str_id) % 5 != 0:
        return False
    if len(str_id) == 5:
        return False
    number_chunks = []
    counter = 0
    same_numbers = True
    for i in range(len(str_id) // 5):
        number_chunks.append(int(str_id[counter:counter+5]))
        counter += 5
    for i in number_chunks:
        if i != number_chunks[0]:
            same_numbers = False
    return same_numbers



def mod6_pattern(str_id):
    # # divide  string into chunks of 3
    if len(str_id) % 6 != 0:
        return False
    if len(str_id) == 6:
        return False
    number_chunks = []
    counter = 0
    same_numbers = True
    for i in range(len(str_id) // 6):
        number_chunks.append(int(str_id[counter:counter+6]))
        counter += 6
    for i in number_chunks:
        if i != number_chunks[0]:
            same_numbers = False
    return same_numbers

        

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
        # check if the digits of the id are all the same
        if all_same(i):
            print(f'Digits of {i} are all the same')
            invalid_ids += int(i)
        # check if id has pattern where first half matches second half (don't check ids that were all the same digit)
        elif half_and_half(i):
            print(f'{i} matches the half/half pattern')
            invalid_ids += int(i)
        # check if id has pattern where first 2, 3, 4, ... (len(id)/2 - 1) are the same digits
        elif mod2_pattern(i):
            print(f'{i} matches a mod2 pattern')
            invalid_ids += int(i)
        elif mod3_pattern(i):
            print(f'{i} matches a mod3 pattern')
            invalid_ids += int(i)
        elif mod4_pattern(i):
            print(f'{i} matches a mod4 pattern')
            invalid_ids += int(i)
        elif mod5_pattern(i):
            print(f'{i} matches a mod5 pattern')
            invalid_ids += int(i)
        elif mod6_pattern(i):
            print(f'{i} matches a mod6 pattern')
            invalid_ids += int(i)

print(f'The invalid IDs sum to {invalid_ids}')