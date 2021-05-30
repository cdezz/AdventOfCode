from collections import Counter

with open('input.txt', 'r') as f:
    input = f.read()

# [' \na\nb\nc', 'ab\nac', 'a\na\na\na', 'b\n']
groups = [group for group in input.split('\n\n')]

count = 0

def yes_count(group):
    group = group.strip().replace('\n', '')
    print(f"Count for {group} is: ", Counter(group).keys().__len__())
    return Counter(group).keys().__len__()

for g in groups:
    count += yes_count(g)

print(count)