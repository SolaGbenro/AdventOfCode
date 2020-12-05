"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

    Each line gives the password policy and then the password. The password policy indicates the lowest and highest
    number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password
    must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but
    needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of
    their respective policies.
"""
import re

print("**********\t\t DAY 2 EVENT 1 \t\t**********")
input_list = []
with open("day2_input.txt") as f:
    read_data = f.read().split("\n")

    # each line will be separate index in list
    for line in read_data:
        input_list.append(line)

valid_pwrds = 0

for line in input_list:
    minMax, letter, password = re.split(": | ", line)
    # print(f"minMax = {minMax}, letter = {letter}, password = {password}")
    # separate the minimum and maximum counts
    minNum, maxNum = minMax.split("-")
    minNum, maxNum = int(minNum), int(maxNum)
    counter = 0
    # iterate through password string looking for matches
    for chr in password:
        if chr == letter:
            counter += 1
    # ensure constraints are met
    if (counter >= minNum) and (counter <= maxNum):
        valid_pwrds += 1

print(f"Number of valid passwords: {valid_pwrds}")

"""                 DAY 2 EVENT 2
    Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second 
    character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of 
    these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of 
    policy enforcement.

    Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""
print("**********\t\t DAY 2 EVENT 2 NEXT \t\t**********")
# separate variable for new valid passwords
new_valid_pswrd = 0
for line in input_list:
    # no longer counts, but indexes
    indexes, letter, password = re.split(": | ", line)
    idxOne, idxTwo = indexes.split("-")
    idxOne, idxTwo = int(idxOne), int(idxTwo)
    # must be just one index, not both
    if password[idxOne - 1] == password[idxTwo - 1]:
        continue
    if (password[idxOne - 1] == letter) or (password[idxTwo - 1] == letter):
        new_valid_pswrd += 1

print(f"Number of new valid passwords: {new_valid_pswrd}")
