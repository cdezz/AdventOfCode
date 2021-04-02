import re

with open("input.txt", 'r') as f:
    passports = f.read()
    passports = passports.split('\n\n')

first = passports[0]

length = len(passports)

def check_validity(p: str):
    regex = re.findall('[a-z]{3}:', p)
    if len(regex) == 8:
        return True
    elif len(regex) == 7 and ('cid:' in set(regex)):
        return True
    return False

print(check_validity(first))

valid = 0
while i < length:
    i = 0
    if check_validity(passports[i]):
        valid += 1
    i += 1
