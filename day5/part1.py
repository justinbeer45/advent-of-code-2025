

fresh_ranges = []
ingredients = []
fresh_ingredients = 0


with open('day5/input.txt', encoding="UTF-8") as f:
    input_data = f.read()

input_data = input_data.split('\n')
# print(input_data)

for data in input_data:
    if '-' in data:
        fresh_ranges.append(data.split('-'))
    elif data != '':
        ingredients.append(int(data))

# print(fresh_ranges)
# print(ingredients)

for ingredient in ingredients:
    for fresh_range in fresh_ranges:
        if ingredient in range(int(fresh_range[0]), int(fresh_range[1]) + 1):
            fresh_ingredients += 1
            # print(f'Ingredient: {ingredient} is fresh and in range {fresh_range[0]}-{fresh_range[1]}')
            break

print(f'There are {fresh_ingredients} fresh ingredients.')

