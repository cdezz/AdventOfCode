with open('input.txt') as f:
    text = f.readlines()

nums = (num for num in text if num)

num_set = set()

def find_product(num):
    if num.strip():
        num = int(num)
        num_set.add(num)
        if (2020 - num) in num_set:
            ans = num * (2020 - num)
            print(ans)

for num in nums:
    find_product(num)