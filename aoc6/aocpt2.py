from collections import Counter

with open('input.txt', 'r') as f:
    input = f.read()

# [' \na\nb\nc', 'ab\nac', 'a\na\na\na', 'b\n']
groups = [group for group in input.split('\n\n')]

count = 0

def yes_count(group):
    group_length = len(group.strip().split('\n'))
    
    group = group.strip().replace('\n', '')
    the_count = Counter(group).items()
    allY = list(filter(lambda x: x[1] == group_length, the_count))
    num_of_y = len(allY)
    return num_of_y


for g in groups:
    count += yes_count(g)

print(count)