import copy

fresh_ranges = []
fresh_ids = []
fresh_ingredients = 0


with open('day5/input.txt', encoding="UTF-8") as f:
    input_data = f.read()

input_data = input_data.split('\n')
# print(input_data)

for data in input_data:
    if '-' in data:
        fresh_ranges.append(data.split('-'))

# print(fresh_ranges)

# convert everything to integers
for i in range(len(fresh_ranges)):
    fresh_ranges[i][0] = int(fresh_ranges[i][0])
    fresh_ranges[i][1] = int(fresh_ranges[i][1])

# print(fresh_ranges)

# sort according to minimum value of range
    # go through each range 1 by 1
        # go through each 
fresh_ranges_min_sort = []
for i in range(len(fresh_ranges)):
    if i == 0:
        fresh_ranges_min_sort.append(fresh_ranges[0])
    else:
        range_sorted = False
        for j in range(len(fresh_ranges_min_sort)):
            # print(f'comparing {fresh_ranges_min_sort[j][0]} with {fresh_ranges[i][0]}')
            if fresh_ranges[i][0] < fresh_ranges_min_sort[j][0]:
                # print(f'inserting {fresh_ranges[i]} at position {j} of {fresh_ranges_min_sort}')
                fresh_ranges_min_sort.insert(j, fresh_ranges[i])
                # print(f'result {fresh_ranges_min_sort}')
                range_sorted = True
                break
            elif fresh_ranges[i][0] == fresh_ranges_min_sort[j][0]:
                # print('-----------------------')
                # print(fresh_ranges[i], ' and ', fresh_ranges[j], 'have the same minimum')
                # if the mins are equal sort by the maxes
                if fresh_ranges[i][1] < fresh_ranges_min_sort[j][1]:
                    fresh_ranges_min_sort.insert(j, fresh_ranges[i])
                    # print(fresh_ranges_min_sort[-1])
                    # print(fresh_ranges_min_sort[-2])
                    # print('----------------------------')
                else:
                    fresh_ranges_min_sort.insert(j+1, fresh_ranges[i])
                    # print(fresh_ranges_min_sort[-1])
                    # print(fresh_ranges_min_sort[-2])
                    # print('----------------------------')
                range_sorted = True
                break
        if not range_sorted: 
            # print(f"{fresh_ranges[i]}'s minimum wasn't less than or equal to any existing elements of the sorted list, appending to the sorted list.")
            fresh_ranges_min_sort.append(fresh_ranges[i])
# print(f'\n\n\n')
# for r in fresh_ranges_min_sort:
#     print(r)
# print(f'There are {len(fresh_ranges)} elements in the fresh ranges list.')
# print(f'There are {len(fresh_ranges_min_sort)} elements in the fresh ranges sorted by minimum list.')



#------------------------------------------------------------------

for i in range(len(fresh_ranges_min_sort)):
    for j in range(len(fresh_ranges_min_sort)):
            if i != j:
                # handle the case where a min/max are both contained in another range
                if fresh_ranges_min_sort[j][0] <= fresh_ranges_min_sort[i][0] <= fresh_ranges_min_sort[j][1] and fresh_ranges_min_sort[j][0] <= fresh_ranges_min_sort[i][1] <= fresh_ranges_min_sort[j][1]:
                    # if fresh_ranges_min_sort[i] != [0, 0]:
                        # print(f'the current range: {fresh_ranges_min_sort[i]} and the range that contains the current range: {fresh_ranges_min_sort[j]}')
                    fresh_ranges_min_sort[i] = [0, 0]
                # otherwise, sort based on the max value being in a subsequent range and update the current max value
                if fresh_ranges_min_sort[j][0] <= fresh_ranges_min_sort[i][1] <= fresh_ranges_min_sort[j][1]:
                    # print(f'extending {fresh_ranges_min_sort[i]} to {[fresh_ranges_min_sort[i][0], fresh_ranges_min_sort[j][1]]}')
                    fresh_ranges_min_sort[i][1] = fresh_ranges_min_sort[j][1]
                    # print(f'{fresh_ranges_min_sort[j]} covered by {fresh_ranges_min_sort[i]}, setting to [0, 0]')
                    fresh_ranges_min_sort[j] = [0, 0]

# for r in fresh_ranges_min_sort:
#     print(r)

for r in fresh_ranges_min_sort:
    if r != [0, 0]:
        # print(f'used {r} to get {r[1] - r[0] + 1}')
        fresh_ingredients += r[1] - r[0] + 1

print(f'There are {fresh_ingredients} fresh IDs.')




