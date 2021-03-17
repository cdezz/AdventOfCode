with open('input.txt') as f:
    text = f.readlines()

nums = (num.strip() for num in text if num.strip())
nums = tuple(map(lambda x: int(x), nums))

num_set = set()

def func(nums):
        
    for i in nums:
        for j in nums:
            num_set.add(j)
            k = 2020 - i - j
            if k in num_set:
               return i * j * k

print("Answer: ", func(nums))