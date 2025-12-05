batteries = []
maximum_joltage = 0

with open('day3/input.txt', encoding="UTF-8") as f:
    for line in f:
        batteries.append(line.strip())


print(batteries)

# go through the bank until you find a battery that has a lower joltage the the subsequent battery, removing this battery ensure the final
# joltage will always be larger than removing another battery
def remove_battery(bank):
    # remove_digit = bank[0]
    # remove_digit_index = 0 
    # remove the first smallest item
    battery_removed = False
    for i in range(len(bank) - 1):
        if bank[i] < bank[i + 1]:
            bank.pop(i)
            battery_removed = True
            break
    if not battery_removed:
        bank.pop()
    #     if bank[i] < remove_digit:
    #         remove_digit = bank[i]
    #         remove_digit_index = i
    # print(f'remove {remove_digit} at index {remove_digit_index}')
    # bank.pop(remove_digit_index)
    # print(bank)
    # print(len(bank))

def recombine(bank):
    joltage = ''
    for battery in bank:
        joltage += str(battery)
    return int(joltage)


# loop through each bank and turn the string into a list
for bank in batteries:
    bank_list = []
    for battery in bank:
        bank_list.append(int(battery))
    print(bank_list)
    while len(bank_list) > 12:
        remove_battery(bank_list)
        print(bank_list)
    max_bank = recombine(bank_list)
    print(max_bank)
    maximum_joltage += max_bank

# print(811111111119 < 811111111111)
print(f'maximum joltage: {maximum_joltage}')




















#     # pick the largest digit at position 0:len(str)-1 and store in variable digit1, make note of the index of this digit with variable digit1_index
#     digit1 = 0
#     digit1_index = 0
#     for i in range(len(bank_list) - 1):
#         if bank_list[i] > digit1:
#             digit1 = bank_list[i]
#             digit1_index = i
#     print(f"{bank}'s first digit is {digit1} at position {digit1_index}")
#     # then pick the largest digit at position digit1_index:len(str) and store in variable digit2
#     digit2 = 0
#     digit2_index = 0
#     for i in range(digit1_index + 1, len(bank_list)):
#         if bank_list[i] > digit2:
#             digit2 = bank_list[i]
#             digit2_index = i
#     print(f"{bank}'s second digit is {digit2} at position {digit2_index}")
# # combine digit1,digit2 and add to maximum joltage variable
#     bank_joltage = str(digit1) + str(digit2)
#     maximum_joltage += int(bank_joltage)
#     print(bank_joltage)
# # print maximum joltage
#     print(f'maximum joltage: {maximum_joltage}')