with open('input.txt', 'r') as f:
    input = f.readlines()

passwords = (passw.strip() for passw in input if passw.strip())
passwords = tuple(map(lambda x: x.split(": "), passwords))

valid_passwords = 0 

def pass_validator(line):
    constraint, passw = line

    values, letter = constraint.split(" ")

    idx1, idx2 = values.split('-')

    num = 0

    idx1 = int(idx1) - 1
    idx2 = int(idx2) - 1

    if passw[idx1] == letter:
        num += 1
    if passw[idx2] == letter:
        num += 1

    return num == int(1)


i = 0
while i < len(passwords):
    if pass_validator(passwords[i]):
        valid_passwords += 1
    i += 1

print("Num of passwords: ", valid_passwords)