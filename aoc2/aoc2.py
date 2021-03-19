from collections import Counter
import operator

with open('input.txt', 'r') as f:
    input = f.readlines()

passwords = (passw.strip() for passw in input if passw.strip())
passwords = tuple(map(lambda x: x.split(": "), passwords))

valid_passwords = 0 

def pass_validator(line):
    constraint, passw = line

    values, letter = constraint.split(" ")

    min, max = values.split('-')

    word_count = Counter(passw)

    if (int(min) <= int(word_count[letter])):
        if (int(word_count[letter]) <= int(max)):
            return True
    return False

i = 0
while i < len(passwords):
    if pass_validator(passwords[i]):
        valid_passwords += 1
    i += 1

print(valid_passwords)