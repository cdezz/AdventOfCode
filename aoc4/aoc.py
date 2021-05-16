import re

with open("input.txt", 'r') as f:
    passports = f.read()
    passports = passports.split('\n\n')

length = len(passports)

def check_validity(p: str):
    regex = re.findall('[a-z]{3}:', p)
    if len(regex) == 8:
        return True
    elif len(regex) == 7 and ('cid:' not in set(regex)):
        return True
    return False

valid = 0
i = 0
while i < length:
    if check_validity(passports[i]):
        valid += 1
    i += 1

print('Valid Passports: ', valid)
