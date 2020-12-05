"""
[1721, 979, 366, 299, 675, 1456]

    In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 =
    514579, so the correct answer is 514579.
"""
import copy

print("**********\t\t DAY 1 EVENT 1 \t\t**********")
# set that will store input integers
input_set = set()
with open("day1_input.txt") as f:
    # create a list from input txt file
    read_data = f.read().split("\n")
    for line in read_data:
        if line:
            # drop newline character to convert from str to int
            line = line.replace("\n", "")
            input_set.add(int(line))

# year is the required sum
year = 2020
# result will store answer to question
result = 0
for ele in input_set:
    difference = year - ele
    if difference in input_set:
        result = difference * ele
        print(f"{ele} * {difference} = {result}")

"""             DAY 1 EVENT 2              

    Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together 
    produces the answer, 241861950.

    In your expense report, what is the product of the three entries that sum to 2020?
"""
print("**********\t\t DAY 1 EVENT 2 NEXT \t\t**********")
for ele in input_set:
    # deep copy because items will be removed
    temp_set = copy.deepcopy(input_set)
    temp_set.remove(ele)
    temp_sum = year - ele
    for second_ele in temp_set:
        third_ele = temp_sum - second_ele
        if third_ele in temp_set:
            result = ele * second_ele * third_ele
            print(f"{ele} * {second_ele} * {third_ele} = {result}")
